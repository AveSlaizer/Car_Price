from apps.finance_expenses.graphs_utils.month_bars import MonthBars

GRAPH_UTILS_SETTINGS = {
    'MonthBars': {'verbose_name': 'Столбцы за месяц', 'class': MonthBars}
}

GRAPH_CHOICES = [(i[0], i[1].get('verbose_name')) for i in GRAPH_UTILS_SETTINGS.items()]


class GraphBuilder:
    UTILS_SETTINGS = GRAPH_UTILS_SETTINGS

    def __init__(self, util_name: str, **kwargs):
        self.strategy = self.set_strategy(util_name)
        self.kwargs = kwargs

    def set_strategy(self, util_name: str):
        return self.UTILS_SETTINGS.get(util_name).get('class')

    def build_graph(self):
        self.strategy(self.kwargs)
        pass


