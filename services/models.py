from django.conf import settings
from django.db import models


class EmailHistory(models.Model):
    name = models.CharField(max_length=200)
    report = models.TextField()
    is_sent = models.BooleanField(default=False)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.PROTECT,
                               related_name='emails_sent',
                               blank=True,
                               null=True)
    send_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-send_date', ]

    def __str__(self):
        return self.name