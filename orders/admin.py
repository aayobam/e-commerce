from django.contrib import admin
from django.contrib.admin.decorators import action
from .models import *



@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity', 'delivery_status', 'created', 'updated')
    actions = ['pending', 'out_for_delivery', 'delivered']


    def pending(self, request, queryset):
        return queryset.update(delivery_status='Pending')

    def out_for_delivery(self, request, queryset):
        return queryset.update(delivery_status='Out for deliver')

    def delivered(self, request, queryset):
        return queryset.update(delivery_status='Delivered')


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'address', 'phone_no', 'city', 'state', 'country', 'zipcode', 'total_amount', 'payment_status', 'reference', 'created')
    search_fields = ("reference", "first_name", "last_name")
