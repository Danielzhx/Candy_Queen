from django.shortcuts import render, get_list_or_404
from jobs.models import Job
from .models import Company


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
