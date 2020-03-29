from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import os


# Function to make right product image file path
def get_upload_path(instance, filename):
    return f"shop/img/product/{instance.url}/{filename}"

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, default='', blank=False)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat')
    sub_category = models.CharField(max_length=50, default='')
    price = models.PositiveIntegerField(blank=False)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    new_price = models.PositiveIntegerField(null=True,blank=True)
    pub_date = models.DateField()
    warranty = models.CharField(max_length=20, default='No')
    replacement = models.CharField(max_length=20, default='No')
    available = models.BooleanField(default=True)
    url = models.CharField(max_length=32, default=get_random_string(length=32))
    product_img1 = models.ImageField(upload_to=get_upload_path,default='shop/img/product/default.png',blank=False)
    product_img2 = models.ImageField(upload_to=get_upload_path,default='shop/img/product/default.png',blank=True)
    product_img3 = models.ImageField(upload_to=get_upload_path,default='shop/img/product/default.png',blank=True)
    product_img4 = models.ImageField(upload_to=get_upload_path,default='shop/img/product/default.png',blank=True)
    product_img5 = models.ImageField(upload_to=get_upload_path,default='shop/img/product/default.png',blank=True)
    product_img6 = models.ImageField(upload_to=get_upload_path,default='shop/img/product/default.png',blank=True)

    def __str__(self):
        return self.product_name

class Slider(models.Model):
    product = models.CharField(max_length=26)
    description = models.CharField(max_length=620)
    price = models.PositiveIntegerField(blank=False)
    img = models.ImageField(upload_to='shop/img/slider/', blank=False)

    def __str__(self):
        return self.product