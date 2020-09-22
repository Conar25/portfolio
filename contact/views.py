from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings

@require_POST
def send_view(request):
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    send_mail(subject, 
              message, 
              settings.EMAIL_HOST_USER,
              ['galiev2512@gmail.com'],
              fail_silently=False)

    return redirect('index')