from django.db import models
from django.utils.translation import ugettext_lazy as _
from base.models import BaseModel


class Product(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    avatar = models.ImageField(verbose_name=_('Avatar'), upload_to='product/', blank=True)
    is_enable = models.BooleanField(verbose_name=_('Is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('Categories'), blank=True)

    def __str__(self):
        return self.title


class Category(BaseModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    avatar = models.ImageField(verbose_name=_('Avatar'), upload_to='category/', blank=True)
    is_enable = models.BooleanField(verbose_name=_('Is enable'), default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['title']


class File(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'), related_name="files")
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    file = models.FileField(verbose_name=_('File'), upload_to='file/%Y/%m/%d/')
    is_enable = models.BooleanField(verbose_name=_('Is enable'), default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'file'
        verbose_name = _('File')
        verbose_name_plural = _('Files')
        ordering = ['title']
