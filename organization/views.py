from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from .forms import ReportForm
from .models import *
from inventory.models import Product


class CreateOrganizationView(LoginRequiredMixin, CreateView):
    """
    a View for creating new Organizations
    """
    model = Organization
    template_name = 'organization/create.html'
    fields = [
        'province',
        'name',
        'phone',
        'workers_count',
        'products',
        'contact_name',
        'contact_phone',
        'contact_email',
    ]
    success_url = reverse_lazy('organization:list_organization')

    def form_valid(self, form):
        form.instance.registrar = self.request.user
        return super(CreateOrganizationView, self).form_valid(form)


class UpdateOrganizationView(LoginRequiredMixin, UpdateView):
    """
        a View for updating new Organizations
    """
    model = Organization
    template_name = 'organization/update.html'
    fields = [
        'province',
        'name',
        'phone',
        'workers_count',
        'products',
        'contact_name',
        'contact_phone',
        'contact_email',
    ]
    success_url = reverse_lazy('organization:list_organization')


class ListOrganizationView(LoginRequiredMixin, ListView):
    """
        a View for listing new Organizations
    """
    model = Organization
    template_name = 'organization/list.html'
    paginate_by = 15


class DetailOrganizationView(LoginRequiredMixin, DetailView):
    model = Organization
    template_name = 'organization/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailOrganizationView, self).get_context_data(**kwargs)
        context['products'] = ','.join([product.name for product in self.object.products.all()])
        ids = self.object.products.all().values_list('related_products__id', flat=True)
        context['related_products'] = Product.objects.filter(id__in=ids)
        print(context['related_products'])
        return context


@login_required
def add_report(request, pk):
    """
        a View for creating new report using a form
    """
    organization = get_object_or_404(Organization,
                                     id=pk)
    if request.method == 'POST':
        form = ReportForm(data=request.POST,
                          files=request.FILES)
        if form.is_valid():
            organization.followups.create(
                registrar=request.user,
                organization=organization,
                report=form.cleaned_data['report']
            )
            return redirect('organization:detail_organization', organization.id)
        else:
            return redirect('organization:list_organization')
    else:
        form = ReportForm()
        return render(request,
                      'organization/report_from.html',
                      {'form': form,
                       'organization': organization})
