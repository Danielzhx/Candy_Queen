from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import forms as authforms
from django import forms

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

class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['pic', 'address', 'date_of_birth', 'phone_number']
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CustomUserForm(authforms.UserCreationForm):
    class Meta:
        model=User
        fields = ('username', 'password1', 'password2')
    
    """username = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                  'type': 'email',
                                  'placeholder': 'Email address',
                                  'required': 'true'
                                  }))
    password1 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                      'required': 'true',
                                      'placeholder': 'Password'
    }))
    password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                      'required': 'true',
                                      'placeholder': 'Repeat Password'
    }))"""
