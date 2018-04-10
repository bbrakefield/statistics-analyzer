# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testing123.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from ordinal import OrdinalDataObject
from matplottest import App
import csv

class Ui_Form2(object):

    def __init__(self):
        super().__init__()
        self.last_figure_plotted = None

    def setupUi(self, Form, ordObject):

        self.percentileBool = False
        self.medianbool = False
        self.modeBool = False
        self.rankSumBool = False
        self.signBool = False
        self.verBarBool = False
        self.horBarBool = False
        self.pieCharBool = False
        self.xyPlotBool = False
        self.normalCurBool = False
        self.ordObject = ordObject
        self.ordinalObject = OrdinalDataObject(ordObject)
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1280, 706)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.MediancheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.MediancheckBox.setGeometry(QtCore.QRect(10, 30, 85, 18))
        self.MediancheckBox.setObjectName("MediancheckBox")
        self.CalcButtonBox = QtWidgets.QDialogButtonBox(self.groupBox_2)
        self.CalcButtonBox.setGeometry(QtCore.QRect(30, 520, 164, 32))
        self.CalcButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.Ok)
        self.CalcButtonBox.setObjectName("CalcButtonBox")
        self.modeCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.modeCheckBox.setGeometry(QtCore.QRect(10, 60, 85, 18))
        self.modeCheckBox.setObjectName("modeCheckBox")
        self.SignTestCheck = QtWidgets.QCheckBox(self.groupBox_2)
        self.SignTestCheck.setGeometry(QtCore.QRect(10, 90, 161, 21))
        self.SignTestCheck.setObjectName("SignTestCheck")
        self.RankSumCheck = QtWidgets.QCheckBox(self.groupBox_2)
        self.RankSumCheck.setGeometry(QtCore.QRect(10, 120, 151, 18))
        self.RankSumCheck.setObjectName("RankSumCheck")
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setEnabled(True)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.graphButtonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.graphButtonBox.setGeometry(QtCore.QRect(50, 520, 164, 32))
        self.graphButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.graphButtonBox.setObjectName("graphButtonBox")
        self.verBarRadioB = QtWidgets.QRadioButton(self.groupBox)
        self.verBarRadioB.setGeometry(QtCore.QRect(20, 40, 141, 18))
        self.verBarRadioB.setObjectName("verBarRadioB")
        self.horBarRadioB = QtWidgets.QRadioButton(self.groupBox)
        self.horBarRadioB.setGeometry(QtCore.QRect(20, 70, 151, 20))
        self.horBarRadioB.setObjectName("horBarRadioB")
        self.pieChartRadioB = QtWidgets.QRadioButton(self.groupBox)
        self.pieChartRadioB.setGeometry(QtCore.QRect(20, 100, 97, 18))
        self.pieChartRadioB.setObjectName("pieChartRadioB")
        self.xyPlotRadioB = QtWidgets.QRadioButton(self.groupBox)
        self.xyPlotRadioB.setGeometry(QtCore.QRect(20, 130, 97, 18))
        self.xyPlotRadioB.setObjectName("xyPlotRadioB")
        self.normalCurRadioB = QtWidgets.QRadioButton(self.groupBox)
        self.normalCurRadioB.setGeometry(QtCore.QRect(20, 160, 111, 18))
        self.normalCurRadioB.setObjectName("normalCurRadioB")
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 601, 661))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.retranslateUi(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Calculations"))
        self.MediancheckBox.setText(_translate("Form", "Median"))
        self.modeCheckBox.setText(_translate("Form", "Mode"))
        self.SignTestCheck.setText(_translate("Form", "Sign Test"))
        self.RankSumCheck.setText(_translate("Form", "Rank Sum"))
        self.groupBox.setTitle(_translate("Form", "Graphs"))
        self.verBarRadioB.setText(_translate("Form", "Vertical Bar Chart"))
        self.horBarRadioB.setText(_translate("Form", "Horizontal Bar Chart"))
        self.pieChartRadioB.setText(_translate("Form", "Pie Chart"))
        self.xyPlotRadioB.setText(_translate("Form", "XY Plot"))
        self.normalCurRadioB.setText(_translate("Form", "Normal Curve"))


        self.modeCheckBox.stateChanged.connect(self.setModeBool)
        self.MediancheckBox.stateChanged.connect(self.setMedianBool)
        self.SignTestCheck.stateChanged.connect(self.setSignTestBool)
        self.RankSumCheck.stateChanged.connect(self.setRankBool)
        self.CalcButtonBox.accepted.connect(self.calcSubmit)
        self.CalcButtonBox.clicked.connect(self.calcReset)
        self.verBarRadioB.clicked.connect(self.setVerBarBool)
        self.horBarRadioB.clicked.connect(self.setHorBarBool)
        self.pieChartRadioB.clicked.connect(self.setPieCharBool)
        self.xyPlotRadioB.clicked.connect(self.setXYPlotBool)
        self.normalCurRadioB.clicked.connect(self.setNormalCurBool)
        self.graphButtonBox.accepted.connect(self.graphSubmit)


    def setMedianBool(self):
        if self.medianbool == True:
            self.medianbool = False
        elif self.medianbool == False:
            self.medianbool = True

    def setModeBool(self):
        if self.modeBool == True:
            self.modeBool = False
        elif self.modeBool == False:
            self.modeBool = True

    def setSignTestBool(self):
        if self.signBool == True:
            self.signBool = False
        elif self.signBool == False:
            self.signBool = True

    def setRankBool(self):
        if self.rankSumBool == True:
            self.rankSumBool = False
        elif self.rankSumBool == False:
            self.rankSumBool = True

    def setPercentileBool(self):
        if self.percentileBool == True:
            self.percentileBool = False
        elif self.percentileBool == False:
            self.percentileBool = True

    def graphSubmit(self):
        if self.verBarBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.ordObject, 3, 1)
            Dialog.exec_()
        elif self.horBarBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.ordObject, 3, 2)
            Dialog.exec_()
        elif self.pieCharBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.ordObject, 3, 3)
            Dialog.exec_()
        elif self.xyPlotBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.ordObject, 3, 4)
            Dialog.exec_()
        elif self.normalCurBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.ordObject, 3, 5)
            Dialog.exec_()

    def setVerBarBool(self):
        self.verBarBool = True
        self.horBarBool = False
        self.pieCharBool = False
        self.xyPlotBool = False
        self.normalCurBool = False

    def setHorBarBool(self):
        self.horBarBool = True
        self.verBarBool = False
        self.pieCharBool = False
        self.xyPlotBool = False
        self.normalCurBool = False

    def setPieCharBool(self):
        self.pieCharBool = True
        self.verBarBool = False
        self.horBarBool = False
        self.xyPlotBool = False
        self.normalCurBool = False

    def setXYPlotBool(self):
        self.xyPlotBool = True
        self.verBarBool = False
        self.horBarBool = False
        self.pieCharBool = False
        self.normalCurBool = False

    def setNormalCurBool(self):
        self.normalCurBool = True
        self.verBarBool = False
        self.horBarBool = False
        self.pieCharBool = False
        self.xyPlotBool = False

    def calcSubmit(self):

        headers = ["Choices"]
        stats = []
        f = open("ordinalDataReport.txt", "w")
        f.write("===Ordinal Data Report===\n\n")
        if self.medianbool == True:
            medianText = "Median A: {}\n" \
                .format(str(self.ordinalObject.a_median))
            f.write(medianText)
            self.listWidget.addItem(medianText)

            medianText = "Median B: {}\n" \
                .format(str(self.ordinalObject.b_median))
            f.write(medianText)
            self.listWidget.addItem(medianText)

            medianText = "Median C: {}\n" \
                .format(str(self.ordinalObject.c_median))
            f.write(medianText)
            self.listWidget.addItem(medianText)

            medianText = "Median D: {}\n" \
                .format(str(self.ordinalObject.d_median))
            f.write(medianText)
            self.listWidget.addItem(medianText)

            medianText = "Median E: {}\n" \
                .format(str(self.ordinalObject.e_median))
            f.write(medianText)
            self.listWidget.addItem(medianText)

            headers.append("Median")
            medians = [self.ordinalObject.a_median, self.ordinalObject.b_median,
                       self.ordinalObject.c_median, self.ordinalObject.d_median,
                       self.ordinalObject.e_median]
            stats.append(medians)

        if self.modeBool == True:
            modeText = "Mode A: {}\n" \
                .format(str(self.ordinalObject.a_mode))
            f.write(modeText)
            self.listWidget.addItem(modeText)

            modeText = "Mode B: {}\n" \
                .format(str(self.ordinalObject.b_mode))
            f.write(modeText)
            self.listWidget.addItem(modeText)

            modeText = "Mode C: {}\n" \
                .format(str(self.ordinalObject.c_mode))
            f.write(modeText)
            self.listWidget.addItem(modeText)

            modeText = "Mode D: {}\n" \
                .format(str(self.ordinalObject.d_median))
            f.write(modeText)
            self.listWidget.addItem(modeText)

            modeText = "Mode E: {}\n" \
                .format(str(self.ordinalObject.e_mode))
            f.write(modeText)
            self.listWidget.addItem(modeText)

            headers.append("Mode")
            modes = [self.ordinalObject.a_mode, self.ordinalObject.b_mode,
                       self.ordinalObject.c_mode, self.ordinalObject.d_mode,
                       self.ordinalObject.e_mode]
            stats.append(modes)

        if self.signBool == True:
            signText = "Sign Test: {}\n" \
               .format(str(self.ordinalObject.sign_test))
            f.write(signText)
            self.listWidget.addItem(signText)

            headers.append("Sign Test")
            signs = [self.ordinalObject.sign_test, self.ordinalObject.sign_test, self.ordinalObject.sign_test,
                     self.ordinalObject.sign_test, self.ordinalObject.sign_test]
            stats.append(signs)

        if self.rankSumBool == True:
            rankSumText = "Rank Sum: {}\n" \
               .format(str(self.ordinalObject.rank_sum))
            f.write(rankSumText)
            self.listWidget.addItem(rankSumText)

            headers.append("Rank Sum")
            ranks_sums = [self.ordinalObject.rank_sum, self.ordinalObject.rank_sum, self.ordinalObject.rank_sum,
                          self.ordinalObject.rank_sum, self.ordinalObject.rank_sum]
            stats.append(ranks_sums)

        f.close()

        with open('ordinalResults.csv', 'w', newline='') as csv_file:

            writer = csv.writer(csv_file)

            choices = ['A', 'B', 'C', 'D', 'E']
            stats.insert(0, choices)
            writer.writerow(headers)

            sublist = []
            for x in zip(*stats):
                for y in x:
                    sublist.append(y)
                writer.writerow(sublist)
                sublist = []

    def calcReset(self):
        self.listWidget.clear()

    def get_last_figure_plotted(self):
        self.last_figure_plotted = self.ui.get_last_figure_plotted()
        return self.last_figure_plotted

