from django.contrib import admin
from .models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ['who', 'when', 'text', 'subj_id']
    
admin.site.register(Posts, PostsAdmin)
