from django.forms import ModelForm, widgets
from jobs.models import Job

class JobCreationForm(ModelForm):
    class Meta:
        model = Job
        exclude = ['company']
        widgets = {
            "category": widgets.TextInput()
        }
