from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Company, Job, JobType

# Create your views here.
def index(request):
    context = {
        "categories": Category.objects.all(),
        "companies": Company.objects.all(),
               }
    
    context['jobs'] = filter_jobs(request)
    return render(request, 'jobs/index.html', context)

def detail(request, job_id):
    job = get_object_or_404(Job, pk = job_id)
    context = {
        'job': job
    }
    return render(request, 'jobs/profile.html', context)

def apply(request, job_id):
    pass



def filter_jobs(request):
    jobs = Job.objects.all()
    if 'category_select' in request.POST and request.POST['category_select'] != "all":
        jobs.filter(category = request.POST['category_select'])
    if 'company_select' in request.POST and request.POST['company_select'] != "all":
        jobs.filter(company = request.POST['company_select'])
    if 'full_time' in request.POST and request.POST['full_time'] != 'on':
        fulltime = get_object_or_404(JobType, job_type = "Full time")
        jobs.filter(job_type = fulltime)
    if 'part_time' in request.POST and request.POST['part_time'] != 'on':
        jobs.filter(job_type = 1)
    if 'internship' in request.POST and request.POST['internship'] != 'on':
        jobs.filter(job_type = 2)
    return jobs


