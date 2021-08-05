import weasyprint
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from quote.forms import QuoteItemFormSet, QuoteForm
from .models import Quote
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


class QuoteListView(ListView):
    model = Quote
    template_name = 'quote/list.html'


class QuoteDetailView(DetailView):
    model = Quote
    template_name = 'quote/detail.html'


@login_required
def quote_pdf(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)

    html = render_to_string('quote/pdf_template.html',
                            {'quote': quote})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=quote_{quote.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[
                                               weasyprint.CSS(settings.STATIC_ROOT + 'css/bootstrap.min.css'),
                                               weasyprint.CSS(settings.STATIC_ROOT + 'css/styles.css'), ])
    return response
