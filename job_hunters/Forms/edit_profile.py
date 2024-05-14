from .individual_form import IndividualForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models
from betterforms.multiform import MultiModelForm

from .signup_form import ISignupForm, CSignupForm


class IEditForm(IndividualForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].required = False
        self.fields['address'].required = False
        self.fields['date_of_birth'].required = False
        self.fields['pic'].required = False
        

class IEditMultiForm(MultiModelForm):
    form_classes = {
            'user': UserChangeForm,
            'individual': IEditForm
        }

    def save(self, commit=True):
        objects = super(CSignupForm, self).save(commit=False)
        print(objects)