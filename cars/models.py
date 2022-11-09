from django.db import models

# Create your models here.
class Karysel(models.Model):
    image = models.ImageField(upload_to='')


class Catal(models.Model):
    class CarType(models.IntegerChoices):
        UNKNOWN = 0, ('Unknown')
        SEDAN = 1, ('Sedan')
        HATCHBACK = 2, ('Hatchback')
        UNIVERSAL = 3, ('Universal')
        SUV = 4, ('SUV')
        TRUCK = 5, ('Truck')
        MINIVAN = 6, ('Minivan')
        COUPE = 7, ('Coupe')
        ROADSTER = 8, ('Roadster')

    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    carType = models.IntegerField(default=CarType.UNKNOWN, choices=CarType.choices)
    price = models.IntegerField()


