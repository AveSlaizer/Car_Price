from django.shortcuts import render
from django.utils import timezone

from .forms import YearGraphSelectForm
from .utils.graph_builder import YearGraphBuilder
from ..month_graphs.views import MonthGraphFormView


class YearGraphFormView(MonthGraphFormView):
    """
    Рендерит шаблон с формой выбора типа диаграммы за месяц.
    """
    form_class = YearGraphSelectForm
    template_name = 'year_graphs/year_graph_form.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transport_obj = None
        self.form_data = None

    def get_initial(self):
        """
        Возвращает словарь с исходными данными для формы.
        :return: словарь
        """
        initial = super(YearGraphFormView, self).get_initial()
        self.transport_obj = self.get_transport(self.request)
        initial['username'] = self.request.user.username
        initial['transport_id'] = self.transport_obj.id
        initial['year'] = timezone.now().year
        return initial

    def build_and_save_graph(self, form_data: dict) -> str:
        pass

    def form_valid(self, form):
        """
        Обрабатывает данные из формы и отправляет их класс-строитель диаграмм. Возвращает функцию генерирующую шаблон.
        :param form: форма.
        :return: функция-генератор шаблона.
        """
        form_data = form.cleaned_data
        print('form_data:', form_data)
        builder = YearGraphBuilder(**form_data)
        builder.build_and_save_graph()
        # file = self.build_and_save_graph(form_data)
        context = {
            # 'file': file,
            'transport': self.transport_obj,
            'year': form_data['year']
        }
        return render(self.request, 'year_graphs/year_graph.html', context=context)
