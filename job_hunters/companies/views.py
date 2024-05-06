from django.shortcuts import render
from django.views import generic


# Create your views here.
def index(request):
    template = "companies/index.html"
    return render(request, template)

class CompDetailView(generic.DetailView):
    template_name = "companies/detail."