from django.db import models

# Create your models here.
class Airport(models.Model):
    code= models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    origin= models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="depatures")
    destination  = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()


    def __str__(self) :
        return f"This flight is from {self.origin} to {self.destination} and takes {self.duration} hr/s"
    
class Passengers(models.Model):
    firstname=models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True,related_name="passengers")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"