from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from phone_field import PhoneField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone_no = PhoneField(blank=True, help_text="contact phone number")
    profile_picture = models.ImageField(default="default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
