import csv
import matplotlib.pyplot as plot
import numpy as np
from scipy.stats import norm


class Plotter:

    def __init__(self):
        self.last_figure_plotted = None

        # these blocks are temporary.
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


    def make_horizontal_bar_chart(self, labels, y_pos, row):

        plot.rcdefaults()
        fig, ax = plot.subplots()
        values = [int(x) for x in row[1:]]
        ax.barh(y_pos, values, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        ax.invert_yaxis()
        ax.set_title(row[0])

        #self.last_figure_plotted = plot.gcf()  # save plot before showing

        z = plot.gcf()
        plot.close()

        return z

    def make_vertical_bar_chart(self, labels, x_pos, row):

        plot.rcdefaults()
        fig, ax = plot.subplots()
        values = [int(x) for x in row[1:]]
        ax.bar(x_pos, values, color='blue')
        ax.set_title(row[0])
        plot.xticks(x_pos, labels)
        ax.set_xticklabels(labels)

        #self.last_figure_plotted = plot.gcf()  # save plot before showing

        z = plot.gcf()
        plot.close()

        return z

    def make_pie_chart(self, labels, row):

        plot.rcdefaults()
        values = [int(x) for x in row[1:]]
        sizes = []
        valsum = sum(values)

        for value in values:
            sizes.append(value/valsum)

        fig, ax = plot.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        ax.set_title(row[0])

        # self.last_figure_plotted = plot.gcf()  # save plot before showing

        z = plot.gcf()
        plot.close()

        return z

    def make_normal_distribution_curve(self):
        # collect required calculations
        mean = 0
        stdev = 1

        # plot between -5 and 5 with .01 steps
        range = np.arange(-5, 5, 0.01)

        plot.plot(range, norm.pdf(range, mean, stdev))

        self.last_figure_plotted = plot.gcf()  # save plot before showing

        plot.show()

    def make_xy_graph(self):

        values = []
        values2 = []
        sampleCount = len(self.freqData[1:])

        for row in self.freqData[1:]:
            values.append(int(row[1]))
            values2.append(int(row[2]))

        line1 = np.array(values)
        line2 = np.array(values2)

        t = np.arange(0, sampleCount, 1)

        plot.plot(t, line1)
        plot.plot(t, line2)
        plot.xlabel("Sample #")
        plot.ylabel("Frequency")
        plot.title("XY Graph")

        self.last_figure_plotted = plot.gcf()  # save plot before showing

        plot.show()
