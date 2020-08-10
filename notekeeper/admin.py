from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ('fid',)
    list_display = ('id', 'fid', 'email', 'created_at', 'is_active', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('fid',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('fid', 'email', 'password1', 'password2')
        })
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Note)
