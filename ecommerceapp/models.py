from django.core.validators import *
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinValueValidator



class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_list", kwargs={"slug": self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200)
    model = models.CharField(max_length=250)
    product_image = models.ImageField(default="default.png", upload_to="product_image/")
    product_description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(1)])
    in_stock = models.IntegerField(default=0, blank=True, null=True, validators=[MinValueValidator(1)])
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ("name",)
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})


