from abc import ABC, abstractmethod
from calculations import Calculations
from graphing import Plotter


class DataObject(ABC):

    def __init__(self):
        self.calculator = Calculations()
        self.plotter = Plotter()
        self.x = []
        self.y = []

    @abstractmethod
    def unpack_data(self):
        pass
