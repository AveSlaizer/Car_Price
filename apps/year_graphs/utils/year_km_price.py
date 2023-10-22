from abc import ABC

import matplotlib.pyplot as plt
import matplotlib

from .abstractions import YearGraph
from ...garage.models import Transport
from ...finance_expenses.models import FinanceExpense


class YearGraphKmPrice(YearGraph, ABC):
    """
    Строит график изменения стоимости километра пройденного на транспорте
    """
    # matplotlib.use('agg')
    matplotlib.use('TkAgg')

    def __init__(self, transport_id: int, year: int):
        self.__transport_id = transport_id
        self.__year = year

    @staticmethod
    def get_verbose_name() -> str:
        return 'Стоимость 1-го км. в течении года'

    def build_and_save_graph(self, path: str):
        """
        Строит и сохраняет в .png файл диаграмму.
        :param path: Путь для сохранения файла.
        """
        self.format_queryset_to_data()

    def get_queryset(self):
        queryset = FinanceExpense.objects. \
            filter(transport_id=self.__transport_id, date__year=self.__year).\
            values('odometer', 'summ', 'date').order_by('date')
        return queryset

    def format_queryset_to_data(self):
        queryset = self.get_queryset()

        current_month = 1
        temp_odometer = 0
        temp_odometer_sum = 0
        temp_expenses = 0
        data = {
            'month_odometer': [],
            'month_expenses': []
        }
        for item in queryset:
            if temp_odometer == 0:

            if item['date'].month == current_month:
                temp_odometer_sum += item['odometer']
                temp_expenses += item['summ']
            else:
                current_month = item['date'].month
                data['month_odometer'].append(temp_odometer_sum)
                data['month_expenses'].append(temp_expenses)
                temp_odometer_sum = item['odometer']
                temp_expenses = item['summ']
        else:
            data['month_odometer'].append(temp_odometer_sum)
            data['month_expenses'].append(temp_expenses)
        print(data)

