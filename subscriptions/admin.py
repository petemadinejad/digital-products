from django.contrib import admin

from .models import *


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass
