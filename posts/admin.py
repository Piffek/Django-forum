from django.contrib import admin
from .models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ['who', 'when', 'text']
    
admin.site.register(Posts, PostsAdmin)
