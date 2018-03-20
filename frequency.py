from calculations import Calculations
from graphing import Plotter
from data_object import DataObject
import numpy as np


class FrequencyDataObject(DataObject):

    def __init__(self, data):
        self.calculator = Calculations()
        self.plotter = Plotter()
        self.data = data
        self.unpack_data()
        self.chi_square = self.get_chi_square();
        self.expected_mode = self.get_mode(self.x)
        self.actual_mode = self.get_mode(self.y)
        self.probability_distribution = None  # self.get_probability_distribution();
        self.binomial_distribution = None  # self.get_binomial_distribution();
        self.vertical_bar_graphs = self.get_vertical_bar_graphs()
        self.horizontal_bar_graphs = self.get_horizontal_bar_graphs()
        self.pie_graphs = self.get_pie_charts()

    def unpack_x(self):
        x = []

        for row in self.data[1:]:
            x.append(float(row[1]))
        return x

    def unpack_y(self):
        y = []

        for row in self.data[1:]:
            y.append(float(row[2]))
        return y

    def unpack_data(self):

        self.x = FrequencyDataObject.unpack_x(self)
        self.y = FrequencyDataObject.unpack_y(self)

    def get_chi_square(self):

        return self.calculator.calculate_chi_square(self.x, self.y)

    def get_mode(self, data):

        return self.calculator.calculate_mode(data)

    def get_probability_distribution(self):

        # return self.calculator.calculate_probability_distribution();
        pass

    def get_binomial_distribution(self):

        # return self.calculator.calculate_binomial_distribution()
        pass

    def get_horizontal_bar_graphs(self):

        labels = self.data[0][1:]
        y_pos = np.arange(len(labels))
        bar_graphs = []

        for row in self.data[1:]:
            ax = self.plotter.make_horizontal_bar_chart(labels, y_pos, row)
            bar_graphs.append(ax)

        return bar_graphs

    def get_vertical_bar_graphs(self):

        labels = self.data[0][1:]
        x_pos = np.arange(len(labels))
        bar_graphs = []

        for row in self.data[1:]:
            ax = self.plotter.make_vertical_bar_chart(labels, x_pos, row)
            bar_graphs.append(ax)

        return bar_graphs

    def get_pie_charts(self):

        labels = self.data[0][1:]
        pie_graphs = []

        for row in self.data[1:]:
            ax = self.plotter.make_pie_chart(labels, row)
            pie_graphs.append(ax)

        return pie_graphs




