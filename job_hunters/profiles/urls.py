from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path("", views.index, name="profiles")
    # Apply for job
    ]   
