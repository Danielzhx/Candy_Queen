from django.shortcuts import render, get_list_or_404, redirect
from django.views import generic

from .models import Company


# Create your views here.
def index(request):
    template = "companies/index.html"
    companies = Company.objects.all()
    return render(request, template, {'companies': companies})


def details(request, comp_id):
    template = "companies/profile.html"
    company = get_list_or_404(Company, pk=comp_id)
    return render(request, template, {'company': company[0]})


def edit(request):
    template_name = 'companies/edit.html'
    user = request.user
    company = Company.objects.get(user = request.user)
    context = {'auto_username': request.user.username,
               'auto_email': company.contact_email,
               'auto_phone': company.phone_number,
               'auto_address': company.address,
               'auto_desc': company.description}
    if request.method == 'POST':
        d = request.POST
        if validate(d):
            user.username = d['user-username']
            company.contact_email = d['company-contact_email']
            company.phone_number = d['company-phone_number']
            company.address = d['company-address']
            company.description = d['company-description']
            user.save()
            company.save()
            return redirect('profiles:profiles')
        else:
            # Implement Error display later
            return render(request, template_name, context)

    else:
        return render(request, template_name, context)
    


# Profile edit validation
def validate(data):
    e = validate_email(data['user-username'])
    c = validate_email(data['company-contact_email'])
    a = validate_address(data['company-address'])
    p = data['company-phone_number'].isnumeric()
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