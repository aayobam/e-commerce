from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.urls import reverse



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone_no = PhoneField(blank=True)
    profile_picture = models.ImageField(upload_to="media/images", default="default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "profiles"

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("userpage", kwargs={"pk": self.pk})
