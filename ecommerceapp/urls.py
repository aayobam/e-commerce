from django.urls import path
from .views import *


urlpatterns = [
    path('', project_test_views, name="home"),
    path('products/', products_view, name="products")
]
