from django.shortcuts import render

from projects.models import ProjectModel

def index_view(request):
    projects = ProjectModel.objects.all()[:3]
    return render(request, 'core/index.html', {
        'projects': projects,
        })
