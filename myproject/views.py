# from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse("Hello, world! This is the home page.")

# def about(request):
#     return HttpResponse("My name is Angel Arreola.")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')