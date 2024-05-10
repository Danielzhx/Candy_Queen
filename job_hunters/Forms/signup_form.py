from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
from Forms.individual_form import IndividualForm

class SignupForm(MultiModelForm):
    form_classes = {
        'user': UserCreationForm,
        'individual': IndividualForm,
    }

    def save(self, commit=True):
        objects = super(SignupForm, self).save(commit=False)
        if commit:
            user = objects['user']
            user.save()
            individual = objects['individual']
            individual.parent_user = user
            individual.save()

        return objects
