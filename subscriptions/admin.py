from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass
