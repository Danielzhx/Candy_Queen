from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

def detail(request, job_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % job_id)

