from django.contrib import admin
from .models import *


@admin.register(QuoteItem)
class QuoteItemAdmin(admin.ModelAdmin):
    list_display = ['product',
                    'count_of_product',
                    'price_before_tax',
                    'price_after_tax',
                    'off_percent', ]
    list_filter = ['product',
                   'count_of_product', ]
    search_fields = ['product', 'off_percent', ]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['organization',
                    'registrar',
                    'registration_date',
                    'updating_date', ]
    list_filter = ['organization',
                   'registrar', ]
    search_fields = ['organization',
                     'registrar', ]
