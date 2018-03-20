import unittest

import calculations


class TestCalculations(unittest.TestCase):

    def setUp(self):

        self.calc = calculations.Calculations()

    def test_calculate_mean(self):

        data = [100, 234, 253, 112, 467]
        self.assertEqual(233.2, self.calc.calculate_mean(data))

    def test_calculate_mode(self):

        # test data with reoccurring values.
        data = [6, 3, 9, 6, 6, 5, 9, 3]
        self.assertEqual(6, self.calc.calculate_mode(data))

        # test data set that shouldn't have a mean.
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(None, self.calc.calculate_mode(data))

    def test_calculate_median(self):

        # test list with odd number of values.
        data = [100, 234, 253, 112, 467]
        self.assertEqual(234, self.calc.calculate_median(data))

        # test list with even number of values.
        data = [100, 234, 253, 112, 467, 874]
        self.assertEqual(243.5, self.calc.calculate_median(data))

    def test_calculate_standard_deviation(self):

        data = [5, 20, 40, 80, 100]
        self.assertEqual(40.06245124802026, self.calc.calculate_standard_deviation(data))

    def test_calculate_variance(self):

        data = [5, 20, 40, 80, 100]
        self.assertEqual(1605, self.calc.calculate_variance(data))

    def test_calculate_coefficient_of_variance(self):

        data = [5, 20, 40, 80, 100]
        self.assertEqual(0.8176010458779644, self.calc.calculate_coefficient_of_variance(data))

    def test_calculate_covariance(self):

        x = [5, 20, 40, 80, 100]
        y = [10, 24, 33, 54, 10]
        self.assertEqual(187.74999999999997, self.calc.calculate_covariance(x, y))

    def test_calculate_pearson_correlation(self):

        x = [5, 20, 40, 80, 100]
        y = [10, 24, 33, 54, 10]
        self.assertEqual(0.25521056226004085, self.calc.calculate_pearson_correlation(x, y))

    def test_calculate_least_square_line(self):

        x = [5, 20, 40, 80, 100]
        y = [10, 24, 33, 54, 10]
        self.assertEqual("Y = 20.4681 + (0.1170)X", self.calc.calculate_least_square_line(x, y))

    def test_calculate_percentiles(self):
        pass

    def test_calculate_probability_distribution(self):
        pass

    def test_calculate_binomial_distribution(self):
        pass

    def test_calculate_chi_square(self):
        x = [445, 144, 225, 289, 316, 479, 217]
        y = [371, 162, 188, 261, 277, 958, 186]

        self.assertEqual(159.41524509442092, self.calc.calculate_chi_square(x, y))

    def test_calculate_correlation_coefficient(self):

        x = [445, 144, 144, 225, 289, 316, 479, 217]
        y = [371, 162, 188, 222, 261, 277, 958, 186]
        self.assertEqual(0.7998246086998627, self.calc.calculate_correlation_coefficient(x, y))

    def test_calculate_sign_test(self):
        x = [443, 421, 436, 376, 458, 408, 422, 431, 459, 369, 360, 431, 403, 436, 376, 370, 443]
        y = [57, 352, 587, 415, 458, 424, 463, 583, 432, 379, 370, 584, 422, 587, 415, 419, 57]
        self.assertEqual("Reject", self.calc.calculate_sign_test(x, y))

    def test_calculate_rank_sum_test(self):

        x = [34.5, 37.5, 39.5, 40.0, 45.5, 47.0, 47.0, 47.5, 48.7, 49.0, 51.0, 51.0, 52.0, 53.0, 54.0, 54.0, 55.0, 56.5, 57.0, 58.5, 58.5]
        y = [28.0, 35.0, 37.0, 37.0, 43.5, 44.0, 45.5, 46.0, 48.0, 48.3, 48.7, 51.0, 52.0, 53.0, 53.0, 54.0, 54.0, 55.0]
        self.assertEqual(-1.3240749990746759, self.calc.calculate_rank_sum_test(x, y))

    def test_calculate_spearman_rank(self):

        x = [445, 144, 144, 225, 289, 316, 479, 217]
        y = [371, 162, 188, 222, 261, 277, 958, 186]
        self.assertEqual(0.958101009530607, self.calc.calculate_spearman_rank(x, y))

    def test_get_rank(self):

        data = [445, 144, 225, 289, 316, 479, 217]
        self.assertEqual([6, 1, 3, 4, 5, 7, 2], self.calc.get_rank(data))
