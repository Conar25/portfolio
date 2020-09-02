from django.shortcuts import render


def index_view(request):
    return render(request, 'projects/index.html', {})

def search_view(request):
    return render(request, 'projects/search.html', {})
