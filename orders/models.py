from django.db import models
from phone_field import PhoneField
from ecommerceapp.models import Product
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator



class OrderHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = CountryField()
    phone_no = PhoneField(blank=True, help_text="contact phone number")
    total_amount = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(1)])
    payment_status = models.BooleanField(default=False)
    order_reference = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.product.name


class OrderedItem(models.Model):
    Delivert_Status = (
        (1, "Pending"),
        (2, "Out for Delivery"),
        (3, "Delivered"),
    )
    order_history = models.ForeignKey(OrderHistory, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ordered_items")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    delivery_status = models.CharField(choices=Delivert_Status, default="Pending", max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.product
    