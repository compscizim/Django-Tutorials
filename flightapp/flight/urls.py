from django.urls import path

from . import views

app_name="flight"
urlpatterns = [
    path("", views.index , name="index"),
    path("<int:flight_id>", views.Oneflight , name="Oneflight"),
    path("<int:flight_id>/book", views.book, name="book")
    
]
