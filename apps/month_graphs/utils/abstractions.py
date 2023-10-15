from abc import ABC, abstractmethod


class MonthGraph(ABC):
    period = 'month'
    file_name = 'month_graph.png'

    @staticmethod
    @abstractmethod
    def get_verbose_name() -> str:
        raise NotImplementedError

    @abstractmethod
    def build_and_save_graph(self, path: str):
        raise NotImplementedError
