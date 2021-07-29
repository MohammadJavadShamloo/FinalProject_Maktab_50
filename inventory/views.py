from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from .models import *


class CreateProductView(LoginRequiredMixin, CreateView):
    """
      Class Based View For Creating Products
    """
    model = Product
    template_name = 'inventory/create.html'
    fields = ['name',
              'price',
              'tax',
              'pdf_file',
              'pic_file',
              'technical_report',
              'related_products', ]
    success_url = reverse_lazy('inventory:list_product')


class UpdateProductView(LoginRequiredMixin, UpdateView):
    """
          Class Based View For Updating Products
    """
    model = Product
    template_name = 'inventory/update.html'
    fields = ['name',
              'price',
              'tax',
              'pdf_file',
              'pic_file',
              'technical_report',
              'related_products', ]
    success_url = reverse_lazy('inventory:list_product')


class ListProductView(LoginRequiredMixin, ListView):
    """
          Class Based View For Listing Products
    """
    model = Product
    template_name = 'inventory/list.html'
    paginate_by = 15


class DetailProductView(LoginRequiredMixin, DetailView):
    """
          Class Based View For Showing Details of Products
    """
    model = Product
    template_name = 'inventory/detail.html'
