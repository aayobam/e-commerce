from django.contrib import admin
from .models import OrderedItem, OrderHistory



@admin.register(OrderedItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ('order_history', 'product', 'price', 'quantity', 'delivery_status', 'created', 'updated')


@admin.register(OrderHistory)
class AdminOrderHistory(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'address', 'phone_no', 'postal_code', 'city', 'state', 'country', 'total_amount', 'payment_status', 'order_reference', 'created')
