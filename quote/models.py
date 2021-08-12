from django.conf import settings
from django.db import models
from django.urls import reverse

from inventory.models import Product
from organization.models import Organization


class QuoteItem(models.Model):
    """
    Model For Quote Items That Has Parent Named Quote
    """
    quote = models.ForeignKey('Quote',
                              on_delete=models.PROTECT,
                              related_name='items')
    product = models.ForeignKey(Product,
                                on_delete=models.PROTECT,
                                related_name='quote_items')
    count_of_product = models.PositiveIntegerField(default=1)
    price_before_tax = models.DecimalField(max_digits=10,
                                           decimal_places=2)
    price_after_tax = models.DecimalField(max_digits=10,
                                          decimal_places=2)
    off_percent = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['price_after_tax', ]

    def __str__(self):
        return self.product.name


class Quote(models.Model):
    """
    Model Quote For Saving Quote For Every Organization.
    """
    organization = models.ForeignKey(Organization,
                                     on_delete=models.PROTECT,
                                     related_name='quotes')
    registrar = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.PROTECT,
                                  related_name='quotes')
    registration_date = models.DateTimeField(auto_now_add=True)
    updating_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-registration_date', ]

    def __str__(self):
        return f'Quote Number {self.id}'

    def get_absolute_url(self):
        return reverse('quote:quote_detail', self.id)
