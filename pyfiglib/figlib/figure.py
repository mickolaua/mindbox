import importlib.util
import os
import pkgutil
from abc import ABC, abstractmethod
from typing import TypedDict

CUR_DIR = os.path.dirname(__file__)
PLUGIN_FOLDER = os.path.join(os.path.dirname(__file__), "plugins")

class FigureParams(TypedDict):
    ...


class Figure(ABC):
    @abstractmethod
    def __assign_params__(self, params: FigureParams) -> FigureParams:
        ...

    def create(self, params: FigureParams):
        self.__params = self.__assign_params__(params)

    @property
    @abstractmethod
    def area(self) -> float:
        ...


def load_plugins(plugin_folder: str = PLUGIN_FOLDER) -> list[Figure]:
    plugins = []

    for importer, package_name, _  in pkgutil.iter_modules([plugin_folder]):
        # module_info = importlib.import_module(f"{plugin_folder}.{module.name}")
        # full_name = f"{os.path.abspath(os.path.dirname(plugin_folder))}.{package_name}"
        module = importer.find_module(package_name).load_module(package_name)
        for name, cls_ in module.__dict__.items():
            if isinstance(cls_, type) and issubclass(cls_, Figure) and cls_ is not Figure:
                plugins.append(cls_())
    
    return plugins
