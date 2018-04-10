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
        if whichObject == 1:
            self.intervalObject = IntervalDataObject(dataObject)
            self.intervalObject.unpack_data()
            self.plot_next()
            if whichGraph == 1:
                #display vertical Bar chart
                print("")
            elif whichGraph == 2:
                #display horizontal Bar chart
                print("")
            elif whichGraph == 3:
                # display pie chart
                print("")
            elif whichGraph == 4:
                # display xy graph
                print("")
            elif whichGraph == 5:
                # display normal curve graph
                print("")
        elif whichObject == 2:
            self.frequencyObject = FrequencyDataObject(dataObject)

            if whichGraph == 1:
                #display vertical Bar chart
                self.plot_next()

            elif whichGraph == 2:
                #display horizontal Bar chart
                print("")
            elif whichGraph == 3:
                # display pie chart
                print("")
        elif whichObject == 3:
            self.ordinalObject = OrdinalDataObject(dataObject)
            self.plot_next()
            if whichGraph == 1:
                #display vertical Bar chart
                print("")
            elif whichGraph == 2:
                #display horizontal Bar chart
                print("")
            elif whichGraph == 3:
                # display pie chart
                print("")
            elif whichGraph == 4:
                # display xy graph
                print("")
            elif whichGraph == 5:
                # display normal curve graph
                print("")

    def get_last_figure_plotted(self):
        print("")
        return self.last_figure_plotted

    def plot_next(self):

        # self.fig.clear()
        # data = [1, 2, 3, 4, 5]
        # ax = self.figure.add_subplot(111)
        # ax.plot(data, 'r-')
        # ax.set_title('') #Graph Title
        # self.draw()
        if self.whichObject == 2:
            if (self.counter < len(self.frequencyObject.data) - 1):
                self.counter = self.counter + 1
            else:
                self.counter = len(self.frequencyObject.data) - 1

            print(self.counter)
            labels = self.frequencyObject.data[0][1:]
            x_pos = np.arange(len(labels))

            self.fig.clear()
            row = self.frequencyObject.data[self.counter]
            print(row)
            values = [int(x) for x in row[1:]]
            print(values)
            ax = self.figure.add_subplot(111)
            ax.bar(x_pos, values, color='blue')
            ax.set_title(row[0])  # Graph Title
            #self.last_figure_plotted = self.fig.gca() #--??
            self.draw()

    def plot_previous(self):

        # self.fig.clear()
        # data = [1, 2, 3, 4, 5]
        # ax = self.figure.add_subplot(111)
        # ax.plot(data, 'r-')
        # ax.set_title('') #Graph Title
        # self.draw()
        if self.whichObject == 2:
            if(self.counter > 1):
                self.counter = self.counter - 1
            else:
                self.counter = 1

            print(self.counter)
            labels = self.frequencyObject.data[0][1:]
            x_pos = np.arange(len(labels))

            self.fig.clear()
            row = self.frequencyObject.data[self.counter]
            print(row)
            values = [int(x) for x in row[1:]]
            print(values)
            ax = self.figure.add_subplot(111)
            ax.bar(x_pos, values, color='blue')
            ax.set_title(row[0])  # Graph Title
            self.draw()

    def nextButtonHandler(self):
        #if statement for next graph
        print("")

    def prevButtonHandler(self):
        # if statement for next graph
        print("")

    def plot_horizontal_bar_chart(self, labels, y_pos, row):
        self.fig.clear()
        """
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
        #plot.close()

        #return z
        """

    def plot_vertical_bar_chart(self, labels, x_pos, row):
        self.fig.clear()
        """
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
        """

    def plot_pie_chart(self, labels, row):
        self.fig.clear()
        """
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
        """

    def plot_normal_distribution_curve(self):
        self.fig.clear()
        """
        # collect required calculations
        mean = 0
        stdev = 1

        # plot between -5 and 5 with .01 steps
        range = np.arange(-5, 5, 0.01)

        plot.plot(range, norm.pdf(range, mean, stdev))

        self.last_figure_plotted = plot.gcf()  # save plot before showing

        plot.show()
        """

    def plot_xy_graph(self):
        self.fig.clear()
        """
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
        """

