from django.shortcuts import render, get_list_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from Forms.edit_forms import CEditForm
from .models import Company
from jobs.models import Job


# Create your views here.
def index(request):
    template = "companies/index.html"
    companies = Company.objects.all()
    return render(request, template, {'companies': companies})


def details(request, comp_id):
    template = "companies/profile.html"
    company = get_list_or_404(Company, pk=comp_id)
    jobs = Job.objects.all().filter(company = company[0])
    return render(request, template, {'company': company[0],'jobs':jobs})

@login_required
def edit(request):
    template_name = 'companies/edit.html'
    user = request.user
    company = Company.objects.get(user = request.user)
    context = {'auto_name': company.name,
               'auto_username': request.user.username,
               'auto_email': company.contact_email,
               'auto_phone': company.phone_number,
               'auto_address': company.address,
               'auto_desc': company.description}
    if request.method == 'POST':
        form = CEditForm(request.POST, request.FILES)
        if validate(form):
            user.username = form.data['user-username']
            company.contact_email = form.data['company-contact_email']
            company.phone_number = form.data['company-phone_number']
            company.address = form.data['company-address']
            company.description = form.data['company-description']
            user.save()
            company.save()
            return redirect('profiles:profiles')
        else:
            context['errors'] = form.errors
            return render(request, template_name, context)

    else:
        return render(request, template_name, context)
    


# Profile edit validation
def validate(form:CEditForm):
    e = validate_email(form.data['user-username'])
    if not e:
        form.add_error(NON_FIELD_ERRORS, ValidationError('Invalid account email'))
    c = validate_email(form.data['company-contact_email'])
    if not c:
        form.add_error(NON_FIELD_ERRORS, ValidationError('Invalid contact email'))
    a = validate_address(form.data['company-address'])
    if not a:
        form.add_error(NON_FIELD_ERRORS, ValidationError('Invalid address'))
    p = form.data['company-phone_number'].isnumeric()
    if not p:
        form.add_error(NON_FIELD_ERRORS, ValidationError('Invalid phone number'))

    return e and c and a and p

def validate_email(email: str):
    e_split = email.split('@')
    if len(e_split) == 2:
        if len(e_split[1].split('.')) == 2:
            return True
    return False

def validate_address(address: str):
    a_split = address.split(' ')
    return len(a_split) >= 2 and a_split[0].isalpha() and a_split[-1].isnumeric()
