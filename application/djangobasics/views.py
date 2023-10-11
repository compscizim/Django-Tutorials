from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World")

def wellington(request):
    return HttpResponse("hello, Wellington")


def greet(request,name):
    return render(request, "djangobasics/greet.html",{
        "name" : name.capitalize
    })