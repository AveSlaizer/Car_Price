from abc import ABC

import matplotlib.pyplot as plt
import matplotlib

from .abstractions import MonthGraph


class MonthGraphBars(MonthGraph, ABC):
    matplotlib.use('agg')

    def __init__(self, data: dict[str, float]):
        self.__group_data = list(data.values())
        self.__group_names = list(data.keys())

    @staticmethod
    def get_verbose_name() -> str:
        return 'Столбцы за месяц'

    def __add_labels(self):
        for i in range(len(self.__group_names)):
            plt.text(self.__group_data[i] + 150, i-0.25, str(self.__group_data[i]), color='black', ha='center', rotation='vertical')

    def build_and_save_graph(self, path: str):
        # print(self.__group_names)
        # print(self.__group_data)
        plt.rcParams.update({'figure.autolayout': True})
        plt.barh(self.__group_names, self.__group_data)
        plt.title(f'Общая сумма: {sum(self.__group_data)}р.', fontsize=16)
        self.__add_labels()
        plt.savefig(str(path) + '\\' + self.file_name)
        plt.close()
