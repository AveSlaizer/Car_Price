from .abstractions import MonthGraph


class MonthBars(MonthGraph):

    @staticmethod
    def get_verbose_name() -> str:
        return 'Столбцы за месяц'
