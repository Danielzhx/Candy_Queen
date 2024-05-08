from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Individual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pic = models.ImageField(default='default', upload_to='profile_images')
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField("Date of Birth")
    phone_number = models.CharField(max_length=20)


class IndividualForm(forms.ModelForm):
    class Meta:
        exclude = ('user',)
        model = Individual
        fields = ['address', 'date_of_birth', 'phone_number']
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super(IndividualForm, self).__init__(*args, **kwargs)