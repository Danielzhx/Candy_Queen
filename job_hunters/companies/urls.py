from django.urls import path
from . import views

app_name = 'companies'
urlpatterns = [
    path("", views.index, name="index"),
    path("companies/", views.companies, name="companies"),
    path("<int:comp_id>/", views.details, name="details"),
]