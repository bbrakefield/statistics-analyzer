# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrdinalDataScreen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1082, 666)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.MediancheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.MediancheckBox.setGeometry(QtCore.QRect(10, 30, 85, 18))
        self.MediancheckBox.setObjectName("MediancheckBox")
        self.CalcButtonBox = QtWidgets.QDialogButtonBox(self.groupBox_2)
        self.CalcButtonBox.setGeometry(QtCore.QRect(30, 520, 164, 32))
        self.CalcButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
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
        self.PercentileCheck = QtWidgets.QCheckBox(self.groupBox_2)
        self.PercentileCheck.setGeometry(QtCore.QRect(10, 150, 85, 18))
        self.PercentileCheck.setObjectName("PercentileCheck")
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.graphButtonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.graphButtonBox.setGeometry(QtCore.QRect(50, 520, 164, 32))
        self.graphButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
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
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setMaximumSize(QtCore.QSize(500, 16777215))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Calculations"))
        self.MediancheckBox.setText(_translate("Form", "Median"))
        self.modeCheckBox.setText(_translate("Form", "Mode"))
        self.SignTestCheck.setText(_translate("Form", "Sign Test"))
        self.RankSumCheck.setText(_translate("Form", "Rank Sum"))
        self.PercentileCheck.setText(_translate("Form", "Percentile"))
        self.groupBox.setTitle(_translate("Form", "Graphs"))
        self.verBarRadioB.setText(_translate("Form", "Vertical Bar Chart"))
        self.horBarRadioB.setText(_translate("Form", "Horizontal Bar Chart"))
        self.pieChartRadioB.setText(_translate("Form", "Pie Chart"))
        self.xyPlotRadioB.setText(_translate("Form", "XY Plot"))
        self.normalCurRadioB.setText(_translate("Form", "Normal Curve"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

