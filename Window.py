import csv
import sys

from PyQt5.QtWidgets import QWidget, QMenuBar, QGridLayout, QRadioButton, QPushButton, QFileDialog, QApplication


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.data = []
        self.history = []
        self.data_flag = 0

        self.left = 200
        self.top = 200
        self.width = 350
        self.height = 200
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.menuBar = QMenuBar(self)
        menu = self.menuBar.addMenu("File")

        action = menu.addAction("Open Input File")
        action.triggered.connect(self.open_file)

        action = menu.addAction("Save As PNG")
        action.triggered.connect(self.save_file)

        layout = QGridLayout()
        self.setLayout(layout)

        radiobutton = QRadioButton("Interval")
        radiobutton.name = "Interval"
        radiobutton.toggled.connect(self.on_radio_button_toggled_interval)
        layout.addWidget(radiobutton, 0, 0)

        radiobutton = QRadioButton("Ordinal")
        radiobutton.name = "Ordinal"
        radiobutton.toggled.connect(self.on_radio_button_toggled_ordinal)
        layout.addWidget(radiobutton, 1, 0)

        radiobutton = QRadioButton("Frequency")
        radiobutton.setChecked(True)
        radiobutton.name = "Frequency"
        radiobutton.toggled.connect(self.on_radio_button_toggled_frequency)
        layout.addWidget(radiobutton, 2, 0)

        buttonInput = QPushButton('Open Input File', self)
        buttonInput.resize(150, 32)
        buttonInput.setToolTip('Input a data file')
        buttonInput.move(100, 100)
        buttonInput.clicked.connect(self.open_file)
        layout.addWidget(buttonInput, 1, 1)

        submitbutton = QPushButton('Submit')
        submitbutton.resize(70, 70)
        submitbutton.setToolTip('Submit')
        submitbutton.move(100, 300)
        submitbutton.clicked.connect(self.submitFun)
        layout.addWidget(submitbutton, 3, 1)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "CSV File (*.csv);;All Files (*)")
        self.import_data(filename)

    def import_data(self, filename):
        try:
            with open(filename) as input_file:
                self.data = list(csv.reader(input_file))
                self.history.append("File Opened: {}".format(filename))
        except IOError:
            print("Could not open file: {}!".format(filename))

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save a ", "",
                                                  "PNG File (*.png)")

        if self.plotter.last_figure_plotted is not None:
            self.plotter.last_figure_plotted.savefig(filename)

            self.plotter.last_figure_plotted.show()  # temp
        else:
            print("Nothing has been plotted; there is nothing to save!")

    def on_radio_button_toggled_ordinal(self):
        radiobutton = self.sender()

        if radiobutton.isChecked():
            self.data_flag = 1

    def on_radio_button_toggled_interval(self):
        radiobutton = self.sender()

        if radiobutton.isChecked():
            self.data_flag = 2

    def on_radio_button_toggled_frequency(self):
        radiobutton = self.sender()

        if radiobutton.isChecked():
            self.data_flag = 3

    def submitFun(self):
            print("")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    screen = Window()
    screen.show()

    sys.exit(app.exec_())
