import os

from django.db.models import Sum, QuerySet

from apps.finance_expenses.models import FinanceExpense
from apps.garage.models import Transport
from .abstractions import MonthGraph
from .month_graphs_settings import MONTH_GRAPH_UTILITIES
from config.settings import MEDIA_DIR


class MonthGraphBuilder:
    GRAPHS_DIR = MEDIA_DIR / 'images/graphs'
    __user_dir: str

    def __init__(self, username: str, transport: Transport, graph_type: str, year: int, month_number: int):
        self.__username = username
        self.__transport = transport
        self.__graph_type = graph_type
        self.__year = year
        self.__month_number = month_number
        self.__strategy = self.__set_strategy()

    def __get_queryset(self) -> QuerySet:
        queryset = FinanceExpense.objects.values('expense_type'). \
            filter(date__year=self.__year,
                   date__month=self.__month_number,
                   transport=self.__transport).annotate(total=Sum('summ'))
        return queryset

    def __get_formatted_queryset_data(self) -> dict[str, float]:
        data = dict([item.values() for item in self.__get_queryset()])
        return data

    def __set_strategy(self) -> MonthGraph:
        return MONTH_GRAPH_UTILITIES.get(self.__graph_type)(self.__get_formatted_queryset_data())

    def __set_user_dir(self, request):
        if request.user.username not in os.listdir(self.GRAPHS_DIR):
            os.mkdir(self.GRAPHS_DIR / request.user.username)
        self.__user_dir = self.GRAPHS_DIR / request.user.username

    def build_and_save_graph(self, request):
        self.__set_user_dir(request)
        self.__strategy.build_and_save_graph(self.__user_dir)

    def get_user_dir(self) -> str:
        index = str(self.__user_dir).rfind('\\media\\')
        path = str(self.__user_dir)[index:]
        return path

    def get_file_name(self) -> str:
        return self.__strategy.file_name
