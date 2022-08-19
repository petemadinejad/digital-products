from django.contrib import admin

from .models import *


@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
