from django.shortcuts import render
# from .models import User
# Create your views here.

def register_user(request):
    return render(request, 'users/register.html')
