from django.urls import path
from .views import AddFinanceExpenses, ShowFinanceExpenses, GraphView

urlpatterns = [
    path('add_expense/', AddFinanceExpenses.as_view(), name='add_expense'),
    path('expenses_table/', ShowFinanceExpenses.as_view(), name='expenses_table'),
    path('graphs/', GraphView.as_view(), name='graphs'),
]
