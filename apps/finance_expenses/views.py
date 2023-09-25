from django.shortcuts import render
from django.views.generic import TemplateView


class AddFinanceExpenses(TemplateView):
    template_name = 'finance_expenses/add_expense.html'

    def get(self, request, *args, **kwargs):
        context = {'transport_id': self.request.GET.get('transport_id')}
        super().get(context, *args, **kwargs)

# TODO вытащить GET запросом из адресной строки параметры
