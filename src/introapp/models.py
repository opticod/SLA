from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField(blank=False, null=False, unique=True)
	full_name = models.CharField(max_length=128, blank=False, null=False, unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	roll = models.CharField(max_length=128, blank=False, null=False)
	department = models.CharField(max_length=128, blank=False, null=False)
	semester = models.CharField(max_length=128, blank=False, null=False)
	
	def __unicode__(self): #Python 3.3 is __str__
		return self.email
		

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    roll = models.CharField(max_length=128, blank=False, null=False)
    department = models.CharField(max_length=128, blank=False, null=False)
    semester = models.IntegerField()