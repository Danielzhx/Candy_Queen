from django.http import HttpResponse
from signup.models import Individual

def get_pic(request, user_id):
    profile = Individual.objects.get(pk=user_id)
    print(profile.pic)
    return HttpResponse(str(profile.pic))