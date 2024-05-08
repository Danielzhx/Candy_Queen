from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Individual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(default='default', upload_to='profile_images')
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField("Date of Birth")
    phone_number = models.CharField(max_length=20)


class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['pic', 'address', 'date_of_birth', 'phone_number']
    user = models.OneToOneField(User, on_delete=models.CASCADE)