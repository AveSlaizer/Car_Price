from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class FuelType(models.Model):
    """
    Таблица в БД. Содержит записи о типах топлива.
    """
    fuel_type = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name='Тип топлива'
    )

    def __str__(self):
        return self.fuel_type

    class Meta:
        verbose_name = 'Тип топлива'
        verbose_name_plural = 'Типы топлива'


class TransmissionType(models.Model):
    """
    Таблица в БД. Содержит записи о типах коробок передач.
    """
    gearbox_type = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name='Тип КПП'
    )

    def __str__(self):
        return self.gearbox_type

    class Meta:
        verbose_name = 'Вид коробки передач'
        verbose_name_plural = 'Виды коробок передач'


class DriveType(models.Model):
    """
    Таблица в БД. Содержит записи о видах привода.
    """
    drive_type = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name='Тип привода'
    )

    def __str__(self):
        return self.drive_type

    class Meta:
        verbose_name = 'Тип привода'
        verbose_name_plural = 'Типы приводы'


class TransportCategory(models.Model):
    """
    Таблица в БД. Содержит записи о категориях ТС.
    """
    class Meta:
        verbose_name = 'Категория транспорта'
        verbose_name_plural = 'Категории транспорта'

    category = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name='Категория'
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/garage/transport_cat/',
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.category


class Transport(models.Model):
    """
    Таблица в БД. Содержит записи о транспорте.
    """
    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'
        ordering = ['brand', 'model', 'year']

    brand = models.CharField(
        null=True,
        max_length=50,
        verbose_name="Марка",
        help_text='Введите марку транспортного средства. Максимум 50 символов.'
    )
    model = models.CharField(
        null=True,
        max_length=50,
        verbose_name="Модель",
        help_text='Введите модель транспортного средства. Максимум 50 символов.'
    )
    year = models.IntegerField(
        default=timezone.now().year,
        validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)],
        verbose_name="Год выпуска",
        help_text='Введите год выпуска транспортного средства.'
    )
    engine_volume = models.FloatField(
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100.0)],
        verbose_name="Объем двигателя, л",
        help_text='Введите объем двигателя транспортного средства.'
    )
    engine_power = models.FloatField(
        null=True,
        validators=[MinValueValidator(0.1)],
        verbose_name="Мощность, л/с",
        help_text='Введите мощность транспортного средства.'
    )
    odometer = models.IntegerField(
        null=True,
        validators=[MinValueValidator(1)],
        verbose_name="Пробег, км",
        help_text='Введите пробег транспортного средства.'
    )
    fuel_type = models.ForeignKey(
        'FuelType',
        default=FuelType.objects.all().first().pk,
        on_delete=models.PROTECT,
        verbose_name='Топливо',
        help_text='Выберите тип топлива потребляемого транспортным средством.'
    )
    transmission_type = models.ForeignKey(
        'TransmissionType',
        default=TransmissionType.objects.all().first().pk,
        on_delete=models.PROTECT,
        verbose_name='Коробка',
        help_text='Выберите вид коробки перемены передач транспортного средства.'
    )
    drive_type = models.ForeignKey(
        'DriveType',
        default=DriveType.objects.all().first().pk,
        on_delete=models.PROTECT,
        verbose_name='Привод',
        help_text='Выберите тип привода транспортного средства.'
    )
    category = models.ForeignKey(
        'TransportCategory',
        default=TransportCategory.objects.all().first().pk,
        on_delete=models.PROTECT,
        verbose_name='Категория',
        help_text='Выберите категорию транспортного средства.'
    )

    description = models.CharField(
        null=True,
        blank=True,
        max_length=150,
        verbose_name='Описание',
        help_text='Введите описание транспортного средства.\n'
                  'Например гос. номер. Не обязательно для заполнения'
    )

    owner = models.ForeignKey(
        'auth.user',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Владелец'
    )

    add_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}г."
