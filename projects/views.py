from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.postgres.search import SearchVector, \
                                           SearchQuery, \
                                           SearchRank

from .models import ProjectModel


def search_view(request):
    query = request.GET.get('query', '')
    if query:
        search_vector = SearchVector('tags__name', weight='A') + \
                        SearchVector('title', weight='B') + \
                        SearchVector('description', weight='C')
        search_query = SearchQuery(query)
        projects = ProjectModel.objects.annotate(
            rank=SearchRank(search_vector, search_query)
        ).filter(rank__gte=0.3).order_by('-rank').distinct()
    else:        
        projects = ProjectModel.objects.all()
    return render(request, 'projects/search.html', {
        'projects': projects,
        })

def project_view(request, slug):
    project = get_object_or_404(ProjectModel, slug=slug)
    return render(request, project.get_template(), {'project': project})
