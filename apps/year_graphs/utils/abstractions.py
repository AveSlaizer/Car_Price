from abc import ABC, abstractmethod


class YearGraph(ABC):
    period = 'year'
    file_name = 'year_graph.png'

    @staticmethod
    @abstractmethod
    def get_verbose_name() -> str:
        raise NotImplementedError

    @abstractmethod
    def build_and_save_graph(self, path: str):
        raise NotImplementedError
