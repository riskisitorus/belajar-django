from django.shortcuts import render
from .models import Profile

# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles,
    }
    return render(request, 'users/profiles.html', context)

def Userprofile(request, pk):
    profile = Profile.objects.get(id=str(pk))
    topSkills = profile.skill_set.exclude(description__exact='')
    allSkills = profile.skill_set.filter(description='')
    context = {
        'profile': profile,
        'topSkills': topSkills,
        'allSkills': allSkills,
    }
    return render(request, 'users/user-profile.html', context)