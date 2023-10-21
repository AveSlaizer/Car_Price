from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Model
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView
from django.urls import reverse_lazy

from .forms import AddTransportForm, DeleteTransportForm
from .models import Transport
from ..finance_expenses.utils import DataMixin


class AddTransportView(SuccessMessageMixin, CreateView):
    """
    Рендерит шаблон с формой добавления записи о тратах
    """
    form_class = AddTransportForm
    template_name = 'garage/add_transport.html'
    success_message = 'Транспорт успешно добавлен'

    def form_valid(self, form: forms) -> HttpResponseRedirect:
        """
        Проверяет данные формы и добавляет данные полученные из self.request.
        :param form: Объект формы
        :return: HttpResponseRedirect объект перенаправления на страницу определенную в методе get_success_url
        """
        transport = form.save(commit=False)
        transport.save()
        transport.owner = self.request.user
        response = super().form_valid(form)
        return response

    def get_success_url(self) -> reverse_lazy:
        """
        Возвращает тэг шаблона.
        :return: reverse_lazy
        """
        return reverse_lazy('garage')


class GarageView(ListView):
    model = Transport
    context_object_name = 'transport_list'
    template_name = 'garage/garage.html'

    def get_queryset(self):
        """
        Возвращает объект Queryset. Результат запроса в БД
        """
        return Transport.objects.filter(owner=self.request.user.id)


class DeleteTransportView(DataMixin, SuccessMessageMixin, DeleteView):
    form_class = DeleteTransportForm
    template_name = 'garage/delete_transport.html'
    success_message = 'Транспорт удален'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transport_obj = None

    def get_object(self, queryset=None) -> Model:
        """
        Возвращает объект из модели, который будет удален
        :param queryset: queryset
        :return: объект Model
        """
        self.transport_obj = self.get_transport(self.request)
        return self.transport_obj

    def get_initial(self) -> dict:
        """
        Возвращает словарь с данными, которые будут отображаться в форме перед ее заполнением.
        :return: dict - словарь с данными для формы
        """
        initial = super(DeleteTransportView, self).get_initial()
        initial['transport'] = self.transport_obj
        return initial

    def get_success_url(self) -> reverse_lazy:
        """
        Возвращает тэг шаблона.
        :return: reverse_lazy
        """
        return reverse_lazy('garage')
