from django.apps import AppConfig


class FinanceExpensesConfig(AppConfig):
    """
    Настройки приложения finance_expense.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.finance_expenses'
    verbose_name = 'Траты на ТС'
