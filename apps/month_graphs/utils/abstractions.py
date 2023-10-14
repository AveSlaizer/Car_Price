from abc import ABC, abstractmethod


class MonthGraph(ABC):
    period = 'month'

    @abstractmethod
    def get_verbose_name(self) -> str:
        raise NotImplementedError
