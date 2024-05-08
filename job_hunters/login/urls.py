from django.urls import path
from django.contrib.auth import views as authviews

from . import views

app_name = 'login'
urlpatterns = [
    path("", authviews.LoginView.as_view(template_name="login/login.html"), name="login"),
    path("out/", authviews.LogoutView.as_view(next_page='login:login'), name="logout"),
]