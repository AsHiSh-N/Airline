from django.db import models
import datetime

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=15)
    def __str__(self):
        return f"({self.code}) {self.city}"

class Flight(models.Model):
    origin = models.ForeignKey(Airport , on_delete = models.CASCADE, related_name="departure")
    destination = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name="arrival")
    duration = models.IntegerField()
    date = models.DateField()
    

    def __str__(self):
        return f"{self.origin} to {self.destination} of {self.duration} Minutes on {self.date}"

class Passenger(models.Model):
    first = models.CharField(max_length=25)
    last = models.CharField(max_length=15)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"