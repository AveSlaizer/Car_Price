from .year_km_price import YearGraphKmPrice

# Словарь с названием и ссылкой на класс-построитель месячных диаграмм
YEAR_GRAPH_UTILITIES = {
    'YearGraphKmPrice': YearGraphKmPrice,
}

# Список кортежей для отображения в форме в шаблоне. Строится автоматически.
year_graphs_choice = [(i, globals()[i].get_verbose_name()) for i in YEAR_GRAPH_UTILITIES.keys()]
