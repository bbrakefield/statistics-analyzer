"""
Module that implements the logic for generating graphs
"""

# Authors: Brannon Brakefield
#          Jenna McCown

from PyQt5.QtWidgets import QDialog, QSizePolicy, QPushButton, QFileDialog, QLineEdit, QLabel
from PyQt5 import QtCore
from interval import IntervalDataObject
from frequency import FrequencyDataObject
from ordinal import OrdinalDataObject

import numpy as np
from scipy.stats import norm

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.pyplot import close

# =============================================================================
# Base window for showing graphs.
# =============================================================================

class App(QDialog):

    def __init__(self, Dialog, dataObject, whichObject, whichGraph, col_headers, row_headers):
        super().__init__()
        self.left = 625
        self.top = 200
        self.title = 'Graphs'
        self.width = 640
        self.height = 400
        self.whichObject = whichObject
        self.last_figure_plotted = None
        self.col_headers = col_headers
        self.row_headers = row_headers

        self.initUI(Dialog, dataObject, whichObject, whichGraph)


    def initUI(self, Dialog, dataObject, whichObject, whichGraph):

        Dialog.setObjectName("Dialog")
        Dialog.resize(0, 0)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.titleBox = QLineEdit(self)
        self.titleBox.setGeometry(QtCore.QRect(510, 280, 120, 25))
        self.titleBox.setObjectName("titleBox")

        self.m = PlotCanvas(self.col_headers, self.row_headers, self.titleBox, self, width=5, height=4)
        self.m.setDataObject(dataObject, whichObject, whichGraph)
        self.m.move(0, 0)

        button = QPushButton('Next\n>>', self)
        button.setToolTip('Next Graph')
        button.setStyleSheet('QPushButton {color: black;}')
        button.move(500, 0)
        button.resize(140, 80)
        button.clicked.connect(self.m.plot_next)

        button2 = QPushButton('Previous\n<<', self)
        button2.setToolTip('Previous Graph')
        button2.move(500, 90)
        button2.resize(140, 80)
        button2.clicked.connect(self.m.plot_previous)

        button3 = QPushButton('Save Graph As', self)
        button3.setToolTip('Save This Graph')
        button3.move(500, 180)
        button3.resize(140, 80)
        button3.clicked.connect(self.m.save_graph)

        _translate = QtCore.QCoreApplication.translate
        self.label1 = QLabel(self)
        self.label1.setGeometry(QtCore.QRect(510, 260, 80, 20))
        self.label1.setObjectName("label1")
        self.label1.setText(_translate("Dialog", "Change Title:"))

        button4 = QPushButton('Change Title', self)
        button4.setToolTip('Change Title')
        button4.move(500, 310)
        button4.resize(140, 50)
        button4.clicked.connect(self.m.changeTitle)

        self.show()

    def closeFigure(self):
        self.m.closeFigure()

    def closeEvent(self, event):
        self.closeFigure()
        close('all')
        close(self.m.fig)
        self.close()

# =============================================================================
# Canvas for plotting graphs on.
# =============================================================================


class PlotCanvas(FigureCanvas):

    def __init__(self, col_headers, row_headers, titleBox, parent=None, width=5, height=4, dpi=100):
        self.titleBox = titleBox
        self.last_figure_plotted = None
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.counter = 0
        self.col_headers = col_headers
        self.row_headers = row_headers

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def save_graph(self):
        """Save graph as jpg."""
        filename, _ = QFileDialog.getSaveFileName(self, "Save a ", "",
                                                  "JPG File (*.jpg)")
        self.figure.savefig(filename)


    def setDataObject(self, dataObject, whichObject, whichGraph):

        self.whichObject = whichObject
        self.whichGraph = whichGraph

        if whichObject == 1:
            self.object = IntervalDataObject(dataObject)
            self.plot_graph()

        elif whichObject == 2:
            self.object = FrequencyDataObject(dataObject)
            self.plot_graph()

        elif whichObject == 3:
            self.object = OrdinalDataObject(dataObject)
            self.plot_graph()

    def plot_next(self):
        if self.whichGraph != 4 and self.whichGraph != 5:
            if (self.counter < len(self.object.data)):
                self.counter = self.counter + 1
            else:
                self.counter = len(self.object.data)

            self.plot_graph()

    def plot_graph(self):

        if self.whichObject == 1:
            '''Interval'''
            if self.whichGraph == 1:
                graphTitle = "Vertical Bar Chart " + str(self.counter)
                self.plot_vertical_bar_chart(graphTitle)

            elif self.whichGraph == 2:
                graphTitle = "Horizontal Bar Chart " + str(self.counter)
                self.plot_horizontal_bar_chart(graphTitle)

            elif self.whichGraph == 3:
                graphTitle = "Pie Chart " + str(self.counter)
                self.plot_pie_chart(graphTitle)

            elif self.whichGraph == 4:
                graphTitle = "XY Graph "
                self.plot_xy_graph(graphTitle)

            elif self.whichGraph == 5:
                graphTitle = "Normal Distribution Curve  "
                self.plot_normal_distribution_curve(graphTitle)

        elif self.whichObject == 2:
            '''Frequncy'''
            if self.whichGraph == 1:
                graphTitle = "Vertical Bar Chart " + str(self.counter)
                self.plot_vertical_bar_chart(graphTitle)

            elif self.whichGraph == 2:
                graphTitle = "Horizontal Bar Chart " + str(self.counter)
                self.plot_horizontal_bar_chart(graphTitle)

            elif self.whichGraph == 3:
                graphTitle = "Pie Chart " + str(self.counter)
                self.plot_pie_chart(graphTitle)

        elif self.whichObject == 3:
            '''Ordinal'''
            if self.whichGraph == 1:
                graphTitle = "Vertical Bar Chart " + str(self.counter)
                self.plot_vertical_bar_chart(graphTitle)

            elif self.whichGraph == 2:
                graphTitle = "Horizontal Bar Chart " + str(self.counter)
                self.plot_horizontal_bar_chart(graphTitle)

            elif self.whichGraph == 3:
                graphTitle = "Pie Chart " + str(self.counter)
                self.plot_pie_chart(graphTitle)

            elif self.whichGraph == 4:
                graphTitle = "XY Graph "
                self.plot_xy_graph(graphTitle)

            # elif self.whichGraph == 5:
            #     self.plot_normal_distribution_curve()

    def changeTitle(self):
        title = self.titleBox.text()
        if self.whichGraph == 1:
            graphTitle = title
            self.plot_vertical_bar_chart(graphTitle)

        elif self.whichGraph == 2:
            graphTitle = title
            self.plot_horizontal_bar_chart(graphTitle)

        elif self.whichGraph == 3:
            graphTitle = title
            self.plot_pie_chart(graphTitle)

        elif self.whichGraph == 4:
            graphTitle = title
            self.plot_xy_graph(graphTitle)

        elif self.whichGraph == 5:
            graphTitle = title
            self.plot_normal_distribution_curve(graphTitle)

    def plot_previous(self):
        """Counter logic for plotting the previous graph."""

        if self.whichGraph is not 4 and self.whichGraph is not 5:
            if (self.counter > 1):
                self.counter = self.counter - 1
            else:
                self.counter = 1

            self.plot_graph()

    def plot_horizontal_bar_chart(self, title):
        """Plot horizontal bar chart on plot canvas. """

        self.fig.clear()
        labels = self.col_headers
        y_pos = np.arange(len(labels))
        row = list(map(int, self.object.data[self.counter - 1]))
        ax = self.figure.add_subplot(111)
        ax.barh(y_pos, row, align='center')
        # ax.set_title(self.row_headers[self.counter-1][0])  # Graph Title
        ax.set_title(title)
        self.draw()

    def plot_vertical_bar_chart(self, title):
        """Plot vertical bar chart on plot canvas"""

        self.fig.clear()
        labels = self.col_headers
        x_pos = np.arange(len(labels))
        row = list(map(int, self.object.data[self.counter - 1]))
        ax = self.figure.add_subplot(111)
        ax.bar(x_pos, row, color='blue')
        # ax.set_title(self.row_headers[self.counter-1][0])  # Graph Title
        ax.set_title(title)
        self.draw()

    def plot_pie_chart(self, title):
        """Plot pie chart on plotting canvas"""

        self.fig.clear()
        labels = self.col_headers
        row = list(map(int, self.object.data[self.counter-1]))
        sizes = []
        valsum = sum(row)
        for value in row:
            sizes.append(value / valsum)
        ax = self.figure.add_subplot(111)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')
        # ax.set_title(self.row_headers[self.counter-1][0])
        ax.set_title(title)
        self.draw()

    def plot_normal_distribution_curve(self, title):
        """Plot normal distribution curve on plotting canvas."""

        self.fig.clear()
        object = IntervalDataObject(self.object.data)
        mean = object.mean_x
        stdev = object.standard_dev_x

        x = np.linspace(mean - 3*stdev, mean + 3*stdev, 100)
        ax = self.figure.add_subplot(111)
        ax.plot(x, norm.pdf(x, mean, stdev))

        ax.set_title(title)
        self.draw()

    def plot_xy_graph(self, title):
        """Plot XY graph on plotting canvas."""

        self.fig.clear()
        values = []
        values2 = []
        sampleCount = len(self.object.data[1:])

        for row in self.object.data[1:]:
            values.append(int(row[0]))
            values2.append(int(row[1]))

        line1 = np.array(values)
        line2 = np.array(values2)

        t = np.arange(0, sampleCount, 1)

        ax = self.figure.add_subplot(111)
        ax.plot(t, line1)
        ax.plot(t, line2)
        # ax.xlabel("Sample #")
        # ax.ylabel("Frequency")
        ax.set_title(title)
        self.draw()

    def closeFigure(self):
        close('all')
