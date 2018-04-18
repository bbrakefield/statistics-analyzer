"""
Module containing the implementation of an frequency data object.
"""

# Authors: Brannon Brakefield

from data_object import DataObject

# =============================================================================
# Frequency data object
# =============================================================================


class FrequencyDataObject(DataObject):
    """Frequency data object that contains all relevant statistical calculations on
    imported data.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.unpack_data()
        self.chi_square = self.get_chi_square()
        self.expected_mode = self.get_mode(self.x)
        self.actual_mode = self.get_mode(self.y)

    def unpack_x(self):
        """Extract first column from data frame."""

        x = []
        try:
            for row in self.data[0:]:
                if row[0] is not None:
                    x.append(float(row[0]))
        except IndexError:
            return None
        return x

    def unpack_y(self):
        """Extract second column from data frame."""

        y = []
        try:
            for row in self.data[0:]:
                if row[1] is not None:
                    y.append(float(row[1]))
        except IndexError:
            return None
        return y

    def unpack_data(self):
        """Extract data from data frame and flatten into singular lists."""

        self.x = FrequencyDataObject.unpack_x(self)
        self.y = FrequencyDataObject.unpack_y(self)

    def get_chi_square(self):

        return self.calculator.calculate_chi_square(self.x, self.y)

    def get_mode(self, data):

        return self.calculator.calculate_mode(data)

    def get_probability_distribution(self, successes, trials):

        return self.calculator.calculate_probability_distribution(successes, trials)

    def get_binomial_distribution(self, probSuccess, trials, successes):

        return self.calculator.calculate_binomial_distribution(probSuccess, trials, successes)






