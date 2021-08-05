from django.contrib import admin
from .models import *


@admin.register(EmailHistory)
class EmailHistoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'report', 'is_sent', ]
    list_filter = ['is_sent', ]
    search_fields = ['name', 'is_sent', ]
