from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm

# Create your views here.
def loginUser(request):
    page = 'login'
    context = {'page':page}
    # cegah user yang sudah login ke halaman login
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            # messages.error(request, 'username does not exist')
            user = None
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html', context)

@login_required
def logoutUser(request):
    logout(request)
    messages.info(request, 'user was logout')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('profiles')
        else:
            messages.success(request, 'An error has occurred during registration')


    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)

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