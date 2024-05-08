from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import IndividualForm

# Create your views here.
def signup_type(request):
    """First step in new account registration.
    
    Allows the user to choose whether they want to create a 
    company or individual account.
    """
    template_name = "signup/index.html"
    return render(request, template_name, None)


def reg_individual(request):
    """Second step in new account registration for individuals.
    
    Takes in only the required info to create a new user. Project specific 
    info is handled in the next step.
    """
    template_name = "signup/reg_individual.html"

    if request.method == 'POST':
        print(f"POST request received: {request.POST['username']}, {request.POST['password1']}, {request.POST['password2']}")
        userform = UserCreationForm(data={'username':request.POST['username'], 
                                          'password1':request.POST['password1'], 
                                          'password2':request.POST['password2']})
        indform = IndividualForm(data=request.POST)
        user_valid = userform.is_valid()
        print(userform.errors)
        print(f"user_valid: {user_valid}")
        ind_valid = indform.is_valid()
        print(f"ind_valid: {ind_valid}")
        if user_valid and ind_valid:
            user = userform.save(commit=True)
            indform.user_id = user
            print(indform.user_id)
            #indform.save(commit=True)

        return render(request, template_name, {'userError':userform.errors, 'indError':indform.errors})
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
