from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name ='accounts/logout.html'), name ='logout'),
    path('edit/', views.editProfile, name='editProfile'),
    path('change-password/', views.changePass, name='changePass'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
