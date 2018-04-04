# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testing123.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from ordinal import OrdinalDataObject

class Ui_Form2(object):

    def setupUi(self, Form, ordObject):

        self.percentileBool = False
        self.medianbool = False
        self.modeBool = False
        self.rankSumBool = False
        self.signBool = False

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


    def calcSubmit(self):
        f = open("ordinalDataReport.txt", "w")
        f.write("===Ordinal Data Report===\n\n")
        if self.medianbool == True:
            medianText = "Median: {}\n" \
                .format(str(self.ordinalObject.a_median))
            f.write(medianText)
            self.listWidget.addItem(medianText)

        if self.modeBool == True:
            modeText = "Mode: {}\n" \
                .format(str(self.ordinalObject.a_median))
            f.write(modeText)
            self.listWidget.addItem(modeText)

        if self.signBool == True:
            signText = "Sign Test: {}\n" \
               .format(str(self.ordinalObject.sign_test))
            f.write(signText)
            self.listWidget.addItem(signText)

        if self.rankSumBool == True:
            rankSumText = "Rank Sum: {}\n" \
               .format(str(self.ordinalObject.rank_sum))
            f.write(rankSumText)
            self.listWidget.addItem(rankSumText)

        f.close()

    def calcReset(self):
        self.listWidget.clear()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

