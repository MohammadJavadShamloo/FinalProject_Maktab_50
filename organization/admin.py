from django.contrib import admin
from .models import *


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]


@admin.register(OrganizationProduct)
class OrganizationProductAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
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


@admin.register(FollowUp)
class FollowUpAdmin(admin.ModelAdmin):
    list_display = ['registrar',
                    'organization',
                    'date',
                    'report', ]
