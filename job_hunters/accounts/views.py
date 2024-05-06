from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import views, authenticate, login
from django.views import generic
from django.contrib.auth.decorators import login_required

# Create your views here.
class LogInView(views.LoginView):
<<<<<<< HEAD
    template_name = "account/login.html"
    next_page = "jobs/"
=======
    template_name = "accounts/login.html"
>>>>>>> 0b2cde8437ff0fa523692cc158e0f1e985606cae

    def get_user():
        return None

class SignUpView(generic.CreateView):
    template_name = "account/signup.html"
    model = User
    fields = ["first_name","last_name","email","password"]

@login_required
def user_profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'accounts/profile.html', context)