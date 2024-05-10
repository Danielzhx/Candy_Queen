from django.shortcuts import render
from signup.models import Individual
from companies.models import Company

# Create your views here.
def index(request):
    "Displays an individual profile."
    content = {}
    try:
        user = Individual.objects.get(parent_user_id=request.user.id)
        template_name = "profiles/indiv_profile.html"

    except:
        user = Company.objects.get(parent_user_id=request.user.id)
        template_name = "profiles/company_profile.html"

    content["user"] = user
    content["profile"] = request.user
    return render(request, template_name, content)