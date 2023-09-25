from django.urls import path
from .views import AddFinanceExpenses
from django.views.generic import TemplateView

urlpatterns = [
    path('add_expense/<int:transport_id>/', TemplateView.as_view(template_name='finance_expenses/add_expense.html'),
         name='add_expense'),
]
