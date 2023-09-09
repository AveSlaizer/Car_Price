from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class FuelType(models.Model):
    name = models.CharField(unique=True, max_length=20)


class TransmissionType(models.Model):
    gearbox_type = models.CharField(unique=True, max_length=20)


class DriveType(models.Model):
    drive_type = models.CharField(unique=True, max_length=20)


class Transport(models.Model):
    brand = models.CharField(default="Марка", max_length=30)
    model = models.CharField(default="Модель", max_length=30)
    year = models.IntegerField(default=datetime.now().year,
                               validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)])
    engine_volume = models.FloatField(default=1.6, validators=[MinValueValidator(0.0001), MaxValueValidator(100.0)])
    odometer = models.IntegerField(default=12345, null=False, validators=[MinValueValidator(1)])
    fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL)
    transmission_type = models.ForeignKey(TransmissionType, on_delete=models.SET_NULL)
    drive_type = models.ForeignKey(DriveType, on_delete=models.SET_NULL)
    # TODO дописать модель Transport
    # TODO makemigrations, migrate
