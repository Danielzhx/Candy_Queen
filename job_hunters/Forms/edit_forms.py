from typing import Any, Mapping
from django.core.files.base import File
from django.forms.utils import ErrorList
from .individual_form import IndividualForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Form
from django.db import models
from betterforms.multiform import MultiModelForm

from .signup_form import ISignupForm, CSignupForm
from .company_form import CompanyForm

class UserEditForm2(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            )


class IndEditForm(IndividualForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].required = False
       
class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['date_joined'].required = False

"""class IEditMultiForm(MultiModelForm):
    form_classes = {
            'user': UserChangeForm,
            'individual': IEditForm
        }

    def save(self, commit=True):
        objects = super(ISignupForm, self).save(commit=False)
        if commit:
            user = objects['user']
            user.save()
            individual = objects['individual']
            individual.parent_user = user
            individual.save()

        return objects"""

class CEditForm(Form):
    fields = ['user-username', 
              'company-name', 
              'company-logo', 
              'company-cover_image', 
              'company-address', 
              'company-phone_number', 
              'contact_email',
              'company-description']
