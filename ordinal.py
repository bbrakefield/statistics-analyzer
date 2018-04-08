from data_object import DataObject
import numpy as np


class OrdinalDataObject(DataObject):

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.unpack_data()

        self.a_mode = self.get_mode(self.a)
        self.b_mode = self.get_mode(self.b)
        self.c_mode = self.get_mode(self.c)
        self.d_mode = self.get_mode(self.d)
        self.e_mode = self.get_mode(self.e)

        self.a_median = self.get_median(self.a)
        self.b_median = self.get_median(self.b)
        self.c_median = self.get_median(self.c)
        self.d_median = self.get_median(self.d)
        self.e_median = self.get_median(self.e)

        self.sign_test = self.get_sign_test()
        self.rank_sum = self.get_rank_sum()
        self.vertical_bar_graphs = self.get_vertical_bar_graphs(self.data)
        self.horizontal_bar_graphs = self.get_horizontal_bar_graphs(self.data)
        self.pie_graphs = self.get_pie_charts(self.data)

    def unpack_a(self):

        a = []

        for row in self.data[1:]:
            a.append(float(row[1]))
        return a

    def unpack_b(self):

        b = []

        for row in self.data[1:]:
            b.append(float(row[2]))
        return b

    def unpack_c(self):

        c = []

        for row in self.data[1:]:
            c.append(float(row[3]))
        return c

    def unpack_d(self):

        d = []

        for row in self.data[1:]:
            d.append(float(row[4]))
        return d

    def unpack_e(self):

        e = []

        for row in self.data[1:]:
            e.append(float(row[5]))
        return e

    def unpack_data(self):

        self.a = OrdinalDataObject.unpack_a(self)
        self.b = OrdinalDataObject.unpack_b(self)
        self.c = OrdinalDataObject.unpack_c(self)
        self.d = OrdinalDataObject.unpack_d(self)
        self.e = OrdinalDataObject.unpack_e(self)

    def get_mode(self, data):

        return self.calculator.calculate_mode(data)

    def get_median(self, data):

        return self.calculator.calculate_median(data)

    def get_sign_test(self):

        return self.calculator.calculate_sign_test(self.a, self.b)

    def get_rank_sum(self):

        return self.calculator.calculate_rank_sum_test(self.a, self.b)

    def get_percentile(self, desiredpercentile):
        return self.calculator.calculate_percentiles(desiredpercentile, self.data)
        pass

