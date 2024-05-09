from django.forms import ModelForm, widgets
from jobs.models import Application
from django_countries.widgets import CountrySelectWidget
from django_countries import countries

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ["id", "user", "job"]
        widgets = {
            "name": widgets.TextInput(attrs={"placeholder":"Full name", "class":"form-control"}),
            "street_name": widgets.TextInput(attrs={"placeholder":"Street name", "class":"form-control"}),
            "house_number": widgets.TextInput(attrs={"placeholder":"House number", "class":"form-control"}),
            "city": widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}),
            "postal": widgets.TextInput(attrs={"placeholder":"Postal code", "class":"form-control"}),
            "country": CountrySelectWidget(),
            "cover_letter": widgets.FileInput(attrs={'label': 'Upload file'})
        }
