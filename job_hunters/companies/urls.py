from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:comp_id>/", views.detail, name="details"),
]