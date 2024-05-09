from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Company, Job, Application
from signup.models import Individual
from Forms.filter_form import FilterForm, ORDERS
from Forms.application_form import ApplicationForm, ExperienceForm, ReferencesForm

# Create your views here.
def index(request):
    form = FilterForm(request.GET)
    context = {
        'form': form,
        "categories": Category.objects.all(),
        "companies": Company.objects.all(),
    }
    context['jobs'] = filter_jobs(request)
    return render(request, 'jobs/index.html', context)


def detail(request, job_id):
    """Detail view for individual job posting.
    """
    job = get_object_or_404(Job, pk=job_id)
    context = {
        'job': job
    }
    return render(request, 'jobs/profile.html', context)


def apply(request, job_id):
    """
        Application view for job posting.
    """
    
    # TODO: Remove the try except and replace with djangos permissions
    try:
        individual = Individual.get(user_id=request.user.id)
    except:
        return redirect('/jobs')

    if request.method == "POST":
        job = Job.objects.get(pk=job_id)
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = Application(form.data, user=individual, job=job_id)
            application.save()
            # TODO: Change redirect to application review page
            return redirect('/jobs')

    else:
        form = ApplicationForm()

    content = {
        'form':form
    }

    return render(request, 'applications/apply.html', content)


def filter_jobs(request):
    jobs = Job.objects.all()
    if not request.GET:
        return jobs

    type_selection = request.GET.getlist("job_type")
    if len(type_selection) > 0:
        jobs = jobs.filter(job_type__in=type_selection)

    if request.GET['title']:
        jobs = jobs.filter(title__icontains=request.GET['title'])

    if request.GET['company']:
        jobs = jobs.filter(company=request.GET['company'])

    if request.GET['category']:
        jobs = jobs.filter(category=request.GET['category'])

    if request.GET['order_by']:
        order = ORDERS[int(request.GET['order_by'])][1]
        if not order:
            return jobs

        jobs = jobs.order_by(order)

    return jobs

def experience(request):
    """Experiences view for applying to a job."""
    return render(request, 'applications/experience.html')
