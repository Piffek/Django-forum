from django.db import models
from posts.models import Posts
from django.conf import settings
from django.utils.timezone import now

class Subject(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL)
    when = models.DateTimeField(default = now)
    subj = models.CharField(max_length=50)
    body = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return "{who} {when} {subj} {body}".format(who=self.who, when=self.when, 
                                                       subj=self.subj, body=self.body)
