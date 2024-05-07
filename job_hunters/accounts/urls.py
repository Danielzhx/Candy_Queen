from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path("login/", views.LogInView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.signup_type, name="signup_type"),
    path("signup/user", views.register, name="register"),
    path("signup/user/profile", views.register_profile, name="register_profile"),
    # path("signup/company", views.c_register, name="c_register")   Implement later
    path("profile/", views.user_profile, name="profile")
    # Change password
    # Edit profile
]