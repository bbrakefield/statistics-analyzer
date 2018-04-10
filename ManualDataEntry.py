from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from textBoxWrapper import textBoxWrapper



class ManualDataEntry(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.scrollArea = QtWidgets.QScrollArea()
        self.RowLabel = QLabel("Rows", self.scrollArea)
        self.ColumnLabel = QLabel("Columns", self.scrollArea)
        self.RowPlusButton = QtWidgets.QPushButton(self.scrollArea)
        self.RowMinusButton = QtWidgets.QPushButton(self.scrollArea)
        self.ColumnPlusButton = QtWidgets.QPushButton(self.scrollArea)
        self.ColumnMinusButton = QtWidgets.QPushButton(self.scrollArea)
        self.LabelFont = QtGui.QFont("Times", 10, QtGui.QFont.Bold)
        self.DataType = QtWidgets.QComboBox(self.scrollArea)
        self.Submit = QtWidgets.QPushButton(self.scrollArea)
        self.rowNumber = 1
        self.columnNumber = 1

    def setupUi(self, Dialog):
        Dialog.setObjectName("UserInputDialog")
        Dialog.resize(800, 600)

        self.verticalLayout.setObjectName("VerticalLayout")

        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setEnabled(True)

        self.DataType.addItem("Interval")
        self.DataType.addItem("Ordinal")
        self.DataType.addItem("Frequency")

        self.Submit.setText("Submit")

        self.RowPlusButton.setText("+")
        self.RowMinusButton.setText("-")
        self.RowPlusButton.setFixedSize(25, 25)
        self.RowMinusButton.setFixedSize(25, 25)
        self.ColumnPlusButton.setText("+")
        self.ColumnMinusButton.setText("-")
        self.ColumnPlusButton.setFixedSize(25, 25)
        self.ColumnMinusButton.setFixedSize(25, 25)

        self.RowLabel.move(10, 10)
        self.RowMinusButton.move(50, 5)
        self.RowPlusButton.move(75, 5)
        self.ColumnLabel.move(110, 10)
        self.ColumnMinusButton.move(168, 5)
        self.ColumnPlusButton.move(193, 5)
        self.DataType.move(250, 7.5)
        self.Submit.move(350, 7.5)

        self.RowLabel.setFont(self.LabelFont)
        self.ColumnLabel.setFont(self.LabelFont)

        self.verticalLayout.addWidget(self.scrollArea)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ManualDataEntry()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())