from django.contrib import admin
from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['who', 'when', 'subj', 'body']

admin.site.register(Subject, SubjectAdmin)
