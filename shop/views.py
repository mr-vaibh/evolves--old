from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelformset_factory
from .models import Product, Slider

# Create your views here.


def index(request):
    slides = Slider.objects.all()

    context = {'slides': slides}
    return render(request, 'shop/index.html', context)


def prodView(request, id, url):
    return render(request, 'shop/product.html')
