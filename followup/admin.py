from django.contrib import admin

from followup.models import FollowUp


@admin.register(FollowUp)
class FollowUpAdmin(admin.ModelAdmin):
    """
        Admin Class For Product Class Made By 1 Arguments.
        list_display
    """
    list_display = ['registrar',
                    'organization',
                    'date',
                    'report', ]
