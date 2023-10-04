from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class ExpenseTypes(models.Model):
    class Meta:
        verbose_name = 'Категория трат на ТС'
        verbose_name_plural = 'Категории трат на ТС'

    expense_type = models.CharField(
        primary_key=True,
        max_length=30,
        verbose_name="Тип расходов"
    )

    def __str__(self):
        return self.expense_type


class FinanceExpense(models.Model):
    class Meta:
        verbose_name = 'Трата на ТС'
        verbose_name_plural = 'Траты на ТС'
        ordering = ['add_date']

    transport = models.ForeignKey(
        'garage.Transport',
        on_delete=models.CASCADE,
        verbose_name="Транспорт"
    )
    summ = models.FloatField(
        blank=True,
        validators=[MinValueValidator(0)],
        verbose_name="Сумма",
        help_text="Укажите сумму израсходованных средств."
    )
    date = models.DateField(
        default=datetime.date.today(),
        validators=[MaxValueValidator(datetime.date.today())],
        verbose_name="Дата",
        help_text='Выберите дату'
    )
    odometer = models.PositiveIntegerField(
        blank=True,
        verbose_name="Пробег",
        help_text='Укажите пробег, на момент траты средств'
    )
    expense_type = models.ForeignKey(
        'ExpenseTypes',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Вид расходов',
        help_text='Выберите категорию расходов'
    )
    add_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    def __str__(self):
        return f"{self.summ} - {self.expense_type}, {self.date}"
