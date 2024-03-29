from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>/<url>/', views.prodView, name='prodView'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
