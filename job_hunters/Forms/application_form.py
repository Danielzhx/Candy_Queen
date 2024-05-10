from django.forms import ModelForm, widgets
from jobs.models import Application, Experiences, References
from django_countries.widgets import CountrySelectWidget
from django_countries import countries

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ["id", "user", "job"]
        widgets = {
            "name": widgets.TextInput(attrs={"placeholder":"Full name", "class":"form-control", "id":"name_field"}),
            "street_name": widgets.TextInput(attrs={"placeholder":"Street name", "class":"form-control"}),
            "house_number": widgets.TextInput(attrs={"placeholder":"House number", "class":"form-control"}),
            "city": widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}),
            "postal": widgets.TextInput(attrs={"placeholder":"Postal code", "class":"form-control"}),
            "country": CountrySelectWidget(attrs={"class":"form-control w-75", "style":"display:inline"},
                                           layout='{widget}<img class="country-select-flag" id="{flag_id}" style="margin-left: 0.5rem" src="{country.flag}" width=25>'
),
            "cover_letter": widgets.Textarea(attrs={"class":"form-control w-100", "placeholder":"Cover letter"})
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experiences
        exclude = ["id", "application"]
        widgets = {
            "workplace": widgets.TextInput(attrs={"placeholder":"Workplace", "class":"form-control"}),
            "role": widgets.TextInput(attrs={"placeholder":"Role", "class":"form-control"}),
            "start_date": widgets.TextInput(attrs={"placeholder":"Start date", "class":"form-control"}),
            "end_date": widgets.TextInput(attrs={"placeholder":"End date", "class":"form-control"}),
        }

class ReferencesForm(ModelForm):
    model = References
    exclude = ["id", "application"]
    widgets = {
        "name": widgets.TextInput(attrs={"placeholder":"Full name", "class":"form-control"}),
        "email": widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}),
        "phone_number": widgets.TextInput(attrs={"placeholder":"Phone number", "class":"form-control"}),
        "contact_bool": widgets.CheckboxInput(attrs={"label":"Are we allowed to contact the reference?", "class":"form-control"})
    }
