from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from phone_field import PhoneField
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager




# class CustomAccountManager(BaseUserManager):

#     def create_superuser(self, username, email, password, **other_fields):
#         other_fields.setdefault('is_active', True)
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)

#         if other_fields.get("is_staff") is not True:
#             raise ValueError("super user must be assigned is_staff=True")

#         if other_fields.get("is_superuser") is not True:
#             raise ValueError("super user must be assigned is_superuser=True")
#         return self.create_superuser(username, email, password, **other_fields)
    
#     def create_user(self, username, email, password, **other_fields):
#         if not email:
#             raise ValueError(_("You must provide an email address"))
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user



# class UserBase(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     username = models.CharField(_('username'), unique=True, max_length=50)
#     first_name = models.CharField(max_length=150, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     date_of_birth = models.DateField()
#     address1 = models.CharField(max_length=250)
#     address2 = models.CharField(max_length=250)
#     zipcode = models.CharField(max_length=10)
#     city = models.CharField(max_length=100)
#     country = CountryField()
#     state = models.CharField(max_length=100)
#     phone_no = PhoneField(blank=True)
#     profile_picture = models.ImageField(upload_to="media/images", default="default.jpg")
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     objects = CustomAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username',]

#     class Meta:
#         verbose_name = "account"
#         verbose_name_plural = "accounts"

#     def __str__(self) -> str:
#         return self.username


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    #zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    #country = CountryField()
    phone_no = PhoneField(help_text="your phone number")
    profile_image = models.ImageField(upload_to="media/images", default="default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy("accounts:userpage-profile", kwargs={"pk": self.pk})
