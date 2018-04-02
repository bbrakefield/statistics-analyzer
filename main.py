import atexit
import sys
from PyQt5.QtWidgets import *

from DataTypeDialogBox import *
from calculations import Calculations
from graphing import Plotter
from OrdinalDataScreen import Ui_Form2
from IntervalDataScreen import Ui_Form1
from FrequencyDataScreen import Ui_Form
from frequency import FrequencyDataObject

class StatisticalAnalyzer(QMainWindow):

    def __init__(self):
        super().__init__()
        self.data = []
        self.history = []

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

        action = menu.addAction("Open Input File")
        action.triggered.connect(self.open_file)

        action = menu.addAction("Save As PNG")
        action.triggered.connect(self.save_file)

        # Show UI
        self.show()

    def on_radio_button_toggled(self):
        radiobutton = self.sender()

        if radiobutton.isChecked():
            print("You selected %s" % radiobutton.country)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "CSV File (*.csv);;All Files (*)")

        self.import_data(filename)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save a ", "",
                                                  "PNG File (*.png)")

        if self.plotter.last_figure_plotted is not None:
            self.plotter.last_figure_plotted.savefig(filename)

            self.plotter.last_figure_plotted.show()  # temp
        else:
            print("Nothing has been plotted; there is nothing to save!")

    def print_data(self):
        for i, line in enumerate(self.data):
            print("row %s. %s" % (i + 1, line))

    def import_data(self, filename):
        try:
            with open(filename) as input_file:
                self.data = list(csv.reader(input_file))
                self.history.append("File Opened: {}".format(filename))
        except IOError:
            print("Could not open file: {}!".format(filename))

    def button_mean_event(self):
        temp = self.calculator.calculate_mean(self.data)
        self.history.append("Mean Calculated: " + str(temp))

    def button_median_event(self):
        temp = self.calculator.calculate_median(self.data)
        self.history.append("Median Calculated: " + str(temp))

    def button_mode_event(self):
        temp = self.calculator.calculate_mode(self.data)
        self.history.append("Mode Calculated: " + str(temp))

    def button_standard_deviation_event(self):
        temp = self.calculator.calculate_standard_deviation(self.data)
        self.history.append("Standard Deviation Calculated: " + str(temp))

    def button_variance_event(self):
        temp = self.calculator.calculate_variance(self.data)
        self.history.append("Variance Calculated: " + str(temp))

    def button_coefficient_of_variance(self):
        temp = self.calculator.calculate_coefficient_of_variance(self.data)
        self.history.append("Coefficient of Variance Calculated: " + str(temp))

    def button_percentiles_event(self):
        temp = self.calculator.calculate_percentiles(self.data)
        self.history.append("Percentiles Calculated: " + str(temp))

    def button_probability_distribution_event(self):
        temp = self.calculator.calculate_probability_distribution(self.data)
        self.history.append("Probability Distribution Calculated: " + str(temp))

    def button_binomial_distribution_event(self):
        temp = self.calculator.calculate_binomial_distribution(self.data)
        self.history.append("Binomial Distribution Calculated: " + str(temp))

    def button_least_square_line_event(self):
        temp = self.calculator.calculate_least_square_line(self.data)
        self.history.append("Least Square Line Calculated: " + str(temp))

    def button_chi_square_event(self):
        temp = self.calculator.calculate_chi_square(self.data)
        self.history.append("Chi Square Calculated: " + str(temp))

    def button_correlation_coefficient_event(self):
        temp = self.calculator.calculate_correlation_coefficient(self.data)
        self.history.append("Correlation Coefficient Calculated: " + str(temp))

    def button_sign_test_event(self):
        temp = self.calculator.calculate_sign_test(self.data)
        self.history.append("Sign Test Calculated: " + str(temp))

    def button_rank_sum_test_event(self):
        temp = self.calculator.calculate_rank_sum_test(self.data)
        self.history.append("Rank Sum Test Calculated: " + str(temp))

    def button_spearman_rank_event(self):
        temp = self.calculator.calculate_spearman_rank(self.data)
        self.history.append("Spearman Rank Calculated: " + str(temp))

    def button_horizontal_bar_chart_event(self):
        self.plotter.make_horizontal_bar_chart()
        self.history.append("Made a horizontal bar chart.")

    def button_vertical_bar_chart_event(self):
        self.plotter.make_vertical_bar_chart()
        self.history.append("Made a vertical bar chart.")

    def button_pie_chart_event(self):
        self.plotter.make_pie_chart()
        self.history.append("Made a pie chart.")

    def button_normal_distribution_curve_event(self):
        self.plotter.make_normal_distribution_curve()
        self.history.append("Made a normal distribution curve.")

    def button_xy_graph_event(self):
        self.plotter.make_xy_graph()
        self.history.append("Made an XY graph.")


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
        ui = Ui_Form1()
        ui.setupUi(inter)
        application.setCentralWidget(inter)
        sys.exit(app.exec_())
    elif typeFlag == 2:
        ordn = QtWidgets.QWidget()
        ui = Ui_Form2()
        ui.setupUi(ordn)
        application.setCentralWidget(ordn)
        sys.exit(app.exec_())
    elif typeFlag == 3:
        freq = QtWidgets.QWidget()
        application.data = ui.getData()
        freqObject = FrequencyDataObject(application.data)
        ui = Ui_Form()
        ui.setupUi(freq)
        application.setCentralWidget(freq)
        text = "X: {}\nY: {}\nChi Square: {}\nExpected Mode: {}\nActual Mode: {}\n" \
               "Probability Dist: {}\nBinomial Distribution: {}\n" \
            .format(str(freqObject.x), str(freqObject.y), str(freqObject.chi_square), str(freqObject.expected_mode),
                    str(freqObject.actual_mode), str(freqObject.probability_distribution),
                    str(freqObject.binomial_distribution))
        ui.qlabel.setText(text)
        sys.exit(app.exec_())

    # def freqReport():
    #     return )