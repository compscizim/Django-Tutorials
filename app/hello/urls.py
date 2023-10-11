from django.urls import path
from . import views
urlpatterns = [
    path("",  views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("wellington", views.wellington, name="wellington"),
    path("webster", views.webster , name="webster")
] 

   