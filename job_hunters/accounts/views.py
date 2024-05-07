from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import views, authenticate, login, logout
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Individual, Company

# Create your views here.
class LogInView(views.LoginView):
    template_name = "accounts/login.html"
    next_page = "jobs:index"

    def get_user():
        return None
    
def log_out(request):
    logout(request)
    return redirect("jobs:index")
    
def signup_type(request):
    template_name = "accounts/signup_type.html"
    return render(request, template_name, None)

class SignUpView(generic.CreateView):
    template_name = "accounts/signup.html"
    model = User
    fields = ["first_name","last_name","email","password"]

def new_user(request):
    if request.POST['password'] != request.POST['repeat_password']:
        return redirect("accounts:signup")
    
    new = User.objects.create_user(
        username = request.POST['username'],
        email = request.POST['email'],
        password = request.POST['password'],
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name']
        )
    ind = Individual.objects.create(
        user = new,
        pic = request.POST['profile_pic'],
        address = request.POST['address'],
        date_of_birth = request.POST['date_of_birth'],
        phone_number = request.POST['phone']
    )
    new.save()
    ind.save()

    return redirect("jobs:index")

@login_required
def user_profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'accounts/profile.html', context)
