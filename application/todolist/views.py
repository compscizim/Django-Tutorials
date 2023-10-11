from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


class TodoForm(forms.Form):
    todo = forms.CharField(label="todo")

# Create your views here.

def index(request):
    if "todos" not in request.session:
        request.session["todos"] =[]
    return render(request, "todolist/index.html",{
        "todos":  request.session["todos"]
    })

def add(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.cleaned_data["todo"]
            request.session["todos"] +=[todo]
            return HttpResponseRedirect(reverse("index"))
        else: 
            render(request,"todolist/add.html",{
                "form" : form
            })
    return render(request, "todolist/add.html",{
        "form": TodoForm()
    })