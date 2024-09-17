from django.db.models import Q
from .models import Profile, Skill

def searchProfiles(request):
    seacrh_query = ''

    if request.GET.get('query'):
        seacrh_query = request.GET.get('query')
    
    skills = Skill.objects.filter(name__icontains=seacrh_query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=seacrh_query)|
        Q(short_intro__icontains=seacrh_query)|
        Q(skill__in=skills))
    
    return profiles, seacrh_query