from django.shortcuts import render, redirect
from Forms.edit_forms import IndEditForm
from django.utils.datastructures import MultiValueDictKeyError
from signup.models import Individual
from companies.models import Company
from datetime import datetime
from jobs.models import Application, Experiences, References
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
    return render(request, template_name, content)


@login_required
def edit(request):
    template_name = "profiles/edit.html"
    user = request.user
    current = Individual.objects.get(pk = request.user.id)
    context = {
        'auto_username': user.username,
        'auto_firstname': user.first_name,
        'auto_lastname': user.last_name,
        'auto_phone': current.phone_number,
        'auto_address': current.address,
        'auto_DoB': datetime.strftime(current.date_of_birth, '%Y-%m-%d')
    }
    if request.method == 'POST':
        """
        copy = request.POST.copy()
        copy.update({'date_joined': user.date_joined})"""
        indprofile = IndEditForm(request.POST, request.FILES, instance=current)
        print(request.POST)
        if indprofile.is_valid() and validate(indprofile, request.POST):
            user.username = request.POST['username']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            current.save()
            return redirect('profiles:profiles')
        
        else:
            print(indprofile.errors)
            context['individual_errors'] = indprofile.errors
            return render(request, template_name, context)

    else:        
        return render(request, template_name, context)

@login_required
def view_applications(request):
    """Allows a user to see and manage their applications."""
    try:
        user = Individual.objects.get(parent_user_id=request.user.id)
    except:
        return redirect('/profile')

    applications = Application.objects.all().filter(user=user)
    temp = {"applications": [application for application in applications]}
    return render(request, 'applications/index.html', temp)

@login_required
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
    DoB = datetime.strptime(DoB, '%Y-%m-%d')
    print('\n\nDoB Check:')
    print(f"DoB:{DoB}, type:{type(DoB)}")
    print(f"Now:{datetime.now()}")
    print(f"Result:{DoB < datetime.now()}")
    print('\n\n')
    return DoB < datetime.now()
    
def validate(form, data):
    e, f, l, a, p, d = True, True, True, True, True, True
    if data['username']:
        e = validate_email(data['username'])
    if data['first_name']:
        f = validate_name(data['first_name'])
    if data['last_name']:
        l = validate_name(data['last_name'])
    if data['address']:
        a = validate_address(data['address'])
    if data['phone_number']:
        p = validate_phone(data['phone_number'])
    if data['date_of_birth']:
        d = validate_DoB(data['date_of_birth'])
        if not d:
            form.errors['individual-phone_number'] = 'Phone number must be in the past.'
            form.errors.pop('user-date_joined')

    return e and f and l and a and p and d
