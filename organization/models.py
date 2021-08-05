from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class Province(models.Model):
    """
    Class For Saving Provinces.
    """
    name = models.CharField(max_length=50)

    class Meta:
        """
        Meta Class Contains Ordering for order in database
        """
        ordering = ('-name',)

    def __str__(self):
        return self.name


class OrganizationProduct(models.Model):
    """
    Class for saving organizations products.
    """
    name = models.CharField(max_length=50)

    class Meta:
        """
            Meta Class Contains Ordering for order in database
        """
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Organization(models.Model):
    """
    Class for the defining organizations.
    """
    province = models.ForeignKey(Province,
                                 on_delete=models.PROTECT,
                                 related_name='organizations')
    name = models.CharField(max_length=50,
                            unique=True)
    phone = models.CharField(max_length=50,
                             validators=[RegexValidator(regex='^(\+98?)?{?(0?9[0-9]{9,9}}?)$'), ],
                             unique=True)
    workers_count = models.PositiveIntegerField(default=0)
    products = models.ManyToManyField(OrganizationProduct,
                                      related_name='organizations')


    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=50,
                                     validators=[RegexValidator(regex='^(\+98?)?{?(0?9[0-9]{9,9}}?)$'), ])
    contact_email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)
    registrar = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.PROTECT,
                                  related_name='registered_organization')

    def get_absolute_url(self):
        """
        Canonical Url for Organization Model
        :return: reverse of detail for organization
        """
        return reverse('organization:detail_organization', self.id)

    class Meta:
        """
            Meta Class Contains Ordering for order in database
        """
        ordering = ('-registration_date', '-name',)

    def __str__(self):
        return self.name