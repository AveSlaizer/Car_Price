from django.shortcuts import render
from django.utils import timezone
from django.views.generic import FormView

from .forms import MonthGraphSelectForm
from .utils.graph_builder import MonthGraphBuilder
from .utils.month_graphs_settings import MONTHS_NAMES
from ..finance_expenses.utils import DataMixin


class MonthGraphFormView(DataMixin, FormView):
    """
    Рендерит шаблон с формой выбора типа диаграммы за месяц.
    """
    form_class = MonthGraphSelectForm
    template_name = 'month_graphs/month_graph_form.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transport_obj = None
        self.form_data = None

    def get_initial(self):
        """
        Возвращает словарь с исходными данными для формы.
        :return: словарь
        """
        initial = super(MonthGraphFormView, self).get_initial()
        self.transport_obj = self.get_transport(self.request)
        initial['username'] = self.request.user.username
        initial['transport'] = self.transport_obj.id
        initial['year'] = timezone.now().year
        return initial

    def build_and_save_graph(self, form_data: dict) -> str:
        """
        Вызывает методы постройки диаграммы, и возвращает относительный путь к файлу с диаграммой.
        :param form_data: данные из формы.
        :return: относительный путь к файлу.
        """
        builder = MonthGraphBuilder(**form_data)
        builder.build_and_save_graph(self.request)
        path = builder.get_user_dir() + '\\' + builder.get_file_name()
        return path

    def form_valid(self, form):
        """
        Обрабатывает данные из формы и отправляет их класс-строитель диаграмм. Возвращает функцию генерирующую шаблон.
        :param form: форма.
        :return: функция-генератор шаблона.
        """
        form_data = form.cleaned_data
        file = self.build_and_save_graph(form_data)
        context = {
            'file': file,
            'transport': self.transport_obj,
            'month': dict(MONTHS_NAMES)[form_data['month_number']].lower(),
            'year': form_data['year']
        }
        return render(self.request, 'month_graphs/month_graph.html', context=context)
