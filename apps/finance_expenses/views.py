from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django_tables2 import SingleTableView
from django.utils import timezone

from .forms import AddFinanceExpensesForm
from .tables import FinanceExpenseTable
from .models import FinanceExpense
from .utils import DataMixin


class AddFinanceExpenses(DataMixin, SuccessMessageMixin, CreateView):
    form_class = AddFinanceExpensesForm
    template_name = 'finance_expenses/add_expense.html'
    success_message = 'Запись успешно добавлена'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transport_obj = None

    def get_initial(self):
        initial = super(AddFinanceExpenses, self).get_initial()
        self.transport_obj = self.get_transport(self.request)
        initial['transport'] = self.transport_obj
        initial['odometer'] = self.transport_obj.odometer
        initial['date'] = timezone.now().date()
        return initial

    def get_context_data(self, **kwargs):
        context = super(AddFinanceExpenses, self).get_context_data(**kwargs)
        context['transport_name'] = self.transport_obj
        return context

    def form_valid(self, form):
        form_odometer = form.cleaned_data['odometer']
        if form_odometer > self.transport_obj.odometer:
            self.transport_obj.odometer = form_odometer
            self.transport_obj.save()
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('garage')


class FinanceExpensesTableView(SingleTableView):
    model = FinanceExpense
    table_class = FinanceExpenseTable
    template_name = 'finance_expenses/expenses_table.html'

    def get_queryset(self):
        self.queryset = FinanceExpense.objects.filter(transport=self.request.GET.get('transport_id'))\
            .order_by('-odometer')
        return self.queryset
