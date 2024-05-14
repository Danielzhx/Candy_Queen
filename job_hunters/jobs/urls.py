from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("<int:job_id>/", views.detail, name="detail"),
    path("<int:job_id>/applications/",views.apply, name="application"),
    path("<int:job_id>/applications/<int:application_id>/experiences",views.experience, name="experiences"),
    path("<int:job_id>/applications/<int:application_id>/references",views.reference, name="references"),
    path("<int:job_id>/companies/<int:company_id>/applications",views.company_applications, name="applicants"),
    path("<int:job_id>/companies/<int:company_id>/applications/<int:application_id>",views.company_application_details, name="applicants_detail")
    # Apply for job
    ]   
