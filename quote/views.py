import weasyprint
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from quote.forms import QuoteItemFormSet, QuoteForm
from .models import Quote
from .utils import calculate_off, calculate_tax
from .tasks import send_quote


class QuoteCreateView(CreateView):
    """
    Class Based View For Creating Quotes By Formsets
    """
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
        self.object.total_price = self.object.items.aggregate(total_price=Sum('price_after_tax'))['total_price']
        self.object.total_count = self.object.items.aggregate(total_count=Sum('count_of_product'))['total_count']
        self.object.save()
        return redirect('quote:quote_list')

    def form_invalid(self, form, quote_item_formset):
        return self.render_to_response(self.get_context_data(form=form,
                                                             quote_item_price=quote_item_formset))


class QuoteListView(ListView):
    """
    Class Based View For Listing Available Quotes
    """
    model = Quote
    template_name = 'quote/list.html'


class QuoteDetailView(DetailView):
    """
    Class Based View For Showing Details Of A Quote
    """
    model = Quote
    template_name = 'quote/detail.html'


@login_required
def quote_pdf(request, quote_id):
    """
    View For Making Pdf For Quotes
    :param request: request
    :param quote_id: id of quote
    :return:
    """
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


def send_quote_to_organization(request, quote_id, organization_id):
    """
    View To Send Quotes By Contact Email Of Organization
    :param request: request
    :param quote_id: quote id
    :param organization_id: organization id
    :return: mail status
    """
    is_sent = send_quote.delay(quote_id, organization_id)
    return is_sent
