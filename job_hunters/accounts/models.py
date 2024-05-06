from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Individual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(default='default', upload_to='profile_images')
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField("Date of Birth")
    phone_number = models.CharField(max_length=20)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    pic = models.ImageField(default='default', upload_to='profile_images')
    address = models.CharField(max_length=200)