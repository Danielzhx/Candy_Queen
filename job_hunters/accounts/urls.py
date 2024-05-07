from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path("login/", views.LogInView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup_type/", views.signup_type, name="signup_type"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signup/new/", views.new_user, name="new_user"),
    path("profile/", views.user_profile, name="profile")
    # Change password
    # Edit profile
]