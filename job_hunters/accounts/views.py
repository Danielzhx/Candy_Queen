from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views, authenticate, login, logout
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from . import models


# Create your views here.
class LogInView(views.LoginView):
    """View for login page. Uses built in LoginView.
    """
    template_name = "accounts/login.html"
    next_page = "jobs:index"

    def get_user(self):
        return self.request.user


def log_out(request):
    """Logs user out and returns them to job listing page.
    """
    logout(request)
    return redirect("jobs:index")


def signup_type(request):
    """First step in new account registration.
    
    Allows the user to choose whether they want to create a 
    company or individual account.
    """
    template_name = "accounts/signup.html"
    return render(request, template_name, None)


def register(request):
    """Second step in new account registration for individuals.
    
    Takes in only the required info to create a new user. Project specific 
    info is handled in the next step.
    """
    template_name = "accounts/signup_user.html"
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    return render(request, template_name, {'form': UserCreationForm({})})


def register_profile(request):
    """Third step in new account registration for individuals.
    
    Gets project specific info which is added to both the user object and 
    its associated individual object.
    """
    template_name = "accounts/signup_profile.html"
    if request.method == 'POST':
        profile_form = models.IndividualForm(data=request.POST, user=request.user)


@login_required
def user_profile(request):
    """Allows a user to see and manage their profile."""
    return render(request, 'accounts/profile.html', "context")
