from django.conf import settings
from django.db import models

from organization.models import Organization


class FollowUp(models.Model):
    """
    CLass for followups and reports.
    """
    registrar = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.PROTECT,
                                  related_name='followups')
    organization = models.ForeignKey(Organization,
                                     on_delete=models.PROTECT,
                                     related_name='followups')
    date = models.DateTimeField(auto_now_add=True)
    report = models.TextField()

    class Meta:
        """
            Meta Class Contains Ordering for order in database
        """
        ordering = ('date',)

    def __str__(self):
        return self.report