from django.db import models
from django.contrib.auth.models import User
from shop.models import Address
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.PositiveSmallIntegerField(max_length=10)
	dob = models.DateField(null=True, blank=True)
	gender = models.CharField(default='', max_length=50, blank=True)
	default_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='default_address', blank=True, default=1)

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)