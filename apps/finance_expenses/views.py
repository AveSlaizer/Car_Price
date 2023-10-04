from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AddFinanceExpensesForm
from ..garage.models import Transport
from .models import FinanceExpense
import datetime


class AddFinanceExpenses(SuccessMessageMixin, CreateView):
    form_class = AddFinanceExpensesForm
    template_name = 'finance_expenses/add_expense.html'
    success_message = 'Запись успешно добавлена'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transport_obj = None

    def get_transport(self):
        transport_id = self.request.GET.get('transport_id')
        self.transport_obj = Transport.objects.get(pk=transport_id)

    def get_initial(self):
        initial = super(AddFinanceExpenses, self).get_initial()
        self.get_transport()
        initial['transport'] = self.transport_obj
        initial['odometer'] = self.transport_obj.odometer
        initial['date'] = datetime.date.today()
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


class ShowFinanceExpenses(ListView):
    model = FinanceExpense
    context_object_name = 'expenses'
    template_name = 'finance_expenses/expenses_table.html'

    def get_transport(self):
        transport_id = self.request.GET.get('transport_id')
        self.transport_obj = Transport.objects.get(pk=transport_id)

    def get_queryset(self):
        queryset = FinanceExpense.objects.filter(transport=self.request.GET.get('transport_id'))\
            .order_by('-date', '-odometer')
        self.queryset = queryset
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        initial = super(ShowFinanceExpenses, self).get_context_data(**kwargs)
        initial['header'] = [
            field.verbose_name for field in self.model._meta.get_fields() if field.verbose_name != 'Транспорт' and
                                                                             field.verbose_name != 'ID'
        ]
        initial['rows'] = list(self.queryset.values('summ', 'date', 'odometer', 'expense_type', 'add_date'))
        self.get_transport()
        initial['transport_name'] = self.transport_obj
        return initial
