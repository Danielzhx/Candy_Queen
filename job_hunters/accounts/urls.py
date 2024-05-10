from django.urls import path
from django.contrib.auth import views as authviews

import accounts
from . import views

app_name = 'accounts'
urlpatterns = [
    path("profile/", views.user_profile, name="profile"),
    path("profile/applications", views.view_applications, name="applications"),
]