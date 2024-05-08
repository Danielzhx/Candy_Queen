from django.shortcuts import render, get_list_or_404
from django.views import generic

from jobs.models import Company


# Create your views here.
def index(request):
    template = "companies/index.html"
    companies = Company.objects.all()
    return render(request, template, {'companies': companies})

def details(request, comp_id):
    template = "companies/profile.html"
    company = get_list_or_404(Company, pk=comp_id)
    return render(request, template, {'company': company})

def companies(request):
    template = "companies/companies.html"
    companies = Company.objects.all()
    return render(request, template, {'companies': companies})