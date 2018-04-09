# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrequencyDataScreen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from frequency import FrequencyDataObject
from PyQt5 import QtCore, QtWidgets
from matplottest import App
import csv

class Ui_Form(object):

    def setupUi(self, Form, freqObject):
        self.chiSquarebool = False
        self.modeBool = False
        self.probabilityBool = False
        self.binomialBool = False
        self.freqObject = freqObject
        self.frequencyObject = FrequencyDataObject(freqObject)
        self.verBarBool = False
        self.horBarBool = False
        self.pieCharBool = False

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
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 60, 90, 18))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 90, 161, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 190, 151, 18))
        self.checkBox_4.setObjectName("checkBox_4")
        self.pbTrialsLabel = QtWidgets.QLabel(self.groupBox_2)
        self.pbTrialsLabel.setGeometry(QtCore.QRect(140, 120, 41, 21))
        self.pbTrialsLabel.setObjectName("pbTrialsLabel")
        self.pbTrialSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.pbTrialSpinBox.setGeometry(QtCore.QRect(180, 120, 53, 21))
        self.pbTrialSpinBox.setMinimum(1)
        self.pbTrialSpinBox.setMaximum(9999)
        self.pbTrialSpinBox.setObjectName("pbTrialSpinBox")
        self.pbSuccessSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.pbSuccessSpinBox.setGeometry(QtCore.QRect(180, 150, 53, 24))
        self.pbSuccessSpinBox.setMaximum(9999)
        self.pbSuccessSpinBox.setObjectName("pbSuccessSpinBox")
        self.pbSuccessesLabel = QtWidgets.QLabel(self.groupBox_2)
        self.pbSuccessesLabel.setGeometry(QtCore.QRect(110, 150, 71, 31))
        self.pbSuccessesLabel.setObjectName("pbSuccessesLabel")
        self.bdTrialSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.bdTrialSpinBox.setGeometry(QtCore.QRect(180, 220, 53, 21))
        self.bdTrialSpinBox.setMinimum(1)
        self.bdTrialSpinBox.setMaximum(9999)
        self.bdTrialSpinBox.setObjectName("bdTrialSpinBox")
        self.bdTrialLabel = QtWidgets.QLabel(self.groupBox_2)
        self.bdTrialLabel.setGeometry(QtCore.QRect(140, 220, 41, 21))
        self.bdTrialLabel.setObjectName("bdTrialLabel")
        self.bdSuccessSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.bdSuccessSpinBox.setGeometry(QtCore.QRect(180, 250, 53, 24))
        self.bdSuccessSpinBox.setMaximum(9999)
        self.bdSuccessSpinBox.setObjectName("bdSuccessSpinBox")
        self.bdSuccessLabel = QtWidgets.QLabel(self.groupBox_2)
        self.bdSuccessLabel.setGeometry(QtCore.QRect(110, 250, 71, 31))
        self.bdSuccessLabel.setObjectName("bdSuccessLabel")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(180, 280, 62, 31))
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setMaximum(0.99)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.bdProbSuccess = QtWidgets.QLabel(self.groupBox_2)
        self.bdProbSuccess.setGeometry(QtCore.QRect(40, 283, 131, 31))
        self.bdProbSuccess.setObjectName("bdProbSuccess")
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox_2.setGeometry(QtCore.QRect(50, 520, 164, 32))
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.verBarRadioB = QtWidgets.QRadioButton(self.groupBox)
        self.verBarRadioB.setGeometry(QtCore.QRect(20, 40, 141, 18))
        self.verBarRadioB.setObjectName("verBarRadioB")
        self.horBarRadioB = QtWidgets.QRadioButton(self.groupBox)
        self.horBarRadioB.setGeometry(QtCore.QRect(20, 70, 151, 20))
        self.horBarRadioB.setObjectName("horBarRadioB")
        self.pieCharRadioB = QtWidgets.QRadioButton(self.groupBox)
        self.pieCharRadioB.setGeometry(QtCore.QRect(20, 100, 97, 18))
        self.pieCharRadioB.setObjectName("pieCharRadioB")
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
        self.verBarRadioB.setText(_translate("Form", "Vertical Bar Chart"))
        self.horBarRadioB.setText(_translate("Form", "Horizontal Bar Chart"))
        self.pieCharRadioB.setText(_translate("Form", "Pie Chart"))
        self.pbTrialsLabel.setText(_translate("Form", "Trials"))
        self.pbSuccessesLabel.setText(_translate("Form", "Successes"))
        self.bdTrialLabel.setText(_translate("Form", "Trials"))
        self.bdSuccessLabel.setText(_translate("Form", "Successes"))
        self.bdProbSuccess.setText(_translate("Form", "Probability of Success:"))
        self.checkBox.stateChanged.connect(self.setModeBool)
        self.checkBox_2.stateChanged.connect(self.setChiSquareBool)
        self.checkBox_3.stateChanged.connect(self.setProbabilityBool)
        self.checkBox_4.stateChanged.connect(self.setBinomialBool)
        self.buttonBox.accepted.connect(self.calcSubmit)
        self.buttonBox.clicked.connect(self.calcReset)
        self.verBarRadioB.clicked.connect(self.setVerBarBool)
        self.horBarRadioB.clicked.connect(self.setHorBarBool)
        self.pieCharRadioB.clicked.connect(self.setPieCharBool)
        self.buttonBox_2.accepted.connect(self.graphSubmit)

    def setVerBarBool(self):
        self.verBarBool = True
        self.horBarBool = False
        self.pieCharBool = False

    def setHorBarBool(self):
        self.horBarBool = True
        self.verBarBool = False
        self.pieCharBool = False

    def setPieCharBool(self):
        self.pieCharBool = True
        self.verBarBool = False
        self.horBarBool = False
    def graphSubmit(self):
        if self.verBarBool == True:
            Dialog = QtWidgets.QDialog()
            ui = App(Dialog, self.freqObject, 2, 1)
            Dialog.exec_()
        elif self.horBarBool == True:
            Dialog = QtWidgets.QDialog()
            ui = App(Dialog, self.freqObject, 2, 2)
            Dialog.exec_()
        elif self.pieCharBool == True:
            Dialog = QtWidgets.QDialog()
            ui = App(Dialog, self.freqObject, 2, 3)
            Dialog.exec_()

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

    def calcSubmit(self):
        pbSuccesses = self.pbSuccessSpinBox.value()
        pbTrials = self.pbTrialSpinBox.value()
        bdSuccesses = self.bdSuccessSpinBox.value()
        bdTrials = self.bdTrialSpinBox.value()
        bdProbSucc = self.doubleSpinBox.value()
        f= open("frequencyDataReport.txt", "w")
        f.write("===Frequency Data Report===\n\n")
        if self.modeBool == True:
            if self.frequencyObject.expected_mode == None:
                f.write("Expected Mode: There is no mode to be calculated.\n")
                modeText = "Expected Mode: There is no mode to be calculated.\n"
                self.listWidget.addItem(modeText)
            else:
                f.write("Expected Mode: " + str(self.frequencyObject.expected_mode) + "\n")
                modeText = "Expected Mode: " + str(self.frequencyObject.expected_mode) + "\n"
                self.listWidget.addItem(modeText)

            if self.frequencyObject.actual_mode == None:
                f.write("Actual Mode: There is no mode to be calculated.\n")
                modeText = "Actual Mode: There is no mode to be calculated.\n"
                self.listWidget.addItem(modeText)
            else:
                f.write("Actual Mode: " + str(self.frequencyObject.actual_mode) + "\n")
                modeText = modeText + "Actual Mode: " + str(self.frequencyObject.actual_mode) + "\n"
                self.listWidget.addItem(modeText)

        if self.chiSquarebool==True:
            if self.frequencyObject.chi_square == None:
                f.write("Chi Square: Value could not be calculated.\n")
                chiSquareText = "Chi Square: Value could not be calculated.\n"
                self.listWidget.addItem(chiSquareText)
            else:
                f.write("Chi Square: " + str(self.frequencyObject.chi_square) + "\n")
                chiSquareText = "Chi Square: " + str(self.frequencyObject.chi_square) + "\n"
                self.listWidget.addItem(chiSquareText)

        if self.probabilityBool==True:
            if pbTrials < pbSuccesses:
                f.write("Probability Distribution: invalid data provided. Successes cannot exceed trials.")
                probText = "Probability Distribution: invalid data provided. Successes cannot exceed trials."
                self.listWidget.addItem(probText)
            else:
                f.write("Probability Distribution: " + str(self.frequencyObject.get_probability_distribution(pbSuccesses, pbTrials)) + "\n")
                probText = "Probability Distribution: " + str(self.frequencyObject.get_probability_distribution(pbSuccesses, pbTrials)) + "\n"
                self.listWidget.addItem(probText)

        if self.binomialBool==True:
            if bdTrials < bdSuccesses:
                f.write("Binomial Distribution: Invalid data provided. Successes cannot exceed trials.")
                binText = "Binomial Distribution: Invalid data provided. Successes cannot exceed trials."
                self.listWidget.addItem(binText)
            else:
                f.write("Binomial Distribution: " + str(self.frequencyObject.get_binomial_distribution(bdProbSucc, bdTrials, bdSuccesses)) + "\n")
                binText = "Binomial Distribution: " + str(self.frequencyObject.get_binomial_distribution(bdProbSucc, bdTrials, bdSuccesses)) + "\n"
                self.listWidget.addItem(binText)

        f.close()
        with open('frequencyResults.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Mode', 'Chi Square', 'Prob. Dist.', 'Binom Dist.'])
            writer.writerow([self.frequencyObject.actual_mode, self.frequencyObject.chi_square,
                             self.frequencyObject.get_probability_distribution(pbSuccesses, pbTrials),
                             self.frequencyObject.get_binomial_distribution(bdProbSucc, bdTrials, bdSuccesses)])
            writer.writerow([self.frequencyObject.actual_mode])


    def calcReset(self):
        self.listWidget.clear()

