from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
projectsList = [
    {
        'id' : '1',
        'title' : 'Project 1',
        'description' : 'Ini adalah deskripsi untuk project pertama saya',
    },
    {
        'id' : '2',
        'title' : 'Project 2',
        'description' : 'Ini adalah deskripsi untuk project kedua saya',
    },
    {
        'id' : '3',
        'title' : 'Project 3',
        'description' : 'Ini adalah deskripsi untuk project ketiga saya',
    },
]

def projects(request):
    Projects = Project.objects.all()
    context = {'projects': Projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=str(pk))
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project':projectObj, 'tags':tags})
