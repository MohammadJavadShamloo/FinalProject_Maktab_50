from django.conf import settings
from django.db import models

from inventory.models import Product
from organization.models import Organization


class QuoteItem(models.Model):
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


class Quote(models.Model):
    organization = models.ForeignKey(Organization,
                                     on_delete=models.PROTECT,
                                     related_name='quotes')
    registrar = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.PROTECT,
                                  related_name='quotes')
    registration_date = models.DateTimeField(auto_now_add=True)
    updating_date = models.DateTimeField(auto_now=True)
