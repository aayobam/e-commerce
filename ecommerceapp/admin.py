from django.contrib import admin
from .models import *


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("name", 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('category', 'brand_name', 'name', 'slug', 'model', 'product_image',
                    'short_description', 'description', 'price', 'in_stock', 'available', 'added_by', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_amount',
                    'created_at', 'updated_at')


@admin.register(OrderHistory)
class AdminOrder(admin.ModelAdmin):
    list_display = ('product', 'price', 'quantity', 'total_amount', 'payment_status','paystack_order_id', 'first_name',
                    'last_name', 'email', 'address', 'postal_code', 'city', 'delivery_status', 'phone_no')
