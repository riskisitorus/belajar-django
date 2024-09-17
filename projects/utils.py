from django.db.models import Q
from .models import Project, Tag

def searchProjects(request):
    seacrh_query = ''

    if request.GET.get('query'):
        seacrh_query = request.GET.get('query')

    tags = Tag.objects.filter(name__icontains=seacrh_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=seacrh_query)|
        Q(description__icontains=seacrh_query)|
        Q(owner__name__icontains=seacrh_query)|
        Q(tags__in=tags)
        )
    return projects, seacrh_query