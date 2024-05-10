from django.urls import path
from django.contrib.auth import views as authviews

from . import views

app_name = 'accounts'
urlpatterns = [
    path("profile/", views.user_profile, name="profile"),
    path("profile/applications", views.applications, name="applications"),
]