from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import views, authenticate, login
from django.views import generic
from django.contrib.auth.decorators import login_required

# Create your views here.
class LogInView(views.LoginView):
    template_name = "accounts/login.html"

    def get_user():
        return None

class SignUpView(generic.CreateView):
    template_name = "accounts/signup.html"
    model = User
    fields = ["first_name","last_name","email","password"]

@login_required
def user_profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'accounts/profile.html', context)