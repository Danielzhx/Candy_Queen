from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from betterforms.multiform import MultiModelForm
from datetime import datetime


# Create your models here.
class Individual(models.Model):
    parent_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pic = models.ImageField('profile picture', upload_to='static/images/avatars/', null=True, blank=True)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField("Date of Birth")
    phone_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.parent_user}"


class IndividualForm(forms.ModelForm):
    class Meta:
        exclude = ('parent_user',)
        model = Individual
        fields = ['pic', 'address', 'date_of_birth', 'phone_number']

    parent_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def is_valid(self):
        valid = super(forms.ModelForm, self).is_valid()
        if not self.data['individual-address'][0].isnumeric():
            valid = False
        print(self.data['individual-date_of_birth'])
        try:
            if datetime.strptime(self.data['individual-date_of_birth'], "%Y-%m-%d") > datetime.now():
                self.add_error("Date of Birth", "Date of birth must be in the past.")
        except ValueError:
            self.add_error("Invalid date of birth")
        
        return valid

    def __init__(self, *args, **kwargs):
        super(IndividualForm, self).__init__(*args, **kwargs)


class SignupForm(MultiModelForm):
    form_classes = {
        'user': UserCreationForm,
        'individual': IndividualForm,
    }

    def save(self, commit=True):
        objects = super(SignupForm, self).save(commit=False)
        if commit:
            user = objects['user']
            user.save()
            individual = objects['individual']
            individual.parent_user = user
            individual.save()

        return objects
