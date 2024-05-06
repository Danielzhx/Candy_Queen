from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:job_id>/", views.detail, name="details"),
    # Apply for job
]