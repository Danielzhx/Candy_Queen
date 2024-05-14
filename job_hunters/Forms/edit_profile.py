from .individual_form import IndividualForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm

class EditForm(MultiModelForm):
    pass
