from django.contrib import admin
from .models import *


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("name", 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('category', 'brand_name', 'name', 'slug', 'model', 'product_image',
                    'product_description', 'price', 'in_stock', 'available','created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'brand_name', 'category__name', )
