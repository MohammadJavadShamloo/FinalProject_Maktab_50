from django.shortcuts import redirect
from django.views.generic import CreateView

from quote.forms import QuoteItemFormSet, QuoteForm
from .utils import calculate_off, calculate_tax


class QuoteCreateView(CreateView):
    form_class = QuoteForm
    template_name = 'quote/create.html'

    def get_context_data(self, **kwargs):
        context = super(QuoteCreateView, self).get_context_data(**kwargs)
        context['formset'] = QuoteItemFormSet()
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        quote_item_formset = QuoteItemFormSet(self.request.POST)
        if form.is_valid and quote_item_formset.is_valid():
            return self.form_valid(form, quote_item_formset)
        else:
            return self.form_invalid(form, quote_item_formset)

    def form_valid(self, form, quote_item_formset):
        self.object = form.save(commit=False)
        self.object.registrar = self.request.user
        self.object.save()
        quote_items = quote_item_formset.save(commit=False)
        for item in quote_items:
            item.quote = self.object
            item.price_before_tax = calculate_off(item.product.price * item.count_of_product, item.off_percent)
            item.price_after_tax = calculate_tax(item.price_before_tax, 9 if item.product.tax else 0)
            item.save()
        return redirect('organization:organization_list')

    def form_invalid(self, form, quote_item_formset):
        return self.render_to_response(self.get_context_data(form=form,
                                                             quote_item_price=quote_item_formset))
