# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrequencyDataScreen.ui'
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
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 85, 18))
        self.checkBox.setObjectName("checkBox")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox_2)
        self.buttonBox.setGeometry(QtCore.QRect(30, 520, 164, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 60, 85, 18))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 90, 161, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 120, 151, 18))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox.raise_()
        self.buttonBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
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

        # self.graphicsView = QtWidgets.QGraphicsView(Form)
        # self.graphicsView.setMaximumSize(QtCore.QSize(500, 16777215))
        # self.graphicsView.setObjectName("graphicsView")
        # self.horizontalLayout.addWidget(self.graphicsView)

        self.qlabel = QtWidgets.QLabel(Form)
        self.qlabel.setMaximumSize(QtCore.QSize(500, 15777215))
        self.qlabel.setObjectName("qlabel")
        self.horizontalLayout.addWidget(self.qlabel)

        self.verticalLayout.addLayout(self.horizontalLayout)

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


