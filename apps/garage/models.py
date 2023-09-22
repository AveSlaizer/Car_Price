from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class FuelType(models.Model):
    fuel_type = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name="Тип топлива"
    )

    def __str__(self):
        return self.fuel_type

    class Meta:
        verbose_name = 'Тип топлива'
        verbose_name_plural = 'Типы топлива'


class TransmissionType(models.Model):
    gearbox_type = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name="Тип КПП"
    )

    def __str__(self):
        return self.gearbox_type

    class Meta:
        verbose_name = 'Вид коробки передач'
        verbose_name_plural = 'Виды коробок передач'


class DriveType(models.Model):
    drive_type = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name="Тип привода"
    )

    def __str__(self):
        return self.drive_type

    class Meta:
        verbose_name = 'Тип привода'
        verbose_name_plural = 'Типы приводы'


class TransportCategory(models.Model):
    category = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name="Категория"
    )

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория транспорта'
        verbose_name_plural = 'Категории транспорта'


class Transport(models.Model):
    brand = models.CharField(
        default="Марка",
        max_length=30,
        verbose_name="Марка"
    )
    model = models.CharField(
        default="Модель",
        max_length=30,
        verbose_name="Модель"
    )
    year = models.IntegerField(
        default=datetime.now().year,
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)],
        verbose_name="Год выпуска"
    )
    engine_volume = models.FloatField(
        default=1.6,
        validators=[MinValueValidator(0), MaxValueValidator(100.0)],
        verbose_name="Объем двигателя, л"
    )
    engine_power = models.FloatField(
        default=1,
        validators=[MinValueValidator(0.1)],
        verbose_name="Мощность, л/с"
    )
    odometer = models.IntegerField(
        default=12345,
        null=False, validators=[MinValueValidator(1)],
        verbose_name="Пробег, км"
    )
    fuel_type = models.ForeignKey(
        'FuelType',
        on_delete=models.PROTECT,
        verbose_name='Топливо'
    )
    transmission_type = models.ForeignKey(
        'TransmissionType',
        on_delete=models.PROTECT,
        verbose_name='Коробка'
    )
    drive_type = models.ForeignKey(
        'DriveType',
        on_delete=models.PROTECT,
        verbose_name='Привод'
    )
    category = models.ForeignKey(
        'TransportCategory',
        on_delete=models.PROTECT,
        verbose_name='Категория'
    )

    owner = models.ForeignKey(
        'auth.user',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Владелец'
    )

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}г"

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'
