from django.urls import path
from .views import *


urlpatterns = [
    path('cart/', cart_summary, name="cart_summary"),
    path('add/', add_to_cart, name="add_to_cart"),
    path('delete-from-cart/', delete_from_cart, name='delete_from_cart'),
    path('update-cart/', update_cart, name='update_cart'),
]
