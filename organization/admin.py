from django.contrib import admin
from .models import *


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    """
        Admin Class For Province Class Made By 2 Arguments.
        list_display, search_fields
    """
    list_display = ['name', ]
    search_fields = ['name', ]


@admin.register(OrganizationProduct)
class OrganizationProductAdmin(admin.ModelAdmin):
    """
        Admin Class For OrganizationProduct Class Made By 2 Arguments.
        list_display, search_fields
    """
    list_display = ['name', ]
    search_fields = ['name', ]


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """
        Admin Class For Product Class Made By 5 Arguments.
        list_display, list_filter, list_per_page, search_fields, date_hierarchy
    """
    list_display = ['province',
                    'name',
                    'phone',
                    'contact_name',
                    'contact_phone',
                    'contact_email', ]
    list_filter = ['registration_date', ]
    date_hierarchy = 'registration_date'
    search_fields = ['name',
                     'province',
                     'phone',
                     'contact_name',
                     'contact_phone',
                     'contact_email', ]


