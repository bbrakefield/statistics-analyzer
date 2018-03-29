from abc import ABC, abstractmethod
from calculations import Calculations
from graphing import Plotter
import numpy as np


class DataObject(ABC):

    def __init__(self):
        self.calculator = Calculations()
        self.plotter = Plotter()
        self.x = []
        self.y = []

    @abstractmethod
    def unpack_data(self):
        pass

    def get_horizontal_bar_graphs(self, data):

        labels = data[0][1:]
        y_pos = np.arange(len(labels))
        bar_graphs = []

        for row in data[1:]:
            ax = self.plotter.make_horizontal_bar_chart(labels, y_pos, row)
            bar_graphs.append(ax)

        return bar_graphs

    def get_vertical_bar_graphs(self, data):

        labels = data[0][1:]
        x_pos = np.arange(len(labels))
        bar_graphs = []

        for row in data[1:]:
            ax = self.plotter.make_vertical_bar_chart(labels, x_pos, row)
            bar_graphs.append(ax)

        return bar_graphs

    def get_pie_charts(self, data):

        labels = data[0][1:]
        pie_graphs = []

        for row in data[1:]:
            ax = self.plotter.make_pie_chart(labels, row)
            pie_graphs.append(ax)

        return pie_graphs
