from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passengers

# Create your views here.

def index(request):
    return render(request, "flight/index.html",{
        "flights" : Flight.objects.all()
    })

def Oneflight(request, flight_id):
    one_flight = Flight.objects.get(pk=flight_id)
    return render(request, "flight/flight.html",{
        "one_flight": one_flight,
        "passengers" : one_flight.passengers.all(),
        "non_passengers" : Passengers.objects.exclude(flights=one_flight).all()
    })
     
def book(request, flight_id):
    if request.method=="POST":
        flight= Flight.objects.get(pk=flight_id)
        passenger = Passengers.objects.get(pk=int(request.POST['passenger']))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight:Oneflight", args=(flight_id,)))
    
    