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

def view_applications(request):
    """Allows a user to see and manage their applications."""
    return render(request, template_name='applications/index.html')

@login_required
def user_profile(request):
    """Allows a user to see and manage their profile."""
    return render(request, 'accounts/profile.html', "context"


