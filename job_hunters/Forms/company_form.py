from django.db import models
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from datetime import datetime

from companies.models import Company

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ('user',)
        fields = ['name', 'logo', 'cover_image', 'address', 'phone_number', 'contact_email', 'description']

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def is_valid(self):
        valid = super(ModelForm, self).is_valid()

        if not self.data['company-phone_number'].isnumeric():
            self.add_error("phone_number", "Phone number must be numeric.")
            return False
    
        address_list = self.data['company-address'].split()
        if len(address_list) < 2 or not address_list[0].isalpha() or not address_list[-1].isnumeric():
            self.add_error("address", "Invalid address")
            return False
        return valid