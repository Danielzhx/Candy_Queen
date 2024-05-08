from django.urls import path

from . import views

app_name = 'signup'
urlpatterns = [
    path("", views.signup_type, name="index"),
    path("user", views.reg_individual, name="reg_individual"),
    path("user/profile", views.register_profile, name="register_profile"),
    # path("signup/company", views.c_register, name="c_register")   Implement later
    # Change password
    # Edit profile
]