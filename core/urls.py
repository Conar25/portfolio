from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search_view, name="search"),
    path('', views.index_view, name="index"),
]