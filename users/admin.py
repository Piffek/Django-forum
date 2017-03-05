from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from django.utils.translation import ugettext_lazy as _

class ProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'),  {'fields': ('is_active', 'is_staff', 'is_superuser','user_permissions', 'groups')}),
        (_('Important dates'),  {'fields': ('last_login', 'date_joined')}),
        (_('Additional info'), {'fields': ('phone', 'avatar')})
        )

admin.site.register(Profile, ProfileAdmin)
