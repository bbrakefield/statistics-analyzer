#"""
#Module containing the code that will generate the view for selecting data.
#"""

# Authors: Jenna McCown
#          Brannon Brakefield

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from ManualDataEntry import ManualDataEntry
import pandas as pd

typeFlag = 0  # global flag for keeping track of which data object is going to be created.

# =============================================================================
# Data specification dialog screen.
# =============================================================================

class Ui_Dialog(QFileDialog):
    """This is the screen that will allow users to select which
    data type they wish to work with. The user will also be able to
    choose the file, invoke manual entry, or specify which columns and/or
    rows they which to operate on within the data file.
    """

    def __init__(self, Dialog, mainApp):
        super(QFileDialog, self).__init__()
        self.mainApp = mainApp
        self.col_headers = []
        self.row_headers = []
        self.setupUi(Dialog)
        self.data = [[None, None, None], [None, None, None]]


    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(354, 306)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.IntervalRadioB = QtWidgets.QRadioButton(self.groupBox)
        self.IntervalRadioB.setGeometry(QtCore.QRect(9, 70, 241, 20))
        self.IntervalRadioB.setObjectName("IntervalRadioB")
        self.IntervalRadioB.clicked.connect(self.isInterval)
        self.OrdinalRadioB = QtWidgets.QRadioButton(self.groupBox)
        self.OrdinalRadioB.setGeometry(QtCore.QRect(9, 40, 241, 20))
        self.OrdinalRadioB.setObjectName("OrdinalRadioB")
        self.OrdinalRadioB.clicked.connect(self.isOrdinal)
        self.FreqRadioB = QtWidgets.QRadioButton(self.groupBox)
        self.FreqRadioB.setGeometry(QtCore.QRect(9, 100, 241, 20))
        self.FreqRadioB.setObjectName("FreqRadioB")
        self.FreqRadioB.clicked.connect(self.isFrequency)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 180, 110, 32))
        self.groupBox2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox2.setGeometry(QtCore.QRect(145, 80, 161, 131))
        self.groupBox2.setObjectName("groupBox2")

        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(150, 40, 110, 32))
        self.pushButton.setObjectName("pushButton")

        # Open file button listener
        self.pushButton.clicked.connect(self.open_file)

        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        # Allow users to select columns and rows to have data run on
        self.rowBeginSpinBox = QtWidgets.QSpinBox(self.groupBox2)
        self.rowBeginSpinBox.setGeometry(QtCore.QRect(10, 50, 53, 24))
        self.rowBeginSpinBox.setMinimum(0)
        self.rowBeginSpinBox.setMaximum(999)
        self.rowBeginSpinBox.setObjectName("spinBox")
        self.rowsToLabel = QtWidgets.QLabel(self.groupBox2)
        self.rowsToLabel.setGeometry(QtCore.QRect(75, 50, 61, 20))
        self.rowsToLabel.setObjectName("rowsToLabel")
        self.rowsLabel = QtWidgets.QLabel(self.groupBox2)
        self.rowsLabel.setGeometry(QtCore.QRect(50, 30, 56, 13))
        self.rowsLabel.setObjectName("rowsLabel")
        self.rowEndSpinBox = QtWidgets.QSpinBox(self.groupBox2)
        self.rowEndSpinBox.setGeometry(QtCore.QRect(100, 50, 53, 24))
        self.rowEndSpinBox.setMinimum(0)
        self.rowEndSpinBox.setMaximum(999)
        self.rowEndSpinBox.setObjectName("spinBox_2")
        self.colsToLabel = QtWidgets.QLabel(self.groupBox2)
        self.colsToLabel.setGeometry(QtCore.QRect(75, 100, 51, 20))
        self.colsToLabel.setObjectName("colsToLabel")
        self.colBeginSpinBox = QtWidgets.QSpinBox(self.groupBox2)
        self.colBeginSpinBox.setGeometry(QtCore.QRect(10, 100, 53, 24))
        self.colBeginSpinBox.setMinimum(0)
        self.colBeginSpinBox.setMaximum(999)
        self.colBeginSpinBox.setObjectName("spinBox_3")
        self.colEndSpinBox = QtWidgets.QSpinBox(self.groupBox2)
        self.colEndSpinBox.setGeometry(QtCore.QRect(100, 100, 53, 24))
        self.colEndSpinBox.setMinimum(0)
        self.colEndSpinBox.setMaximum(999)
        self.colEndSpinBox.setObjectName("spinBox_4")
        self.colsLabel = QtWidgets.QLabel(self.groupBox2)
        self.colsLabel.setGeometry(QtCore.QRect(50, 80, 71, 16))
        self.colsLabel.setObjectName("colsLabel")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(self.closeIt)

        self.pushButton_2.clicked.connect(self.manualEntry)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.history = []

    def open_file(self):
        """Choose file to import using file dialog, then import it"""
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                      "CSV File (*.csv);;All Files (*)")

        self.import_data(filename)

    def import_data(self, filename):
        """Import data from csv file given filename."""

        # The dimensions of the data frame we want to extract from the file.
        startrow = self.rowBeginSpinBox.value()
        endrow = self.rowEndSpinBox.value()
        startcol = self.colBeginSpinBox.value()
        endcol = self.colEndSpinBox.value()

        # Prevent the user from selecting the first row and first column.
        if startrow == 0:
            startrow = 1
        if endrow == 0:
            endrow = None
        if startcol == 0:
            startcol = 1
        if endcol == 0:
            endcol = None

        # Extract the data.
        try:
            with open(filename) as input_file:
                df = pd.read_csv(input_file, header=None)
                rows = df.iloc[startrow:endrow, :1].values.tolist()

                self.row_headers = [item for sublist in rows for item in sublist]
                self.col_headers = df.iloc[:1, startcol:endcol].values.tolist()[0]

                df2 = df.iloc[startrow:endrow, startcol:endcol]
                data = df2.values.tolist()
                self.data = data

        except IOError:
            print("Could not open file: {}!".format(filename))

        # send data to the main class.
        self.mainApp.setData(self.data)

    def closeIt(self):
        exit(0)

    def closeEvent(self, event):
        exit(0)

    def set_theData(self, theData):
        self.data = theData

    def set_row_headers(self, rows):
        self.row_headers = rows

    def set_col_headers(self, cols):
        self.col_headers = cols

    def isInterval(self):
        global typeFlag
        typeFlag = 2

    def isOrdinal(self):
        global typeFlag
        typeFlag = 1

    def isFrequency(self):
        global typeFlag
        typeFlag = 3

    def getType(self):
        return typeFlag

    def getData(self):
        return self.data

    def get_col_headers(self):
        return self.col_headers

    def get_row_headers(self):
        return self.row_headers

    def manualEntry(self):
        """Invoke the manual entry data screen."""

        Dialog = QtWidgets.QDialog()
        self.ui = ManualDataEntry()
        self.ui.setupUi(Dialog, self, typeFlag)
        Dialog.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Data Type"))
        self.groupBox.setTitle(_translate("Dialog", "Statistical Data Type:"))
        self.IntervalRadioB.setText(_translate("Dialog", "Interval"))
        self.OrdinalRadioB.setText(_translate("Dialog", "Ordinal"))
        self.FreqRadioB.setText(_translate("Dialog", "Frequency"))
        self.pushButton_2.setText(_translate("Dialog", "Manual Input"))
        self.pushButton.setText(_translate("Dialog", "Open File"))
        self.rowsToLabel.setText(_translate("Dialog", "to"))
        self.rowsLabel.setText(_translate("Dialog", "Rows"))
        self.colsToLabel.setText(_translate("Dialog", "to"))
        self.colsLabel.setText(_translate("Dialog", "Columns"))
        self.groupBox2.setTitle(_translate("Dialog", "Select Data for Analysis:"))
