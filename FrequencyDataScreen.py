"""
Module responsible for generating the view when operating on frequency data objects.
"""
from frequency import FrequencyDataObject
from PyQt5 import QtCore, QtWidgets
from matplottest import App
import csv

# =============================================================================
# Frequency data screen
# =============================================================================


class Ui_Form(object):
    """The view that is shown when operating on freqency data.
    User will be able to select which stats they wish to see in the report,
    Generate charts, and export data and reports."""

    def __init__(self):
        super().__init__()
        self.last_figure_plotted = None

    def setupUi(self, Form, freqObject, mainScreenObj):
        self.mainScreenObject = mainScreenObj
        self.col_headers = mainScreenObj.col_headers
        self.row_headers = mainScreenObj.row_headers
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
        self.selectAllButton = QtWidgets.QPushButton(self.groupBox_2)
        self.selectAllButton.setGeometry(QtCore.QRect(10, 320, 100, 30))
        self.selectAllButton.setObjectName("selectAllButton")

        self.deselectAllButton = QtWidgets.QPushButton(self.groupBox_2)
        self.deselectAllButton.setGeometry(QtCore.QRect(110, 320, 100, 30))
        self.deselectAllButton.setObjectName("deselectAllButton")

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
        self.selectAllButton.setText(_translate("Form", "Select All"))
        self.deselectAllButton.setText(_translate("Form", "Deselect All"))
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
        self.selectAllButton.clicked.connect(self.selectAll)
        self.deselectAllButton.clicked.connect(self.deselectAll)

    def selectAll(self):
        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)
        self.checkBox_4.setChecked(True)

    def deselectAll(self):
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)

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
            self.ui = App(Dialog, self.freqObject, 2, 1, self.col_headers, self.row_headers)
            Dialog.exec_()
        elif self.horBarBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.freqObject, 2, 2, self.col_headers, self.row_headers)
            Dialog.exec_()
        elif self.pieCharBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.freqObject, 2, 3, self.col_headers, self.row_headers)
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
        """Write calculation report and show it on the GUI."""

        pbSuccesses = self.pbSuccessSpinBox.value()
        pbTrials = self.pbTrialSpinBox.value()
        bdSuccesses = self.bdSuccessSpinBox.value()
        bdTrials = self.bdTrialSpinBox.value()
        bdProbSucc = self.doubleSpinBox.value()
        report = []

        report.append("===Frequency Data Report===\n\n")
        if self.modeBool == True:
            if self.frequencyObject.expected_mode == None:
                modeText = "Expected Mode: There is no mode to be calculated.\n"
                report.append(modeText)
                self.listWidget.addItem(modeText)
            else:
                modeText = "Expected Mode: " + str(self.frequencyObject.expected_mode) + "\n"
                report.append(modeText)
                self.listWidget.addItem(modeText)

            if self.frequencyObject.actual_mode == None:
                modeText = "Actual Mode: There is no mode to be calculated.\n"
                report.append(modeText)
                self.listWidget.addItem(modeText)
            else:
                modeText = "Actual Mode: " + str(self.frequencyObject.actual_mode) + "\n"
                report.append(modeText)
                self.listWidget.addItem(modeText)

        if self.chiSquarebool==True:
            if self.frequencyObject.chi_square == None:
                chiSquareText = "Chi Square: Value could not be calculated.\n"
                report.append(chiSquareText)
                self.listWidget.addItem(chiSquareText)
            else:
                chiSquareText = "Chi Square: " + str(self.frequencyObject.chi_square) + "\n"
                report.append(chiSquareText)
                self.listWidget.addItem(chiSquareText)

        if self.probabilityBool==True:
            if pbTrials < pbSuccesses:
                probText = "Probability Distribution: invalid data provided. Successes cannot exceed trials."
                report.append(probText)
                self.listWidget.addItem(probText)
            else:
                probText = "Probability Distribution: " + str(self.frequencyObject.get_probability_distribution(pbSuccesses, pbTrials)) + "\n"
                report.append(probText)
                self.listWidget.addItem(probText)

        if self.binomialBool==True:
            if bdTrials < bdSuccesses:
                binText = "Binomial Distribution: Invalid data provided. Successes cannot exceed trials."
                report.append(binText)
                self.listWidget.addItem(binText)
            else:
                binText = "Binomial Distribution: " + str(self.frequencyObject.get_binomial_distribution(bdProbSucc, bdTrials, bdSuccesses)) + "\n"
                report.append(binText)
                self.listWidget.addItem(binText)

        # call main function for setting report list in Application class
        self.mainScreenObject.set_report(report)

        if self.frequencyObject.actual_mode == None:
            actual_mode_text = "None"
        else:
            actual_mode_text = self.frequencyObject.actual_mode

        if self.frequencyObject.expected_mode == None:
            expected_mode_text = "None"
        else:
            expected_mode_text = self.frequencyObject.expected_mode

        # Gather up information for csv_report
        csv_data =  [['Type', 'Mode', 'Chi Square', 'Prob. Dist.', 'Binom Dist.'],
                     ['Actual', actual_mode_text, self.frequencyObject.chi_square,
                         self.frequencyObject.get_probability_distribution(pbSuccesses, pbTrials),
                         self.frequencyObject.get_binomial_distribution(bdProbSucc, bdTrials, bdSuccesses)],
                     ['Expected', expected_mode_text, self.frequencyObject.chi_square,
                         self.frequencyObject.get_probability_distribution(pbSuccesses, pbTrials),
                         self.frequencyObject.get_binomial_distribution(bdProbSucc, bdTrials, bdSuccesses)]]

        # store it in main.
        self.mainScreenObject.set_csv(csv_data)


    def calcReset(self):
        self.listWidget.clear()

