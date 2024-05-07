from django.forms import ModelForm,widgets
from django import forms
from ..jobs.models import JobType,Job,Category,Company

JOB_CATEGORIES = Category.object.all()
COMPANIES = Company.object.all()
JOB_TYPES = JobType.objecj.all()

class FilterForm(ModelForm):
    job_type = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,choices = JOB_TYPES)
    class Meta:
        model = Job
        exclude = ['description','location','id','due_date','start_date']
        widgets = {
            'title':widgets.TextInput(attrs={'placeholder':"search title"}),
            'category':widgets.Select(),
            'company':widgets.Select()
        }

