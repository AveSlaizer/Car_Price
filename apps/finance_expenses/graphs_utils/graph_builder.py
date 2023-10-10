from apps.finance_expenses.graphs_utils.month_bars import MonthBars

GRAPH_UTILS_SETTINGS = {
    'MonthBars': {'verbose_name': 'Столбцы за месяц', 'class': MonthBars, 'period': 'month'},
}
# TODO Вывести настройки классов в классы
# TODO Вывести константы в отдельный модуль

MONTH_GRAPH_CHOICES = [(i[0], i[1].get('verbose_name')) for i in GRAPH_UTILS_SETTINGS.items() if
                       i[1].get('period') == 'month']


YEAR_GRAPH_CHOICES = [(i[0], i[1].get('verbose_name')) for i in GRAPH_UTILS_SETTINGS.items() if
                      i[1].get('period') == 'year']


class GraphBuilder:

    def __init__(self, util_name: str, **kwargs):
        self.strategy = self.set_strategy(util_name)
        self.kwargs = kwargs

    @staticmethod
    def set_strategy(util_name: str):
        return GRAPH_UTILS_SETTINGS.get(util_name).get('class')

    def build_graph(self):
        self.strategy(self.kwargs)
        pass
