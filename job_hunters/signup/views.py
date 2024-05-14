from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Forms.individual_form import IndividualForm
from Forms.signup_form import ISignupForm
from Forms.company_form import CompanyForm
from Forms.signup_form import CSignupForm
from companies.models import Company


# Create your views here.
def signup_type(request):
    """First step in new account registration.
    
    Allows the user to choose whether they want to create a 
    company or individual account.
    """
    if request.user.is_authenticated:
        return redirect("jobs:index")
    
    template_name = "signup/index.html"
    return render(request, template_name, None)


def reg_individual(request):
    """Second step in new account registration for individuals.
    
    Takes in the required info to create a new user.
    """
    if request.user.is_authenticated:
        return redirect("jobs:index")
    
    template_name = "signup/reg_individual.html"
    if request.method == 'POST':
        signup = ISignupForm(request.POST, request.FILES)
        if signup.is_valid():
            signup.save()
            return redirect("jobs:index")
        else:
            return render(request, template_name, {'errors': signup.errors})
    else:
        return render(request, template_name, {})

def reg_company(request):
    """Second step in new account registration for companies.
    
    Takes in the required info to create a new company account.
    """
    if request.user.is_authenticated:
        return redirect("jobs:index")
    
    template_name = "signup/reg_company.html"
    if request.method == 'POST':
        signup = CSignupForm(request.POST, request.FILES)
        if signup.is_valid():
            signup.save()
            return redirect("jobs:index")
        else:
            return render(request, template_name, {'errors': signup.errors})
    else:
        return render(request, template_name, {})

def register_profile(request):
    """Third step in new account registration for individuals.
    
    Gets project specific info which is added to both the user object and 
    its associated individual object.
    """
    template_name = "signup/register_profile.html"
    if request.method == 'POST':
        profile_form = IndividualForm(data=request.POST, user=request.user)
