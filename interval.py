from data_object import DataObject
import numpy as np


class IntervalDataObject(DataObject):

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.median_x = self.get_median(self.x)
        self.median_y = self.get_median(self.y)
        self.unpack_data()
        self.mean_x = self.get_mean(self.x)
        self.mean_y = self.get_mean(self.y)
        self.mode_x = self.get_mode(self.x)
        self.mode_y = self.get_mode(self.y)
        self.standard_dev_x = self.get_standard_dev(self.x)
        self.standard_dev_y = self.get_standard_dev(self.y)
        self.coefficient_of_var_x = self.get_coefficient_of_variance(self.x)
        self.coefficient_of_var_y = self.get_coefficient_of_variance(self.y)
        self.pearson = self.get_pearson_correlation()
        self.correlation_coeff = self.get_correlation_coefficient()
        self.variance_x = self.get_variance(self.x)
        self.variance_y = self.get_variance(self.y)
        self.covariance = self.get_covariance()
        self.least_square = self.get_least_square_line()
        self.rank_sum = self.get_rank_sum()
        self.spearman = self.get_spearman_rank()
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

        self.x = IntervalDataObject.unpack_x(self)
        self.y = IntervalDataObject.unpack_y(self)

    def get_median(self, data):

        return self.calculator.calculate_median(data)

    def get_mean(self, data):

        return self.calculator.calculate_mean(data)

    def get_mode(self, data):

        return self.calculator.calculate_mode(data)

    def get_standard_dev(self, data):

        return self.calculator.calculate_standard_deviation(data)

    def get_percentileX(self, desiredpercent):

        return self.calculator.calculate_percentiles(desiredpercent, self.x)

    def get_percentileY(self, desiredpercent):

        return self.calculator.calculate_percentiles(desiredpercent, self.y)

    def get_coefficient_of_variance(self, data):

        return self.calculator.calculate_coefficient_of_variance(data)

    def get_pearson_correlation(self):

        return self.calculator.calculate_pearson_correlation(self.x, self.y)

    def get_correlation_coefficient(self):

        return self.calculator.calculate_correlation_coefficient(self.x, self.y)

    def get_variance(self, data):

        return self.calculator.calculate_variance(data)

    def get_covariance(self):

        return self.calculator.calculate_covariance(self.x, self.y)

    def get_least_square_line(self):

        return self.calculator.calculate_least_square_line(self.x, self.y)

    def get_spearman_rank(self):

        return self.calculator.calculate_spearman_rank(self.x, self.y)

    def get_rank_sum(self):

        return self.calculator.calculate_rank_sum_test(self.x, self.y)
