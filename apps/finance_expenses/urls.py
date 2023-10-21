from django.urls import path
from .views import AddFinanceExpensesView, FinanceExpensesTableView

urlpatterns = [
    path('add_expense/', AddFinanceExpensesView.as_view(), name='add_expense'),
    path('expenses_table/', FinanceExpensesTableView.as_view(), name='expenses_table'),
]
