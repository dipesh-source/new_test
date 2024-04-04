""" admin """

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'birthday', 'gender', 'premium', 'location', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'premium')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'birthday', 'gender', 'premium', 'location', 'is_staff', 'is_active')}),
        ('Permissions', {'fields': ('is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'birthday', 'gender', 'premium', 'location', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, UserAdmin)