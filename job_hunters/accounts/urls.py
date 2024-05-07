from django.urls import path
from django.contrib.auth import views as authviews

from . import views

app_name = 'accounts'
urlpatterns = [
    path("login/", authviews.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", authviews.LogoutView.as_view(next_page='accounts/login'), name="logout"),
    path("signup/", views.signup_type, name="signup_type"),
    path("signup/user", views.register, name="register"),
    path("signup/user/profile", views.register_profile, name="register_profile"),
    # path("signup/company", views.c_register, name="c_register")   Implement later
    path("profile/", views.user_profile, name="profile")
    # Change password
    # Edit profile
]