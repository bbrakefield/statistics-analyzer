import sys

from PyQt5.QtWidgets import QApplication, QDialog, QSizePolicy, QPushButton
from graphing import Plotter

from interval import IntervalDataObject
from frequency import FrequencyDataObject
from ordinal import OrdinalDataObject

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class App(QDialog):

    def __init__(self, Dialog, dataObject, whichObject, whichGraph):
        super().__init__()
        self.left = 625
        self.top = 200
        self.title = 'Graphs'
        self.width = 640
        self.height = 400
        self.whichObject = whichObject
        self.last_figure_plotted = None
        self.initUI(Dialog, dataObject, whichObject, whichGraph)

    def initUI(self, Dialog, dataObject, whichObject, whichGraph):

        Dialog.setObjectName("Dialog")
        Dialog.resize(0, 0)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=4)
        m.setDataObject(dataObject, whichObject, whichGraph)
        m.move(0, 0)

        button = QPushButton('Next\n>>', self)
        button.setToolTip('Next Graph')
        button.setStyleSheet('QPushButton {color: black;}')
        button.move(500, 0)
        button.resize(140, 100)
        button.clicked.connect(m.plot_next)

        button2 = QPushButton('Previous\n<<', self)
        button2.setToolTip('Previous Graph')
        button2.move(500, 110)
        button2.resize(140, 100)
        button2.clicked.connect(m.plot_previous)

        button3 = QPushButton('Save Graph As', self)
        button3.setToolTip('Save This Graph')
        button3.move(500, 220)
        button3.resize(140, 100)
        #button3.clicked.connect()

        self.show()

    def set_last_figure_plotted(self):
        #send new plot down the line
        print("")

    def get_last_figure_plotted(self):
        self.last_figure_plotted = self.m.get_last_figure_plotted
        return self.last_figure_plotted

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.last_figure_plotted = None
        self.plotter = Plotter()
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.counter = 0

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def setDataObject(self, dataObject, whichObject, whichGraph):

        self.whichObject = whichObject
        self.whichGraph = whichGraph

        if whichObject == 1:
            self.object = IntervalDataObject(dataObject)
            self.plot_next()

        elif whichObject == 2:
            self.object = FrequencyDataObject(dataObject)
            self.plot_next()

        elif whichObject == 3:
            self.object = OrdinalDataObject(dataObject)
            self.plot_next()


    def get_last_figure_plotted(self):
        print("")
        return self.last_figure_plotted

    def plot_next(self):

        if (self.counter < len(self.object.data) - 1):
            self.counter = self.counter + 1
        else:
            self.counter = len(self.object.data) - 1

        self.plot_graph()

    def plot_graph(self):

        print(self.whichObject)
        print(self.whichGraph)
        if self.whichObject == 1:
            '''Interval'''
            if self.whichGraph == 1:
                self.plot_vertical_bar_chart()

            elif self.whichGraph == 2:
                self.plot_horizontal_bar_chart()

            elif self.whichGraph == 3:
                self.plot_pie_chart()

            elif self.whichGraph == 4:
                self.plot_xy_graph()

            elif self.whichGraph == 5:
                self.plot_normal_distribution_curve()

        elif self.whichObject == 2:
            '''Frequncy'''
            if self.whichGraph == 1:
                self.plot_vertical_bar_chart()

            elif self.whichGraph == 2:
                self.plot_horizontal_bar_chart()

            elif self.whichGraph == 3:
                self.plot_pie_chart()

        elif self.whichObject == 3:
            '''Ordinal'''
            if self.whichGraph == 1:
                self.plot_vertical_bar_chart()

            elif self.whichGraph == 2:
                self.plot_horizontal_bar_chart()

            elif self.whichGraph == 3:
                self.plot_pie_chart()

            elif self.whichGraph == 4:
                self.plot_xy_graph()

            # elif self.whichGraph == 5:
            #     self.plot_normal_distribution_curve()

    def plot_previous(self):

        if self.whichObject == 2:
            if(self.counter > 1):
                self.counter = self.counter - 1
            else:
                self.counter = 1

        self.plot_graph()

    def nextButtonHandler(self):
        #if statement for next graph
        print("")

    def prevButtonHandler(self):
        # if statement for next graph
        print("")

    def plot_horizontal_bar_chart(self):

        self.fig.clear()
        print(self.counter)
        labels = self.object.data[0][1:]
        y_pos = np.arange(len(labels))
        row = self.object.data[self.counter]
        print(row)
        values = [int(x) for x in row[1:]]
        print(values)
        ax = self.figure.add_subplot(111)
        ax.barh(y_pos, values, align='center')
        ax.set_title(row[0])  # Graph Title
        self.draw()

    def plot_vertical_bar_chart(self):

        print(self.counter)
        labels = self.object.data[0][1:]
        x_pos = np.arange(len(labels))
        self.fig.clear()
        row = self.object.data[self.counter]
        print(row)
        values = [int(x) for x in row[1:]]
        print(values)
        ax = self.figure.add_subplot(111)
        ax.bar(x_pos, values, color='blue')
        ax.set_title(row[0])  # Graph Title
        # self.last_figure_plotted = self.fig.gca() #--??
        self.draw()

    def plot_pie_chart(self):

        print(self.counter)
        labels = self.object.data[0][1:]
        x_pos = np.arange(len(labels))
        self.fig.clear()
        row = self.object.data[self.counter]
        print(row)
        values = [int(x) for x in row[1:]]
        sizes = []
        valsum = sum(values)
        for value in values:
            sizes.append(value / valsum)

        ax = self.figure.add_subplot(111)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        ax.set_title(row[0])
        self.draw()

    def plot_normal_distribution_curve(self):

        self.fig.clear()
        object = IntervalDataObject(self.object.data)
        mean = object.mean_x
        stdev = object.standard_dev_x

        x = np.linspace(mean - 3*stdev, mean + 3*stdev, 100)
        ax = self.figure.add_subplot(111)
        ax.plot(x, norm.pdf(x, mean, stdev))

        self.draw()

    def plot_xy_graph(self):
        self.fig.clear()
        values = []
        values2 = []
        sampleCount = len(self.object.data[1:])

        for row in self.object.data[1:]:
            values.append(int(row[1]))
            values2.append(int(row[2]))

        line1 = np.array(values)
        line2 = np.array(values2)

        t = np.arange(0, sampleCount, 1)

        ax = self.figure.add_subplot(111)
        ax.plot(t, line1)
        ax.plot(t, line2)
        # ax.xlabel("Sample #")
        # ax.ylabel("Frequency")
        ax.set_title("XY Graph")
        self.draw()


