from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

from .models import *


@admin.register(User)
class MyUserAdmin(BaseUserAdmin):
    fieldsets = ((None, {'fields': ('username', 'password')}),
                 (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number', 'email')}),
                 (
                     _('Permissions'),
                     {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
                 (_('Important dates'), {'fields': ['last_login']}))

    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2')}),)
    list_display = ('username', 'email', 'phone_number', 'is_staff')
    search_fields = ['username__exact']
    ordering = ('username',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset = queryset.filter(phone_number=search_term_as_int)
        return queryset, use_distinct


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('user', 'gender',)
    ordering = ('user',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    search_fields = ('device_type', 'device_os',)
    ordering = ('device_type',)


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)


admin.site.unregister(Group)
