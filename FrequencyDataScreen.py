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
        frequencyObject = FrequencyDataObject(freqObject)
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
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_3)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 601, 661))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 599, 659))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        #self.label.setGeometry(QtCore.QRect(20, 40, 56, 13))
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setObjectName("label_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)

        text = "X: {}\nY: {}\nChi Square: {}\nExpected Mode: {}\nActual Mode: {}\n" \
               "Probability Dist: {}\nBinomial Distribution: {}\n" \
            .format(str(frequencyObject.x), str(frequencyObject.y), str(frequencyObject.chi_square), str(frequencyObject.expected_mode),
                    str(frequencyObject.actual_mode), str(frequencyObject.probability_distribution),
                    str(frequencyObject.binomial_distribution))
        self.label.setText(text)

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
        if self.modeBool == True:
            print("hey mode")
        if self.chiSquarebool==True:
            print("hey chi")
        if self.probabilityBool==True:
            print("hey prob")
        if self.binomialBool==True:
            print("hey bin")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

