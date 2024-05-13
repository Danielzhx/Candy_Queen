from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path("", views.index, name="profiles"),
    path("applications", views.view_applications, name="applications"),
    path("applications/<int:application_id>",views.application_details, name="application_detail"),
    ]   
