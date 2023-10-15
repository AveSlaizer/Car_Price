from .month_bars import MonthGraphBars

MONTH_GRAPH_UTILITIES = {
    'MonthGraphBars': MonthGraphBars,
}

MONTH_GRAPH_CHOICES = [(i, globals()[i].get_verbose_name()) for i in MONTH_GRAPH_UTILITIES.keys()]

MONTHS_NAMES = [
    (1, 'Январь'),
    (2, 'Февраль'),
    (3, 'Март'),
    (4, 'Апрель'),
    (5, 'Май'),
    (6, 'Июнь'),
    (7, 'Июль'),
    (8, 'Август'),
    (9, 'Сентябрь'),
    (10, 'Октябрь'),
    (11, 'Ноябрь'),
    (12, 'Декабрь'),
]
