from django.db import models


class Gateway(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='gateways/', blank=True)
    is_enabled = models.BooleanField(_('is enable'), default=True)


class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATUS_REFUNDED = 31
    STATUS_CHOICES = (
        (STATUS_VOID, _('void')),
        (STATUS_PAID, _('paid')),
        (STATUS_ERROR, _('error')),
        (STATUS_CANCELED, _('canceled')),
        (STATUS_REFUNDED, _('refunded')),)
    STATUS_TRANSLATIONS = {
        STATUS_VOID: _('Payment could not be processed'),
        STATUS_PAID: _('Payment was processed successfully'),
        STATUS_ERROR: _('Payment has failed'),
        STATUS_CANCELED: _('Payment canceled by user'),
        STATUS_REFUNDED: _('This Payment has been refunded'),
    }
    user = models.ForeignKey(verbose_name=_('user'), to=User, on_delete=models.CASCADE, related_name='payments')
    package = models.ForeignKey(verbose_name=_('package'), to=Package, on_delete=models.CASCADE)
    gateway = models.ForeignKey(verbose_name=_('gateway'), to=Gateway, on_delete=models.CASCADE)
    price = models.DecimalField(_('price'), )
    status = models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_VOID)
    device_uuid = models.CharField(_('device uuid'), max_length=50, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=50, blank=True)
    discount = models.DecimalField(_('discount'), blank=True, null=True)

    class Meta:
        db_table = 'payment'
        verbose_name = _('payment')
        verbose_name_plural = _('payments')
