from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    path('send', views.send_view, name="send_email"),
]