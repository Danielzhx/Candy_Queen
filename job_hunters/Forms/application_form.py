from django.forms import ModelForm, widgets
from jobs.models import Application
from django_countries.widgets import CountrySelectWidget

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exculde = ["id", "user", "job"]
        widgets = {
            "name": widgets.TextInput(attr={"placeholder":"Full name", "class":"form-control"}),
            "street_name": widgets.TextInput(attr={"placeholder":"Street name", "class":"form-control"}),
            "house_number": widgets.TextInput(attr={"placeholder":"House number", "class":"form-control"}),
            "city": widgets.TextInput(attr={"placeholder":"City", "class":"form-control"}),
            "postal": widgets.TextInput(attr={"placeholder":"Postal code", "class":"form-control"}),
            "country": CountrySelectWidget(),
            "cover_letter": widgets.FileInput(attrs={'label': 'Upload file'})
        }
