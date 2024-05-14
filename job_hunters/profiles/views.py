from django.shortcuts import render, redirect
from Forms.signup_form import ISignupForm
from Forms.edit_profile import IEditForm 
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

def edit(request):
    template_name = "profiles/edit.html"
    current = Individual.objects.get(pk = request.user.id)
    context = {
        'auto_username': request.user.username,
        'auto_firstname': request.user.first_name,
        'auto_lastname': request.user.last_name,
        'auto_phone': current.phone_number,
        'auto_address': current.address,
        'auto_DoB': current.date_of_birth,
        'auto_avatar': current.pic
    }
    if request.method == 'POST':
        # Handle input data
        profile = IEditForm(data=request.POST)
        if profile.is_valid():
            for attr in profile:
                print(attr)

            return redirect('profiles')

        else:
            print(profile.errors)
            context['errors'] = profile.errors
            return render(request, template_name, context)

    else:
        # display page
        
        return render(request, template_name, context)

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
