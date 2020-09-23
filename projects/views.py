from django.shortcuts import render, redirect
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
