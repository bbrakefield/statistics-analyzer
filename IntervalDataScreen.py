"""
Module responsible for generating the view when operating on interval data objects.
"""

# Authors: Jenna McCown
#         Brannon Brakefield

from PyQt5 import QtCore, QtWidgets
from matplottest import *

# =============================================================================
# Interval data screen
# =============================================================================


class Ui_Form1(object):
    """The view that is shown when operating on interval data.
        User will be able to select which stats they wish to see in the report,
        Generate charts, and export data and reports.
    """

    def __init__(self):
        super().__init__()
        self.last_figure_plotted = None

    def setupUi(self, Form, interObject, mainScreenObj):

        self.mainScreenObject = mainScreenObj
        self.col_headers = mainScreenObj.col_headers
        self.row_headers = mainScreenObj.row_headers
        self.medianBool = False
        self.modeBool = False
        self.stanDevBool = False
        self.rankSumBool = False
        self.meanBool = False
        self.percentileBool = False
        self.coeffVarBool = False
        self.spearRankBool = False
        self.corCoeffBool = False
        self.varBool = False
        self.covarBool = False
        self.leastSquareBool = False
        self.pearCorBool = False
        self.verBarBool = False
        self.horBarBool = False
        self.xyPlotBool = False
        self.normalCurBool = False
        self.pieCharBool = False
        self.interObject = interObject
        self.intervalObject = IntervalDataObject(interObject)
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
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calcGroupBox = QtWidgets.QGroupBox(Form)
        self.calcGroupBox.setObjectName("calcGroupBox")
        self.medianCheckBox = QtWidgets.QCheckBox(self.calcGroupBox)
        self.medianCheckBox.setGeometry(QtCore.QRect(10, 60, 85, 18))
        self.medianCheckBox.setObjectName("medianCheckBox")
        self.calcButtonBox = QtWidgets.QDialogButtonBox(self.calcGroupBox)
        self.calcButtonBox.setGeometry(QtCore.QRect(30, 520, 164, 32))
        self.calcButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.Ok)
        self.calcButtonBox.setObjectName("calcButtonBox")
        self.modeCheckBox = QtWidgets.QCheckBox(self.calcGroupBox)
        self.modeCheckBox.setGeometry(QtCore.QRect(10, 90, 85, 18))
        self.modeCheckBox.setObjectName("modeCheckBox")
        self.StanDevCheck = QtWidgets.QCheckBox(self.calcGroupBox)
        self.StanDevCheck.setGeometry(QtCore.QRect(10, 120, 161, 21))
        self.StanDevCheck.setObjectName("StanDevCheck")
        self.RankSumCheck = QtWidgets.QCheckBox(self.calcGroupBox)
        self.RankSumCheck.setGeometry(QtCore.QRect(10, 150, 151, 18))
        self.RankSumCheck.setObjectName("RankSumCheck")
        self.PercentileCheck = QtWidgets.QCheckBox(self.calcGroupBox)
        self.PercentileCheck.setGeometry(QtCore.QRect(10, 390, 85, 18))
        self.PercentileCheck.setObjectName("PercentileCheck")
        self.meanCheckBox = QtWidgets.QCheckBox(self.calcGroupBox)
        self.meanCheckBox.setGeometry(QtCore.QRect(10, 30, 85, 18))
        self.meanCheckBox.setObjectName("meanCheckBox")
        self.CoeffVarCheck = QtWidgets.QCheckBox(self.calcGroupBox)
        self.CoeffVarCheck.setGeometry(QtCore.QRect(10, 210, 161, 18))
        self.CoeffVarCheck.setObjectName("CoeffVarCheck")
        self.SpearRankCheck = QtWidgets.QCheckBox(self.calcGroupBox)
        self.SpearRankCheck.setGeometry(QtCore.QRect(10, 240, 131, 18))
        self.SpearRankCheck.setObjectName("SpearRankCheck")
        self.CorCoeffCheck = QtWidgets.QCheckBox(self.calcGroupBox)
        self.CorCoeffCheck.setGeometry(QtCore.QRect(10, 270, 171, 18))
        self.CorCoeffCheck.setObjectName("CorCoeffCheck")
        self.VarCheckBox = QtWidgets.QCheckBox(self.calcGroupBox)
        self.VarCheckBox.setGeometry(QtCore.QRect(10, 300, 85, 18))
        self.VarCheckBox.setObjectName("VarCheckBox")
        self.CovarCheckBox = QtWidgets.QCheckBox(self.calcGroupBox)
        self.CovarCheckBox.setGeometry(QtCore.QRect(10, 330, 101, 18))
        self.CovarCheckBox.setObjectName("CovarCheckBox")
        self.LeastSquareCheck = QtWidgets.QCheckBox(self.calcGroupBox)
        self.LeastSquareCheck.setGeometry(QtCore.QRect(10, 360, 161, 18))
        self.LeastSquareCheck.setObjectName("LeastSquareCheck")
        self.PearCorCheck = QtWidgets.QCheckBox(self.calcGroupBox)
        self.PearCorCheck.setGeometry(QtCore.QRect(10, 180, 161, 18))
        self.PearCorCheck.setObjectName("PearCorCheck")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.calcGroupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(160, 410, 62, 24))
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setMaximum(0.99)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.percentileLabel = QtWidgets.QLabel(self.calcGroupBox)
        self.percentileLabel.setGeometry(QtCore.QRect(40, 410, 111, 21))
        self.percentileLabel.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.calcGroupBox)
        self.graphsGroupBox = QtWidgets.QGroupBox(Form)
        self.graphsGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphsGroupBox.setCheckable(False)
        self.graphsGroupBox.setObjectName("graphsGroupBox")
        self.graphButtonBox = QtWidgets.QDialogButtonBox(self.graphsGroupBox)
        self.graphButtonBox.setGeometry(QtCore.QRect(50, 520, 164, 32))
        self.graphButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.graphButtonBox.setObjectName("graphButtonBox")
        self.VerBarRadioB = QtWidgets.QRadioButton(self.graphsGroupBox)
        self.VerBarRadioB.setGeometry(QtCore.QRect(20, 40, 141, 18))
        self.VerBarRadioB.setObjectName("VerBarRadioB")
        self.horBarRadioB = QtWidgets.QRadioButton(self.graphsGroupBox)
        self.horBarRadioB.setGeometry(QtCore.QRect(20, 70, 151, 20))
        self.horBarRadioB.setObjectName("horBarRadioB")
        self.PieCharRadioB = QtWidgets.QRadioButton(self.graphsGroupBox)
        self.PieCharRadioB.setGeometry(QtCore.QRect(20, 100, 97, 18))
        self.PieCharRadioB.setObjectName("PieCharRadioB")
        self.xyPlotRadioB = QtWidgets.QRadioButton(self.graphsGroupBox)
        self.xyPlotRadioB.setGeometry(QtCore.QRect(20, 130, 97, 18))
        self.xyPlotRadioB.setObjectName("xyPlotRadioB")
        self.normalCurRadioB = QtWidgets.QRadioButton(self.graphsGroupBox)
        self.normalCurRadioB.setGeometry(QtCore.QRect(20, 160, 121, 18))
        self.normalCurRadioB.setObjectName("normalCurRadioB")

        self.graphButtonBox.raise_()
        self.VerBarRadioB.raise_()
        self.horBarRadioB.raise_()
        self.PieCharRadioB.raise_()
        self.calcGroupBox.raise_()
        self.xyPlotRadioB.raise_()
        self.normalCurRadioB.raise_()

        self.horizontalLayout.addWidget(self.graphsGroupBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 601, 661))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.selectAllButton = QtWidgets.QPushButton(self.calcGroupBox)
        self.selectAllButton.setGeometry(QtCore.QRect(10, 440, 100, 30))
        self.selectAllButton.setObjectName("selectAllButton")

        self.deselectAllButton = QtWidgets.QPushButton(self.calcGroupBox)
        self.deselectAllButton.setGeometry(QtCore.QRect(110, 440, 100, 30))
        self.deselectAllButton.setObjectName("deselectAllButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.calcGroupBox.setTitle(_translate("Form", "Calculations"))
        self.medianCheckBox.setText(_translate("Form", "Median"))
        self.modeCheckBox.setText(_translate("Form", "Mode"))
        self.StanDevCheck.setText(_translate("Form", "Standard Deviation"))
        self.RankSumCheck.setText(_translate("Form", "Rank Sum"))
        self.PercentileCheck.setText(_translate("Form", "Percentile"))
        self.meanCheckBox.setText(_translate("Form", "Mean"))
        self.CoeffVarCheck.setText(_translate("Form", "Coefficient of Variance"))
        self.SpearRankCheck.setText(_translate("Form", "Spearman Rank"))
        self.CorCoeffCheck.setText(_translate("Form", "Correlation Coefficient"))
        self.VarCheckBox.setText(_translate("Form", "Variance"))
        self.CovarCheckBox.setText(_translate("Form", "Covariance"))
        self.LeastSquareCheck.setText(_translate("Form", "Least Square Line"))
        self.PearCorCheck.setText(_translate("Form", "Pearson Correlation"))
        self.graphsGroupBox.setTitle(_translate("Form", "Graphs"))
        self.VerBarRadioB.setText(_translate("Form", "Vertical Bar Chart"))
        self.horBarRadioB.setText(_translate("Form", "Horizontal Bar Chart"))
        self.PieCharRadioB.setText(_translate("Form", "Pie Chart"))
        self.xyPlotRadioB.setText(_translate("Form", "XY Plot"))
        self.normalCurRadioB.setText(_translate("Form", "Normal Curve"))
        self.percentileLabel.setText(_translate("Form", "Desired Percentile:"))
        self.selectAllButton.setText(_translate("Form", "Select All"))
        self.deselectAllButton.setText(_translate("Form", "Deselect All"))

        self.medianCheckBox.stateChanged.connect(self.setMedianBool)
        self.modeCheckBox.stateChanged.connect(self.setModeBool)
        self.StanDevCheck.stateChanged.connect(self.setStanDevBool)
        self.RankSumCheck.stateChanged.connect(self.setRankSumBool)
        self.meanCheckBox.stateChanged.connect(self.setMeanBool)
        self.PercentileCheck.stateChanged.connect(self.setPercentileBool)
        self.CoeffVarCheck.stateChanged.connect(self.setCoeffVarBool)
        self.SpearRankCheck.stateChanged.connect(self.setSpearRankBool)
        self.CorCoeffCheck.stateChanged.connect(self.setCorCoeffBool)
        self.VarCheckBox.stateChanged.connect(self.setVarBool)
        self.CovarCheckBox.stateChanged.connect(self.setCovarBool)
        self.LeastSquareCheck.stateChanged.connect(self.setLeastSquareBool)
        self.PearCorCheck.stateChanged.connect(self.setPearCorBool)
        self.calcButtonBox.accepted.connect(self.calcSubmit)
        self.calcButtonBox.clicked.connect(self.calcReset)
        self.VerBarRadioB.clicked.connect(self.setVerBarBool)
        self.horBarRadioB.clicked.connect(self.setHorBarBool)
        self.PieCharRadioB.clicked.connect(self.setPieCharBool)
        self.xyPlotRadioB.clicked.connect(self.setXYPlotBool)
        self.normalCurRadioB.clicked.connect(self.setNormalCurBool)
        self.graphButtonBox.accepted.connect(self.graphSubmit)
        self.selectAllButton.clicked.connect(self.selectAll)
        self.deselectAllButton.clicked.connect(self.deselectAll)

    def selectAll(self):
        self.meanCheckBox.setChecked(True)
        self.modeCheckBox.setChecked(True)
        self.medianCheckBox.setChecked(True)
        self.StanDevCheck.setChecked(True)
        self.RankSumCheck.setChecked(True)
        self.PercentileCheck.setChecked(True)
        self.CoeffVarCheck.setChecked(True)
        self.CorCoeffCheck.setChecked(True)
        self.VarCheckBox.setChecked(True)
        self.CovarCheckBox.setChecked(True)
        self.SpearRankCheck.setChecked(True)
        self.LeastSquareCheck.setChecked(True)
        self.PearCorCheck.setChecked(True)

    def deselectAll(self):
        self.meanCheckBox.setChecked(False)
        self.modeCheckBox.setChecked(False)
        self.medianCheckBox.setChecked(False)
        self.StanDevCheck.setChecked(False)
        self.RankSumCheck.setChecked(False)
        self.PercentileCheck.setChecked(False)
        self.CoeffVarCheck.setChecked(False)
        self.CorCoeffCheck.setChecked(False)
        self.VarCheckBox.setChecked(False)
        self.CovarCheckBox.setChecked(False)
        self.SpearRankCheck.setChecked(False)
        self.LeastSquareCheck.setChecked(False)
        self.PearCorCheck.setChecked(False)

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

    def graphSubmit(self):

        if self.verBarBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.interObject, 1, 1, self.col_headers, self.row_headers)
            Dialog.exec_()
        elif self.horBarBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.interObject, 1, 2, self.col_headers, self.row_headers)
            Dialog.exec_()
        elif self.pieCharBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.interObject, 1, 3, self.col_headers, self.row_headers)
            Dialog.exec_()
        elif self.xyPlotBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.interObject, 1, 4, self.col_headers, self.row_headers)
            Dialog.exec_()
        elif self.normalCurBool == True:
            Dialog = QtWidgets.QDialog()
            self.ui = App(Dialog, self.interObject, 1, 5, self.col_headers, self.row_headers)
            Dialog.exec_()

    def setMedianBool(self):
        if self.medianBool == True:
            self.medianBool = False
        elif self.medianBool == False:
            self.medianBool = True

    def setModeBool(self):
        if self.modeBool == True:
            self.modeBool = False
        elif self.modeBool == False:
            self.modeBool = True

    def setStanDevBool(self):
        if self.stanDevBool == True:
            self.stanDevBool = False
        elif self.stanDevBool == False:
            self.stanDevBool = True

    def setRankSumBool(self):
        if self.rankSumBool == True:
            self.rankSumBool = False
        elif self.rankSumBool == False:
            self.rankSumBool = True

    def setMeanBool(self):
        if self.meanBool == True:
            self.meanBool = False
        elif self.meanBool == False:
            self.meanBool = True

    def setPercentileBool(self):
        if self.percentileBool == True:
            self.percentileBool = False
        elif self.percentileBool == False:
            self.percentileBool = True

    def setCoeffVarBool(self):
        if self.coeffVarBool == True:
            self.coeffVarBool = False
        elif self.coeffVarBool == False:
            self.coeffVarBool = True

    def setSpearRankBool(self):
        if self.spearRankBool == True:
            self.spearRankBool = False
        elif self.spearRankBool == False:
            self.spearRankBool = True

    def setCorCoeffBool(self):
        if self.corCoeffBool == True:
            self.corCoeffBool = False
        elif self.corCoeffBool == False:
            self.corCoeffBool = True

    def setVarBool(self):
        if self.varBool == True:
            self.varBool = False
        elif self.varBool == False:
            self.varBool = True

    def setCovarBool(self):
        if self.covarBool == True:
            self.covarBool = False
        elif self.covarBool == False:
            self.covarBool = True

    def setLeastSquareBool(self):
        if self.leastSquareBool == True:
            self.leastSquareBool = False
        elif self.leastSquareBool == False:
            self.leastSquareBool = True

    def setPearCorBool(self):
        if self.pearCorBool == True:
            self.pearCorBool = False
        elif self.pearCorBool == False:
            self.pearCorBool = True

    def calcSubmit(self):
        """Write calculation report and show it on the GUI."""

        desiredpercent = self.doubleSpinBox.value()
        headers = ["Phases"]
        stats = []
        report = []

        report.append("===Interval Data Report===\n\n")
        if self.meanBool == True:
            meanText = "Mean X: {}\n" \
                   .format(str(self.intervalObject.mean_x))
            self.listWidget.addItem(meanText)
            report.append(meanText)

            meanText = "Mean Y: {}\n" \
                .format(str(self.intervalObject.mean_y))
            self.listWidget.addItem(meanText)
            report.append(meanText)

            means = ['Mean', self.intervalObject.mean_x, self.intervalObject.mean_y]
            stats.append(means)

        if self.medianBool == True:
            medianText = "Median X: {}\n" \
               .format(str(self.intervalObject.median_x))
            self.listWidget.addItem(medianText)
            report.append(medianText)

            medianText = "Median Y: {}\n" \
                .format(str(self.intervalObject.median_y))
            self.listWidget.addItem(medianText)
            report.append(medianText)

            medians = ['Median', self.intervalObject.median_x, self.intervalObject.median_y]
            stats.append(medians)

        if self.modeBool == True:
            if self.intervalObject.mode_x != None:
                modeText = "Mode X: {}\n" \
                    .format(str(self.intervalObject.mode_x))
                self.listWidget.addItem(modeText)
                report.append(modeText)
                mode_text_x = self.intervalObject.mode_x
            else:
                modeText = "Mode X: There is no mode to be calculated.\n"
                self.listWidget.addItem(modeText)
                report.append(modeText)
                mode_text_x = "None"

            if self.intervalObject.mode_y != None:
                modeText = "Mode Y: {}\n" \
                    .format(str(self.intervalObject.mode_y))
                self.listWidget.addItem(modeText)
                report.append(modeText)
                mode_text_y = self.intervalObject.mode_y

            else:
                modeText = "Mode Y: There is no mode to be calculated.\n"
                self.listWidget.addItem(modeText)
                report.append(modeText)
                mode_text_y = "None"

            modes = ['Mode', mode_text_x, mode_text_y]
            stats.append(modes)

        if self.stanDevBool == True:
            stanDevText = "Standard Deviation X: {}\n" \
                   .format(str(self.intervalObject.standard_dev_x))
            self.listWidget.addItem(stanDevText)
            report.append(stanDevText)

            stanDevText = "Standard Deviation Y: {}\n" \
                .format(str(self.intervalObject.standard_dev_y))
            self.listWidget.addItem(stanDevText)
            report.append(stanDevText)

            stddevs = ['Standard Dev', self.intervalObject.standard_dev_x, self.intervalObject.standard_dev_y]
            stats.append(stddevs)

        if self.rankSumBool == True:
            rankSumText = "Rank Sum: {}\n" \
                   .format(str(self.intervalObject.rank_sum))
            self.listWidget.addItem(rankSumText)
            report.append(rankSumText)

            rank_sums = ['Rank Sum', self.intervalObject.rank_sum, self.intervalObject.rank_sum]
            stats.append(rank_sums)

        if self.pearCorBool == True:
            pearCorText = "Pearson Correlation: {}\n" \
                   .format(str(self.intervalObject.pearson))
            self.listWidget.addItem(pearCorText)

            report.append(pearCorText)

            pearsons = ["Pearson", self.intervalObject.pearson, self.intervalObject.pearson]
            stats.append(pearsons)

        if self.coeffVarBool == True:
            coeffVarText = "Coefficient of Variance X: {}\n" \
                   .format(str(self.intervalObject.coefficient_of_var_x))
            self.listWidget.addItem(coeffVarText)
            report.append((coeffVarText))

            coeffVarText = "Coefficient of Variance Y: {}\n" \
                .format(str(self.intervalObject.coefficient_of_var_y))
            self.listWidget.addItem(coeffVarText)
            report.append((coeffVarText))


            coeffvars = ["Coeff of Var", self.intervalObject.coefficient_of_var_x, self.intervalObject.coefficient_of_var_y]
            stats.append(coeffvars)

        if self.spearRankBool == True:
            spearRankText = "Spearman Rank: {}\n" \
                   .format(str(self.intervalObject.spearman))
            self.listWidget.addItem(spearRankText)
            report.append(spearRankText)

            spearmans = ['Spearman', self.intervalObject.spearman, self.intervalObject.spearman]
            stats.append(spearmans)

        if self.corCoeffBool == True:
            corCoeffText = "Correlation Coefficient: {}\n" \
                   .format(str(self.intervalObject.correlation_coeff))
            self.listWidget.addItem(corCoeffText)
            report.append(corCoeffText)

            corcoeffs = ['Correlation Coeff', self.intervalObject.correlation_coeff, self.intervalObject.correlation_coeff]
            stats.append(corcoeffs)

        if self.varBool == True:
            varText = "Variance X: {}\n" \
                   .format(str(self.intervalObject.variance_x))
            self.listWidget.addItem(varText)
            report.append(varText)

            varText = "Variance Y: {}\n" \
                .format(str(self.intervalObject.variance_y))
            self.listWidget.addItem(varText)
            report.append(varText)

            variences = ['Varience', self.intervalObject.variance_x, self.intervalObject.variance_y]
            stats.append(variences)

        if self.covarBool == True:
            covarText = "Covariance: {}\n" \
                   .format(str(self.intervalObject.covariance))
            self.listWidget.addItem(covarText)
            report.append(covarText)

            covariances = ['Covariance', self.intervalObject.covariance, self.intervalObject.covariance]
            stats.append(covariances)

        if self.leastSquareBool == True:
            leastSquareText = "Least Square Line: {}\n" \
                   .format(str(self.intervalObject.least_square))
            self.listWidget.addItem(leastSquareText)
            report.append(leastSquareText)

            least_squares = ['Least Square Line', self.intervalObject.least_square, self.intervalObject.least_square]
            stats.append(least_squares)

        if self.percentileBool == True:

            percentileText = "Percentile of Pretest: {}\n" \
                   .format(str(self.intervalObject.get_percentileX(desiredpercent)))
            self.listWidget.addItem(percentileText)
            report.append(percentileText)

            percentileText2 = "Percentile of Posttest: {}\n" \
                .format(str(self.intervalObject.get_percentileY(desiredpercent)))
            self.listWidget.addItem(percentileText2)
            report.append(percentileText2)

            percentiles = ['Percentiles', self.intervalObject.get_percentileX(desiredpercent),
                           self.intervalObject.get_percentileY(desiredpercent)]
            stats.append(percentiles)

        self.mainScreenObject.set_report(report)

        phases = ['Stats', 'Pretest', "Posttest"]
        stats.insert(0, phases)

        self.mainScreenObject.set_csv(stats)

    def calcReset(self):
        self.listWidget.clear()

