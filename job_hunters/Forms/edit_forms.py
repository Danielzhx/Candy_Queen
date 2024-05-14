from .individual_form import IndividualForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models
from betterforms.multiform import MultiModelForm

from .signup_form import ISignupForm, CSignupForm

class IEditForm(MultiModelForm):
    form_classes = {
            'user': UserChangeForm,
            'individual': IndividualForm
        }

    def save(self, commit=True):
        objects = super(ISignupForm, self).save(commit=False)
        if commit:
            user = objects['user']
            user.save()
            individual = objects['individual']
            individual.parent_user = user
            individual.save()

        return objects
