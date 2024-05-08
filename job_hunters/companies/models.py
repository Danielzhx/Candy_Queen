
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    logo = models.ImageField(default='default', upload_to='logo_images')
    cover_image = models.ImageField(default='default', upload_to='cover_images')
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    contact_email = models.CharField(max_length=255)
    email = models.CharField(max_length=255) #The difference between contact_email and email is that contact email is for other users to contact the company, while email is the company's own email that they sign up with
    password = models.CharField(max_length=255)

