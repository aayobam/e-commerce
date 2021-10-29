from django.contrib import admin
from .models import *



@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity', 'delivery_status', 'created', 'updated')


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('user','first_name', 'last_name', 'email', 'address', 'phone_no', 'zipcode', 'city', 'state', 'country', 'total_amount', 'payment_status', 'reference', 'created')
    search_fields = ("reference", "first_name", "last_name")