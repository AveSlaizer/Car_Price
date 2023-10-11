from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .forms import AddTransportForm
from .models import Transport


class AddTransport(SuccessMessageMixin, CreateView):
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
