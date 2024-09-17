from django.db.models import Q
from .models import Project, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProjects(request, projects, results):
    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page=1
        projects = paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, projects

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