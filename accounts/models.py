from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=10)
	dob = models.DateField(null=True, blank=True)
	gender = models.CharField(max_length=50, choices=[('',''), ('Female','Female'), ('male','Male')],)
	about = models.TextField(default='')
	wishlist = models.ManyToManyField(Product, related_name='whishlist')
	user_img = models.ImageField(upload_to='user/img', blank=True, default='user/img/default.png')

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)