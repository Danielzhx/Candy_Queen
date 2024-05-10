from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:job_id>/", views.detail, name="detail"),
    path("<int:job_id>/applications",views.apply, name="application"),
    path("<int:job_id>/applications/<int:application_id>/experiences",views.experience, name="experiences"),
    path("<int:job_id>/applications/<int:application_id>/references",views.reference, name="references")
    # Apply for job
    ]   
