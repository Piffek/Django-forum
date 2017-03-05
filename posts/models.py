from django.db import models

from django.conf import settings
from django.utils.timezone import now

class Posts(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL)
    when = models.DateTimeField(default.now)
    text = models.CharField(null=True, blank=True)
