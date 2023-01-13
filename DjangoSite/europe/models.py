from django.db import models

# Create your models here.
class Trip(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    nights = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}, for {self.nights} with price of {self.price} EUR"