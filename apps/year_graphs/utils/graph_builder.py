import os

from .abstractions import YearGraph
from .year_graphs_settings import YEAR_GRAPH_UTILITIES
from config.settings import MEDIA_DIR


class YearGraphBuilder:
    """
    Управляет построением и сохранением диаграмм за определенный год
    """
    GRAPHS_DIR = MEDIA_DIR / 'images/graphs'
    __user_dir: str

    def __init__(self, username: str, transport_id: int, graph_type: str, year: int):
        self.__username = username
        self.__transport_id = transport_id
        self.__graph_type = graph_type
        self.__year = year
        self.__strategy = self.__set_strategy()

    def __set_strategy(self) -> YearGraph:
        """
        Устанавливает стратегию поведения
        """
        # FIXME
        strategy = YEAR_GRAPH_UTILITIES.get(self.__graph_type)(self.__transport_id, self.__year)
        return strategy

    def __set_user_dir(self):
        """
        Определяет, куда сохранится файл с диаграммой.
        """
        if self.__username not in os.listdir(self.GRAPHS_DIR):
            os.mkdir(self.GRAPHS_DIR / self.__username)
        self.__user_dir = str(self.GRAPHS_DIR / self.__username)

    def build_and_save_graph(self):
        """
        Строит и сохраняет диаграмму.
        """
        self.__set_user_dir()
        self.__strategy.build_and_save_graph(self.__user_dir)

    def get_relative_graph_path(self) -> str:
        """
        Возвращает относительный путь к файлу с диаграммой. Используется в шаблоне.
        """
        index = str(self.__user_dir).rfind('\\media\\')
        path = str(self.__user_dir)[index:]
        file_name = self.get_file_name()
        return path + '\\' + file_name

    def get_file_name(self) -> str:
        """
        Возвращает название файла с диаграммой
        """
        return self.__strategy.file_name
