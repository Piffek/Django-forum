from django.db import models

from django.conf import settings
from django.utils.timezone import now
from subject.models import Subject

class Posts(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL)
    when = models.DateTimeField(default = now)
    text = models.TextField(null=True, blank=True)
    subj = models.ForeignKey(Subject)
    
    def __str__(self):
        return "{who} {when} {text} {subj_id}".format(who=self.who, when=self.when, 
                                                       text=self.text, subj_id=self.subj)
