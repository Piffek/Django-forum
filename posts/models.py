from django.db import models

from django.conf import settings
from django.utils.timezone import now

class Posts(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL)
    when = models.DateTimeField(default = now)
    text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return "{who} {when} {text}".format(who=self.who, when=self.when, 
                                                       text=self.text)
