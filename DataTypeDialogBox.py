# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataTypeDialogBox.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from FrequencyDataScreen import Ui_Form
import csv

typeFlag = 0

class Ui_Dialog(QFileDialog):

    def __init__(self):
        super(QFileDialog, self).__init__()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(284, 216)
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
        self.pushButton_2.setGeometry(QtCore.QRect(130, 90, 110, 32))

        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(130, 40, 110, 32))
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

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.history = []

    def test(self):
        print("test")

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

    def isInterval(self):
        global typeFlag
        typeFlag = 1

    def isOrdinal(self):
        global typeFlag
        typeFlag = 2

    def isFrequency(self):
        global typeFlag
        typeFlag = 3

    def end(self):
        print(typeFlag)

    def getType(self):
        return typeFlag


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Data Type"))
        self.groupBox.setTitle(_translate("Dialog", "Statistical Data Type:"))
        self.IntervalRadioB.setText(_translate("Dialog", "Interval"))
        self.OrdinalRadioB.setText(_translate("Dialog", "Ordinal"))
        self.FreqRadioB.setText(_translate("Dialog", "Frequency"))
        self.pushButton_2.setText(_translate("Dialog", "Manual Input"))
        self.pushButton.setText(_translate("Dialog", "Open File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
