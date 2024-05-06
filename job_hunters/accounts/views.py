from django.shortcuts import render
from django.contrib.auth import views, authenticate, login
from django.views import generic

# Create your views here.
class LogInView(views.LoginView):
    template_name = "accounts/login.html"
    next_page = "jobs/"

    def get_user():
        return None
"""
class LogInView(views.LoginView):
    pass"""

class SignUpView(generic.CreateView):
    template_name = "accounts/signup.html"
    queryset = None