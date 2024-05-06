from django.shortcuts import render, get_object_or_404
from jobs.models import Job
from django.http import HttpResponse

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/index.html',{"jobs":jobs})

def detail(request, job_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % job_id)

def apply(request, job_id):
    pass
