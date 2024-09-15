from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

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

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=str(pk))
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=str(pk))

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
