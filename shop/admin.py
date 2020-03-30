from django.contrib import admin
from .models import Category, Product, Slider, Wishlist, Country, Address

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Slider)
admin.site.register(Wishlist)
admin.site.register(Country)
admin.site.register(Address)