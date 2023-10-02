from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AddFinanceExpensesForm
from ..garage.models import Transport
import datetime


class AddFinanceExpenses(SuccessMessageMixin, CreateView):
    form_class = AddFinanceExpensesForm
    template_name = 'finance_expenses/add_expense.html'
    success_message = 'Запись успешно добавлена'

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

    def form_valid(self, form):
        finance_record = form.save(commit=False)
        finance_record.save()
        self.transport_obj.odometer = finance_record['odometer']
        self.transport_obj.save()
        response = super().form_valid(form)
        return response
# FIXME обновить пробег ТС при добавлении новой записи о расходах

    def get_success_url(self):
        return reverse_lazy('garage')
