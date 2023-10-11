from django.contrib import admin
from .models import Airport, Flight,Passengers

# Register your models here.

class AirportAdmin(admin.ModelAdmin):
    list_display =['city', 'code']

class FlightAdmin(admin.ModelAdmin):
    list_display = ['id','origin', 'destination', 'duration']


class PassengersAdmin(admin.ModelAdmin):
    filter_horizontal =("flights",)

admin.site.register(Airport,AirportAdmin)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Passengers,PassengersAdmin)
