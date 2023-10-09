"""
FinanceExpense\
    .objects.values('expense_type')\ # что группировать
    .filter(date__month=1, transport=6)\ # по каким параметрам фильтровать записи
    .annotate(Sum('summ')) # что агрегатировать

    результат:
<QuerySet [
{'expense_type': 'Детейлинг', 'summ__sum': 540.0},
 {'expense_type': 'Заправка', 'summ__sum': 5200.0},
  {'expense_type': 'Ремонт', 'summ__sum': 1670.0}
  ]>

"""

