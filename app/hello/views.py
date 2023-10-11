from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def wellington(request):
    return HttpResponse("hello, Wellington")

def webster(request):
    return HttpResponse("Hello webster")

def greet(request, name):
    return render(request, "hello/greet.html" , {
       "name" : name.capitalize()
    })
