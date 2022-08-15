from django.contrib import admin
from .models import Product, Category, File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["parent", "title", "is_enable", "created_at"]
    list_filter = ["is_enable", "parent"]
    search_fields = ["title"]


class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ["title", "file", "is_enable"]
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "is_enable", "created_at"]
    list_filter = ["is_enable"]
    filter_horizontal = ["categories"]
    search_fields = ["title"]
    inlines = [FileInlineAdmin]


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ["title", "is_enable",'product', "created_at"]
    list_filter = ["is_enable"]
    search_fields = ["title"]
