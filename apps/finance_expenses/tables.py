import django_tables2 as tables
from .models import FinanceExpense


class FinanceExpenseTable(tables.Table):
    """
    Таблица для шаблона.
    """
    class Meta:
        model = FinanceExpense
        fields = ('summ', 'date', 'odometer', 'expense_type', 'add_date', 'description')
