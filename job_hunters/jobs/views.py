from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Category, Company, Job, JobType

# Create your views here.
def index(request):
    jobs = [{
        'id': x.id,
        'title': x.title,
        'description': x.description,
        'job_type': x.job_type.job_type,
        'category': x.category.category,
        'company': x.company.name,
        'due_date': x.due_date,
        'start_date': x.start_date
        } for x in Job.objects.all()]
    
    if 'query' in request.GET:
        if 'search_name' in request.GET:
            jobs = [x for x in jobs if request.GET['search_name'].lower() in x['title'].lower()]
            
        return JsonResponse({'data':jobs})

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
    #jobs = Job.objects.all()

    """if 'search_filter' in request.GET:
        jobs = Job.objects.filter(name__icontains = request.GET['search_filter'])
    if 'category_select' in request.POST and request.POST['category_select'] != "undefined":
        jobs.filter(category = request.POST['category_select'])
    if 'company_select' in request.POST and request.POST['company_select'] != "undefined":
        jobs.filter(company = request.POST['company_select'])"""
    

    """if 'search_filter' in request.GET:
        jobs = Job.objects.filter(name__icontains = request.GET['search_filter'])
    if 'category_select' in request.POST and request.POST['category_select'] != "all":
        jobs.filter(category = request.POST['category_select'])
    if 'company_select' in request.POST and request.POST['company_select'] != "all":
        jobs.filter(company = request.POST['company_select'])
    if 'full_time' in request.POST and request.POST['full_time'] != 'on':
        fulltime = get_object_or_404(JobType, job_type = "Full time")
        jobs.filter(job_type = fulltime)
    if 'part_time' in request.POST and request.POST['part_time'] != 'on':
        fulltime = get_object_or_404(JobType, job_type = "Full time")
        jobs.filter(job_type = 1)
    if 'internship' in request.POST and request.POST['internship'] != 'on':
        fulltime = get_object_or_404(JobType, job_type = "Full time")
        jobs.filter(job_type = 2)
    if 'order_by_due' == 'on':
        jobs.order_by('due_date')
    else:
        jobs.order_by('start_date')"""
    
    """
    print(jobs)

    return JsonResponse({'data': jobs})"""


