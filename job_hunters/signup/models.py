from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from betterforms.multiform import MultiModelForm


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
