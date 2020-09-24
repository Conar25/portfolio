from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('search/', views.search_view, name="search"),
    path('<slug:slug>/', views.project_view, name='project'),
]