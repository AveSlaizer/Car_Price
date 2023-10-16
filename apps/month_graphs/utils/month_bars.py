from abc import ABC

import matplotlib.pyplot as plt
import matplotlib

from .abstractions import MonthGraph


class MonthGraphBars(MonthGraph, ABC):
    """
    Строит столбчатую диаграмму.
    """
    matplotlib.use('agg')
    cats_and_colors = {
        'Штрафы': 'blue',
        'Тюнинг': 'orange',
        'Страховка': 'green',
        'Ремонт': 'red',
        'Пошлина': 'purple',
        'Плановое': 'brown',
        'ТО': 'pink',
        'Налог': 'gray',
        'Заправка': 'olive',
        'Другое': 'cyan',
        'Детейлинг': 'crimson',
    }

    def __init__(self, data: dict[str, float]):
        self.__colors = [self.cats_and_colors[i] for i in data.keys()]
        self.__group_data = list(data.values())
        self.__group_names = [i[0] + '\n' + str(i[1]) for i in data.items()]

    @staticmethod
    def get_verbose_name() -> str:
        """
        Возвращает русифицированное название. Используется для отображения в шаблоне.
        """
        return 'Столбцы за месяц'

    def build_and_save_graph(self, path: str):
        """
        Строит и сохраняет в .png файл диаграмму.
        :param path: Путь для сохранения файла.
        """
        plt.rcParams.update({'figure.autolayout': True})
        plt.barh(self.__group_names, self.__group_data, color=self.__colors)
        plt.title(f'Общая сумма: {sum(self.__group_data)}р.', fontsize=16)
        plt.savefig(str(path) + '\\' + self.file_name)
        plt.close()
