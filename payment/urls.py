from django.urls import path
from .views import *


urlpatterns = [
    path('billing/', billing_view, name="billing-view"),
    path('billing/card', card_form_view, name="card-modal")
]
