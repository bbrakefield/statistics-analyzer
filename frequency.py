from data_object import DataObject
import numpy as np


class FrequencyDataObject(DataObject):

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.unpack_data()
        self.chi_square = self.get_chi_square()
        self.expected_mode = self.get_mode(self.x)
        self.actual_mode = self.get_mode(self.y)
        self.probability_distribution = None  # self.get_probability_distribution();
        self.binomial_distribution = None  # self.get_binomial_distribution();
        self.vertical_bar_graphs = self.get_vertical_bar_graphs(self.data)
        self.horizontal_bar_graphs = self.get_horizontal_bar_graphs(self.data)
        self.pie_graphs = self.get_pie_charts(self.data)

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





