from django.urls import path
from .views import *



urlpatterns = [
    path('orders/', orders_view, name="order-views"),
    path('success/', order_success, name="order-success")
]
