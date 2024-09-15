from django.shortcuts import render
from django.http import HttpResponse

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
    context = {'projects': projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project':projectObj})
