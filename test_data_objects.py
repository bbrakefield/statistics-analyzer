import csv
import unittest

from frequency import FrequencyDataObject
from interval import IntervalDataObject


class TestDataObjects(unittest.TestCase):

    def setUp(self):

        try:
            with open("OrdinalDataTest.csv") as input_file:
                self.ordinalData = list(csv.reader(input_file))
        except IOError:
            print("Couldn't find OrdinalDataTest.csv!")

        try:
            with open("FrequencyDataTest.csv") as input_file:
                self.freqData = list(csv.reader(input_file))
        except IOError:
            print("Couldn't find FrequencyDataTest.csv!")

        try:
            with open("IntervalDataTest.csv") as input_file:
                self.intervalData = list(csv.reader(input_file))
        except IOError:
            print("Couldn't find IntervalDataTest.csv!")

    def test_freq_unpack_x(self):

        freqObject = FrequencyDataObject(self.freqData)
        self.assertEqual([445, 144, 225, 289, 316, 479, 217], freqObject.unpack_x())

    def test_freq_unpack_y(self):

        freqObject = FrequencyDataObject(self.freqData)
        self.assertEqual([371, 162, 188, 261, 277, 958, 186], freqObject.unpack_y())

    def test_freq_chi_square(self):
        freqObject = FrequencyDataObject(self.freqData)
        self.assertEqual(159.41524509442092, freqObject.chi_square)

    def test_freq_get_horizontal_bar_chart(self):

        freqObject = FrequencyDataObject(self.freqData)
        self.assertTrue(freqObject.get_horizontal_bar_graphs(self.freqData))

    def test_freq_get_vertical_bar_graph(self):

        freqObject = FrequencyDataObject(self.freqData)
        self.assertTrue(freqObject.get_vertical_bar_graphs(self.freqData))

    def test_freq_get_pie_graph(self):

        freqObject = FrequencyDataObject(self.freqData)
        self.assertTrue(freqObject.get_pie_charts(self.freqData))

    def test_interval_unpack_x(self):

        test_list = [83,66,89,74,57,63,91,74,61,94,57,81,79,84,62,58,73,75,59,80,59,
                     71,59,78,76,89,86,52,50,95,96,94,76,92,58,69,63,89,68,70,72,74,
                     67,96,57,78,66,78,63,90,58,78,73,60,76,85,67,73,56,78,78,78,84,
                     60,71,77,81,67,46,97,77,88,53,63,91,85,94,83,72,47,71,54,63,83,
                     80,59,79,69,76,67,74,73,63,66,74,69,64,77,58,53]

        intervalObject = IntervalDataObject(self.intervalData)
        self.assertEqual(test_list, intervalObject.unpack_x())

    def test_interval_unpack_y(self):

        test_list = [88,69,92,76,61,68,99,75,66,96,61,84,81,87,64,62,76,75,59,81,64,
                     76,59,81,76,92,88,54,50,98,100,96,77,92,58,69,63,92,73,76,72,74,
                     67,98,57,81,67,80,66,92,63,80,73,63,83,85,67,76,58,79,83,79,85,
                     63,72,83,81,67,50,97,77,89,53,63,94,87,98,87,73,50,78,58,67,85,
                     83,64,86,78,76,68,77,82,64,66,74,69,64,83,58,56]

        intervalObject = IntervalDataObject(self.intervalData)
        self.assertEqual(test_list, intervalObject.unpack_y())



