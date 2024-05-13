from django.shortcuts import render, redirect
from signup.models import Individual
from companies.models import Company
from jobs.models import Application, Experiences, References


# Create your views here.
def index(request):
    "Displays an individual profile."
    content = {}
    try:
        user = Individual.objects.get(parent_user_id=request.user.id)
        template_name = "profiles/indiv_profile.html"

    except:
        user = Company.objects.get(user_id=request.user.id)
        template_name = "profiles/company_profile.html"

    content["profile"] = user
    content["user"] = request.user
    return render(request, template_name, content)

def view_applications(request):
    """Allows a user to see and manage their applications."""
    try:
        user = Individual.objects.get(parent_user_id=request.user.id)
    except:
        return redirect('/profile')

    applications = Application.objects.all().filter(user=user)
    temp = {"applications": [application for application in applications]}
    return render(request, 'applications/index.html', temp)

def application_details(request,application_id):
    application = Application.objects.get(pk=application_id)
    experiences = Experiences.objects.all().filter(application=application)
    references = References.objects.all().filter(application=application)
    content = {
        "application":application,
        "experiences":[experience for experience in experiences],
        "references":[reference for reference in references]
    }
    return render(request, "applications/details.html", content) 
