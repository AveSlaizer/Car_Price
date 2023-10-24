from abc import ABC

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

from matplotlib.axes import Axes

from .abstractions import YearGraph
from ...finance_expenses.models import FinanceExpense
from ...month_graphs.utils.month_graphs_settings import MONTHS_NAMES


class YearGraphKmPrice(YearGraph, ABC):
    """
    Строит график изменения стоимости километра пройденного на транспорте
    """
    matplotlib.use('agg')
    month_names = dict(MONTHS_NAMES)

    def __init__(self, transport_id: int, year: int):
        self.__transport_id = transport_id
        self.__year = year

    @staticmethod
    def get_verbose_name() -> str:
        """
        Возвращает русифицированное название. Используется для отображения в шаблоне.
        """
        return 'Стоимость 1-го км. в течении года'

    def build_and_save_graph(self, path: str):
        """
        Строит и сохраняет в .png файл диаграмму.
        :param path: Путь для сохранения файла.
        """
        queryset = self.__get_queryset()

        plt.rcParams.update({'figure.autolayout': True})
        fig, ax = plt.subplots(figsize=(7, 6))
        ax: Axes

        if queryset:
            data = self.__format_queryset_to_data(queryset)

            median_color = 'indigo'
            mean_color = 'darkgreen'

            ax.plot(data['month_names'], data['month_km_price'], c='crimson', lw=2, label='Динамика стоимости')
            ax.axhline(data['km_price_mean'], ls='--', c=mean_color, lw=2, label='Среднее арифметическое')
            ax.axhline(data['km_price_median'], ls=':', c=median_color, lw=2, label='Медианное значение')

            ax.set_title(f'Пробег за год: {data["odometer_summ"]} км., траты за год: {data["km_price_summ"]:.2f} р.',
                         loc='left', y=-0.3)
            ax.text(x=10, y=data['km_price_mean'], s=data['km_price_mean'], weight='bold', c='w',
                    backgroundcolor=mean_color)
            ax.text(x=0, y=data['km_price_median'], s=data['km_price_median'], weight='bold', c='w',
                    backgroundcolor=median_color)

            legend = ax.legend(loc='best', shadow=True)
            legend.get_frame()

            ax.grid()
            labels = ax.get_xticklabels()
            plt.setp(labels, rotation=45, ha='right')
            ax.set(xlabel='Месяц', ylabel='Стоимость 1-го км (р.)')

        else:
            data = 'Данные отсутствуют!'
            fig, ax = plt.subplots()
            ax: Axes
            ax.text(0.5, 0.5, data, ha='center', size=28)

        fig.savefig(path + '\\' + self.file_name)
        fig.clear()

    def __get_queryset(self) -> list[dict]:
        """
        Возвращает объект QuerySet преобразованный к списку словарей.
        :return: список словарей.
        """
        queryset = FinanceExpense.objects. \
            filter(transport_id=self.__transport_id, date__year=self.__year). \
            values('odometer', 'summ', 'date').order_by('date')
        return list(queryset)

    def __format_queryset_to_data(self, queryset: list) -> dict:
        """
        Обрабатывай данные содержащиеся в списке словарей и преобразует их в словарь.
        :param queryset: список словарей.
        :return: словарь.
        """
        # TODO добавить обработку не полных данных: пробег без трат, траты без пробега, месяца без записей
        # queryset = [{'odometer': 162871, 'summ': 1000.0, 'date': datetime.date(2022, 12, 31)}, ...]

        current_month = queryset[0]['date'].month
        temp_odometer = queryset[0]['odometer']
        temp_expenses_sum = 0
        data = {
            'month_odometer': [],
            'month_expenses': [],
            'month_names': [],
        }

        for item in queryset:
            if item['date'].month == current_month:
                temp_expenses_sum += item['summ']
            else:
                data['month_names'].append(self.month_names[current_month])
                current_month = item['date'].month

                data['month_odometer'].append(item['odometer'] - temp_odometer)
                data['month_expenses'].append(temp_expenses_sum)

                temp_odometer = item['odometer']
                temp_expenses_sum = item['summ']

        data['month_odometer'].append(queryset[-1]['odometer'] - temp_odometer)
        data['month_expenses'].append(temp_expenses_sum)
        data['month_names'].append(self.month_names[current_month])

        data['month_odometer'] = np.array(data['month_odometer'])
        data['month_expenses'] = np.array(data['month_expenses'])

        data['odometer_summ'] = np.sum(data['month_odometer'])
        data['km_price_summ'] = np.sum(data['month_expenses']).round(2)
        data['month_km_price'] = np.round(data.pop('month_expenses') / data.pop('month_odometer'), 2)
        data['km_price_median'] = np.median(data['month_km_price']).round(2)
        data['km_price_mean'] = np.mean(data['month_km_price']).round(2)

        return data
