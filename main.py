import atexit
import sys
from PyQt5.QtWidgets import *

from DataTypeDialogBox import *
from calculations import Calculations
from graphing import Plotter
from OrdinalDataScreen import Ui_Form2
from IntervalDataScreen import Ui_Form1
from FrequencyDataScreen import Ui_Form


class StatisticalAnalyzer(QMainWindow):

    def __init__(self):
        super().__init__()
        self.data = []
        self.csv_data = []
        self.text_report = []
        self.history = []
        self.last_figure_plotted = None

        self.calculator = Calculations()
        self.plotter = Plotter()

        self.title = "Statistical Analyzer"
        self.left = 200
        self.top = 200
        self.width = 1280
        self.height = 720

        self.initialize_ui()

    def initialize_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create Menu
        menu = self.menuBar().addMenu("File")

        action = menu.addAction("Save As...")
        action.triggered.connect(self.save_csv)

        action2 = menu.addAction("Generate Report...")
        action2.triggered.connect(self.write_report)
        # Show UI
        self.show()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "CSV File (*.csv);;All Files (*)")
        self.import_data(filename)

    def save_csv(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save a ", "",
                                                  "CSV File (*.csv)")

        with open(filename, 'w', newline='') as csv_file:

            writer = csv.writer(csv_file)
            for row in self.csv_data:
                writer.writerow(row)

    def write_report(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save a ", "",
                                                  "TXT File (*.txt)")

        with open(filename, 'w', newline='') as new_report:
            for item in self.text_report:
                new_report.write('%s\n' % item)

    def set_csv(self, csv_data):
        self.csv_data = csv_data

    def set_report(self, report):
        self.text_report = report

    def import_data(self, filename):
        try:
            with open(filename) as input_file:
                self.data = list(csv.reader(input_file))
                self.history.append("File Opened: {}".format(filename))
        except IOError:
            print("Could not open file: {}!".format(filename))

    def set_last_figure_plotted(self, plotted_figure):
        self.last_figure_plotted = plotted_figure

def exit_handler():
    try:
        with open("history.txt", "w") as file:
            try:
                file.writelines(application.history)
            except NameError:
                print("Could not write application history at exit!")
    except PermissionError:
        print("Could not write application history at exit because of a permissions error!")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    atexit.register(exit_handler)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    Dialog.exec_()
    typeFlag = ui.getType()
    application = StatisticalAnalyzer()
    if typeFlag == 1:
        inter = QtWidgets.QWidget()
        application.data = ui.getData()
        ui = Ui_Form1()
        ui.setupUi(inter, application.data, application)
        application.setCentralWidget(inter)
        sys.exit(app.exec_())
    elif typeFlag == 2:
        ordn = QtWidgets.QWidget()
        application.data = ui.getData()
        ui = Ui_Form2()
        ui.setupUi(ordn, application.data, application)
        application.setCentralWidget(ordn)
        sys.exit(app.exec_())
    elif typeFlag == 3:
        freq = QtWidgets.QWidget()
        application.data = ui.getData()
        ui = Ui_Form()
        ui.setupUi(freq, application.data, application)
        application.setCentralWidget(freq)
        sys.exit(app.exec_())


