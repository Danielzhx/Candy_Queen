from django.forms import ModelForm, widgets
from jobs.models import Job
from django import forms

class JobCreationForm(ModelForm):
    category = forms.CharField()
    class Meta:
        model = Job
        exclude = ['company','category']
