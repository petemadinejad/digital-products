from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel
from user.models import User
from utils.validators import sku_validator


class Package(BaseModel):
    title = models.CharField(_('title'), max_length=50)
    sku = models.CharField(_('stock keeping unit'), max_length=50, validators=[sku_validator])
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='packages/', blank=True)
    is_enabled = models.BooleanField(_('is enabled'), default=True)
    price = models.PositiveIntegerField(_('price'),default=0)
    duration = models.IntegerField(_('duration'), default=0)

    class Meta(BaseModel.Meta):
        db_table = 'package'
        verbose_name = _('package')
        verbose_name_plural = _('packages')


class Subscription(models.Model):
    user = models.ForeignKey(verbose_name=_('user'), to=User, on_delete=models.CASCADE, related_name='subscriptions')
    package = models.ForeignKey(verbose_name=_('package'), to=Package, on_delete=models.CASCADE)
    expire_time = models.DateField(_('expire time'), blank=True, null=True)
    is_enabled = models.BooleanField(_('is enabled'), default=True)

    class Meta(BaseModel.Meta):
        db_table = 'subscription'
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')
