from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
from Forms.individual_form import IndividualForm
from Forms.company_form import CompanyForm

class ISignupForm(MultiModelForm):
    form_classes = {
        'user': UserCreationForm,
        'individual': IndividualForm
    }

    def save(self, commit=True):
        objects = super(ISignupForm, self).save(commit=False)
        if commit:
            user = objects['user']
            user.save()
            individual = objects['individual']
            individual.parent_user = user
            individual.save()

        return objects


class CSignupForm(MultiModelForm):
    form_classes = {
        'user': UserCreationForm,
        'company': CompanyForm,
    }

    def save(self, commit=True):
        objects = super(CSignupForm, self).save(commit=False)
        if commit:
            user = objects['user']
            user.save()
            company = objects['company']
            company.user = user
            company.save()

        return objects
