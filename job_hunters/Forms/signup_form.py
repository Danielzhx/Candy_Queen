from django.forms import ModelForm, widgets
from django.forms import Form, formset_factory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from signup.models import IndividualForm
from jobs.models import JobType,Job


JOB_TYPES = JobType.objects.all()
class SignupForm(Form):
    class Meta:
        model = 


    def __init__(self, *args, **kwargs):
        userform = UserCreationForm(*args, **kwargs)
        indivform = IndividualForm(data=args)        

        for field in self.Meta.widgets:
            self.fields[field].required = False

    job_type = forms.MultipleChoiceField(required=False,widget = forms.CheckboxSelectMultiple,choices = [(str(type.id),str(type)) for type in JOB_TYPES])
    order_by = forms.ChoiceField(required=False,choices = ORDERS )
    class Meta:
        model = Job
        exclude = ['description','location','id','due_date','start_date','job_type']
        widgets = {
            'title':widgets.TextInput(attrs={'placeholder':"search title", "class":"form-control"}),
            'category':widgets.Select(attrs={ "class":"form-select" }),
            'company':widgets.Select(attrs={ "class":"form-select" })
        }

