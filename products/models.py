from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    avatar=models.imageField(verbose_name=_('Avatar'), upload_to='category/', blank=True)
    is_enable = models.BooleanField(verbose_name=_('Is enable'), default=True)

    def __str__(self):
        return self.title


class File(BaseModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="files/")

    def __str__(self):
        return self.name
