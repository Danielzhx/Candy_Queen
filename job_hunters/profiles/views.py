from django.shortcuts import render, redirect
from Forms.signup_form import ISignupForm
from Forms.edit_forms import IEditForm 
from signup.models import Individual
from companies.models import Company
from datetime import datetime
from jobs.models import Application, Experiences, References


# Create your views here.
def index(request):
    "Displays an individual profile."
    content = {}
    try:
        profile = Individual.objects.get(parent_user_id=request.user.id)
        template_name = "profiles/indiv_profile.html"

    except:
        profile = Company.objects.get(user_id=request.user.id)
        template_name = "profiles/company_profile.html"

    content["profile"] = profile
    content["user"] = request.user
    print(content['profile'].logo)
    return render(request, template_name, content)

def edit(request):
    template_name = "profiles/edit.html"
    user = request.user
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
        profile = IEditForm(data=request.POST, instance={'User': request.user, 'Individual': current})
        if validate(profile.data['user-username'], 
                    profile.data['user-first_name'], 
                    profile.data['user-last_name'],
                    profile.data['individual-address'],
                    profile.data['individual-phone_number'],
                    profile.data['individual-date_of_birth']):
            user.username = profile.data['user-username']
            user.first_name = profile.data['user-first_name']
            user.last_name = profile.data['user-last_name']
            current.address = profile.data['individual-address']
            current.phone_number = profile.data['individual-phone_number']
            current.pic = request.FILES['individual-pic']
            if profile.data['individual-date_of_birth']:
                current.date_of_birth = profile.data['individual-date_of_birth']
            user.save()
            current.save()
            return redirect('profiles:profiles')

        else:
            print(profile.errors)
            context['errors'] = profile.errors
            return render(request, template_name, context)

    else:        
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


# Profile edit validation
def validate_email(email: str):
    e_split = email.split('@')
    if len(e_split) == 2:
        if len(e_split[1].split('.')) == 2:
            return True        
    return False

def validate_name(name: str):
    return name.isalpha()

def validate_address(address: str):
    a_split = address.split(' ')
    return len(a_split) >= 2 and a_split[0].isalpha() and a_split[-1].isnumeric()

def validate_phone(phone: str):
    return phone.isnumeric()

def validate_DoB(DoB):
    return DoB < datetime.now()
    
def validate(email, firstname, lastname, address, phone, DoB):
    e, f, l, a, p, d = True, True, True, True, True, True
    if email:
        e = validate_email(email)
    if firstname:
        f = validate_name(firstname)
    if lastname:
        l = validate_name(lastname)
    if address:
        a = validate_address(address)
    if phone:
        p = validate_phone(phone)
    if DoB:
        d = validate_DoB(DoB)
    return e and f and l and a and p and d