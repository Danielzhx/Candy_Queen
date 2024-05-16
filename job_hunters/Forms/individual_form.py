from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from datetime import datetime

from signup.models import Individual

class IndividualForm(forms.ModelForm):
    class Meta:
        exclude = ('parent_user',)
        model = Individual
        fields = ['pic', 'address', 'date_of_birth', 'phone_number']

    parent_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def is_valid(self):
        valid = super(forms.ModelForm, self).is_valid()
        try:
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
            
            address_list = self.data['individual-address'].split()
            if len(address_list) < 2 or not address_list[0].isalpha() or not address_list[-1].isnumeric():
                self.add_error("address", "Invalid address")
                return False
            return valid
        except MultiValueDictKeyError:
            if not self.data['phone_number'].isnumeric():
                self.add_error("phone_number", "Phone number must be numeric.")
                return False
            try:
                if datetime.strptime(self.data['date_of_birth'], "%Y-%m-%d") > datetime.now():
                    self.add_error("date_of_birth", "Date of birth must be in the past.")
                    return False
            except ValueError:
                self.add_error("date_of_birth", "Invalid date of birth")
                return False
            
            address_list = self.data['address'].split()
            if len(address_list) < 2 or not address_list[0].isalpha() or not address_list[-1].isnumeric():
                self.add_error("address", "Invalid address")
                return False
            return valid


    def __init__(self, *args, **kwargs):
        super(IndividualForm, self).__init__(*args, **kwargs)
        self.fields['pic'].required = False