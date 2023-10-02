from django.urls import path
from .views import AddFinanceExpenses

urlpatterns = [
    path('add_expense/', AddFinanceExpenses.as_view(), name='add_expense'),
]
