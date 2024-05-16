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


class IndEditForm(IndividualForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].required = False
       
class CEditForm(Form):
    fields = ['user-username', 
              'company-name', 
              'company-logo', 
              'company-cover_image', 
              'company-address', 
              'company-phone_number', 
              'contact_email',
              'company-description']
