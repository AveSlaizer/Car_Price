from .month_bars import MonthGraphBars

# Словарь с названием и ссылкой на класс-построитель месячных диаграмм
MONTH_GRAPH_UTILITIES = {
    'MonthGraphBars': MonthGraphBars,
}

# Список кортежей для отображения в форме в шаблоне. Строится автоматически.
month_graph_choices = [(i, globals()[i].get_verbose_name()) for i in MONTH_GRAPH_UTILITIES.keys()]

# Номера и названия месяцев для отображения в форме в шаблоне.
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
