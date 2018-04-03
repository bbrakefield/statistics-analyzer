# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrequencyDataScreen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from frequency import FrequencyDataObject
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):

    def setupUi(self, Form, freqObject):
        self.chiSquarebool = False
        self.modeBool = False
        self.probabilityBool = False
        self.binomialBool = False
        self.frequencyObject = FrequencyDataObject(freqObject)
        text = "X: {}\nY: {}\nChi Square: {}\nExpected Mode: {}\nActual Mode: {}\n" \
               "Probability Dist: {}\nBinomial Distribution: {}\n" \
            .format(str(self.frequencyObject.x), str(self.frequencyObject.y), str(self.frequencyObject.chi_square), str(self.frequencyObject.expected_mode),
                    str(self.frequencyObject.actual_mode), str(self.frequencyObject.probability_distribution),
                    str(self.frequencyObject.binomial_distribution))

        Form.setObjectName("Form")
        Form.resize(1280, 706)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 85, 18))
        self.checkBox.setObjectName("checkBox")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox_2)
        self.buttonBox.setGeometry(QtCore.QRect(30, 520, 164, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 60, 90, 18))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 90, 161, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 120, 151, 18))
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox_2.setGeometry(QtCore.QRect(50, 520, 164, 32))
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 141, 18))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 151, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 100, 97, 18))
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 601, 661))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.addItem(text)
        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.listWidget.addItem(text)
        self.listWidget.addItem(text)
        self.listWidget.addItem(text)
        self.listWidget.addItem(text)
        self.listWidget.addItem(text)
        self.listWidget.addItem(text)
        self.listWidget.addItem(text)
        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Calculations"))
        self.checkBox.setText(_translate("Form", "Mode"))
        self.checkBox_2.setText(_translate("Form", "Chi Square"))
        self.checkBox_3.setText(_translate("Form", "Probability Distribution"))
        self.checkBox_4.setText(_translate("Form", "Binomial Distribution"))
        self.groupBox.setTitle(_translate("Form", "Graphs"))
        self.radioButton.setText(_translate("Form", "Vertical Bar Chart"))
        self.radioButton_2.setText(_translate("Form", "Horizontal Bar Chart"))
        self.radioButton_3.setText(_translate("Form", "Pie Chart"))
        self.checkBox.stateChanged.connect(self.setModeBool)
        self.checkBox_2.stateChanged.connect(self.setChiSquareBool)
        self.checkBox_3.stateChanged.connect(self.setProbabilityBool)
        self.checkBox_4.stateChanged.connect(self.setBinomialBool)
        self.buttonBox.accepted.connect(self.submit)

    def setModeBool(self):
        if self.modeBool == True:
            self.modeBool = False
        elif self.modeBool == False:
            self.modeBool = True

    def setChiSquareBool(self):
        if self.chiSquarebool == True:
            self.chiSquarebool = False
        elif self.chiSquarebool == False:
            self.chiSquarebool = True

    def setProbabilityBool(self):
        if self.probabilityBool == True:
            self.probabilityBool = False
        elif self.probabilityBool == False:
            self.probabilityBool = True

    def setBinomialBool(self):
        if self.binomialBool == True:
            self.binomialBool = False
        elif self.binomialBool == False:
            self.binomialBool = True

    def submit(self):

        f= open("frequencyDataReport.txt", "w")
        f.write("===Frequency Data Report===\n\n")
        if self.modeBool == True:
            if self.frequencyObject.actual_mode == None:
                f.write("Mode: There is no mode to be calculated.\n")
            else:
                f.write("Mode: " + str(self.frequencyObject.actual_mode) + "\n")
            print("Hey mode")

        if self.chiSquarebool==True:
            if self.frequencyObject.chi_square == None:
                f.write("Chi Square: Value could not be calculated.\n")
            else:
                f.write("Chi Square: " + str(self.frequencyObject.chi_square) + "\n")
            print("Hey Chi")

        if self.probabilityBool==True:
            if self.frequencyObject.probability_distribution == None:
                f.write("Probability Distribution: Value could not be calculated.\n")
            else:
                f.write("Probability Distribution: " + str(self.frequencyObject.probability_distribution) + "\n")
            print("Hey prob")

        if self.binomialBool==True:
            if self.frequencyObject.binomial_distribution == None:
                f.write("Binomial Distribution: Value could not be calculated\n")
            else:
                f.write("Binomial Distribution: " + str(self.frequencyObject.binomial_distribution) + "\n")
            print("Hey bin")

        f.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

