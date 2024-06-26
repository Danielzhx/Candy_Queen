from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    logo = models.ImageField(default='images/logo_images/default_logo.png', upload_to='images/logo_images/')
    cover_image = models.ImageField(default='images/cover_images/default_cover.jpg', upload_to='images/cover_images/')
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    contact_email = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    email = models.CharField(max_length=255)

    # The difference between contact_email and email is that contact email is for other users to contact the company,
    # while email is the company's own email that they sign up with

    def __str__(self) -> str:
        return self.name
