from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializers
from projects.models import Project, Tag
from users.models import Profile

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'POST': 'api/projects/id/vote'},

        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializers(projects, many=True)
    context = {}
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request,pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializers(projects, many=False)
    context = {}
    return Response(serializer.data)