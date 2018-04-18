"""
Module containing the implementation of an ordinal data object.
"""

# Authors: Brannon Brakefield

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


    def unpack_a(self):

        a = []

        try:
            for row in self.data[0:]:
                if row[0] is not None:
                    a.append(float(row[0]))
        except IndexError:
            return None
        return a

    def unpack_b(self):

        b = []

        try:
            for row in self.data[0:]:
                if row[1] is not None:
                    b.append(float(row[1]))
        except IndexError:
            return None
        return b

    def unpack_c(self):

        c = []

        try:
            for row in self.data[1:]:
                if row[2] is not None:
                    c.append(float(row[2]))
        except IndexError:
            return None
        return c

    def unpack_d(self):

        d = []

        try:
            for row in self.data[1:]:
                if row[3] is not None:
                    d.append(float(row[3]))
        except IndexError:
            return None
        return d

    def unpack_e(self):

        e = []
        try:
            for row in self.data[1:]:
                if row[4] is not None:
                    e.append(float(row[4]))
        except IndexError:
            return None
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

