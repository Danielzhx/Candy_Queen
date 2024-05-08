from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import forms as authforms
from django import forms


# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    pic = models.ImageField(default='default', upload_to='profile_images')
    address = models.CharField(max_length=200)