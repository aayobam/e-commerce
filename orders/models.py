import random
from django.db import models
from phone_field import PhoneField
from ecommerceapp.models import Product
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator





def random_numbers():
    return random.randint(1111111111, 2147483647)


class Order(models.Model):
    
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    address = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = CountryField()
    phone_no = PhoneField(blank=True, help_text="contact phone number")
    total_amount = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(1)])
    payment_status = models.BooleanField(default=False)
    reference = models.CharField(max_length=250, default=random_numbers)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    Delivert_Status = (
        (1, "Pending"),
        (2, "Out for Delivery"),
        (3, "Delivered"),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    delivery_status = models.CharField(choices=Delivert_Status, default="Pending", max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.delivery_status
    