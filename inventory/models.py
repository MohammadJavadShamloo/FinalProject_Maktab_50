from django.db import models
from django.urls import reverse

from .validators import *
from organization.models import OrganizationProduct


class Product(models.Model):
    """
    Product Model That Has 7 Fields and a Meta Class For Configuration.
    """
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    tax = models.BooleanField(default=True)
    pdf_file = models.FileField(upload_to='files/pdf_files/%Y/%m/%d',
                                validators=[validate_pdf, ])
    pic_file = models.FileField(upload_to='files/pic_files/%Y/%m/%d',
                                validators=[validate_pic, ])
    technical_report = models.TextField()
    related_products = models.ManyToManyField(OrganizationProduct,
                                              related_name='related_products')

    class Meta:
        """
        Meta Class Contains ordering for order in database
        """
        ordering = ('-price', '-name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Canonical Url for access the core Class
        """
        return reverse('inventory:detail_product', self.id)
