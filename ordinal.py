from data_object import DataObject
import numpy as np


class OrdinalDataObject(DataObject):

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.unpack_data()
        self.x_mode = self.get_mode(self.x)
        self.y_mode = self.get_mode(self.y)
        self.x_median = self.get_median(self.x)
        self.y_median = self.get_median(self.y)
        self.sign_test = self.get_sign_test()
        self.rank_sum = self.get_rank_sum()
        self.percentile = None
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

        self.x = OrdinalDataObject.unpack_x(self)
        self.y = OrdinalDataObject.unpack_y(self)

    def get_mode(self, data):

        return self.calculator.calculate_mode(data)

    def get_median(self, data):

        return self.calculator.calculate_median(data)

    def get_sign_test(self):

        return self.calculator.calculate_sign_test(self.x, self.y)

    def get_rank_sum(self):

        return self.calculator.calculate_rank_sum_test(self.x, self.y)

    def get_percentile(self):

        # return self.calculator.calculate_percentiles(percentile, data)
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
