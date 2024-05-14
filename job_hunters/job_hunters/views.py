from django.http import HttpResponse
from signup.models import Individual
from companies.models import Company

def get_pic(request, user_id):
    try:
        profile = Individual.objects.get(pk=user_id)
        if profile.pic:
            return HttpResponse(str(profile.pic))
        else:
            return HttpResponse('images/default_avatar.jpg')        
    except Individual.DoesNotExist:
        pass

    try:
        company = Company.objects.get(user=user_id)
        return HttpResponse(str(company.logo))
    except Company.DoesNotExist:
        return HttpResponse('images/default_avatar.jpg')