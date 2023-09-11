from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class FuelType(models.Model):
    fuel_type = models.CharField(primary_key=True, max_length=20, verbose_name="Топливо")

    def __str__(self):
        return self.fuel_type


class TransmissionType(models.Model):
    gearbox_type = models.CharField(primary_key=True, max_length=20, verbose_name="КПП")

    def __str__(self):
        return self.gearbox_type


class DriveType(models.Model):
    drive_type = models.CharField(primary_key=True, max_length=20, verbose_name="Привод")

    def __str__(self):
        return self.drive_type


class TransportCategory(models.Model):
    category = models.CharField(primary_key=True, max_length=20, verbose_name="Категория")

    def __str__(self):
        return self.category


class Transport(models.Model):
    brand = models.CharField(default="Марка", max_length=30, verbose_name="Марка")
    model = models.CharField(default="Модель", max_length=30, verbose_name="Модель")
    year = models.IntegerField(default=datetime.now().year,
                               validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)],
                               verbose_name="Год выпуска")
    engine_volume = models.FloatField(default=1.6, validators=[MinValueValidator(0), MaxValueValidator(100.0)],
                                      verbose_name="Объем двигателя, л")
    engine_power = models.FloatField(default=1, validators=[MinValueValidator(0.1)], verbose_name="Мощность, л/с")
    odometer = models.IntegerField(default=12345, null=False, validators=[MinValueValidator(1)],
                                   verbose_name="Пробег, км")
    fuel_type = models.ForeignKey(FuelType, null=True, on_delete=models.SET_NULL)
    transmission_type = models.ForeignKey(TransmissionType, null=True, on_delete=models.SET_NULL)
    drive_type = models.ForeignKey(DriveType, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(TransportCategory, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}г"
