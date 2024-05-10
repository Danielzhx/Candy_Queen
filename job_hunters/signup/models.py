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
        if not self.data['individual-phone_number'].isnumeric():
            self.add_error("phone_number", "Phone number must be numeric.")
            return False
        try:
            if datetime.strptime(self.data['individual-date_of_birth'], "%Y-%m-%d") > datetime.now():
                self.add_error("date_of_birth", "Date of birth must be in the past.")
                return False
        except ValueError:
            self.add_error("date_of_birth", "Invalid date of birth")
            return False
        
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
