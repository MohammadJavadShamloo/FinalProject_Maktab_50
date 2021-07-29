from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin Class For Product Class Made By 4 Arguments.
    list_display, list_filter, list_per_page, search_fields
    """
    list_display = ['name',
                    'price',
                    'tax',
                    'technical_report', ]
    list_filter = ['name',
                   'price',
                   'tax', ]
    list_per_page = 3
    search_fields = ['name',
                     'price',
                     'tax', ]
