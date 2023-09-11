from django.db import models
from apps.garage.models import Transport
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class ExpenseTypes(models.Model):
    expense_type = models.CharField(primary_key=True, max_length=30, verbose_name="Тип расходов")

    def __str__(self):
        return self.expense_type


class FinanceExpense(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, verbose_name="Транспорт")
    summ = models.FloatField(default=1, validators=[MinValueValidator(0)], verbose_name="Сумма")
    date = models.DateField(default=timezone.now, validators=[MaxValueValidator(timezone.now)], verbose_name="Дата")
    odometer = models.IntegerField(default=1,
                                   validators=[MinValueValidator(1)],
                                   verbose_name="Пробег")
    expense_type = models.ForeignKey(ExpenseTypes, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.summ} - {self.expense_type}, {self.date}"
