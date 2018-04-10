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
        self.initialBox1 = textBoxWrapper()
        self.initialBox2 = textBoxWrapper()
        self.initialBox3 = textBoxWrapper()
        self.pointerBox = self.initialBox1
        self.rowNumber = 1
        self.columnNumber = 3

        self.intervalColumnMin = 3
        self.intervalColumnMax = 3
        self.frequencyColumnMin = 3
        self.frequencyColumnMax = 3
        self.ordinalColumnMin = 3
        self.ordinalColumnMax = 6
        self.columnDistance = 100
        self.rowDistance = 50

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

        self.DataType.addItem("Ordinal")
        self.DataType.addItem("Interval")
        self.DataType.addItem("Frequency")

        self.Submit.setText("Submit")

        self.initialBox1.setParent(self.scrollArea)
        self.initialBox2.setParent(self.scrollArea)
        self.initialBox3.setParent(self.scrollArea)
        self.initialBox1.setRight(self.initialBox2)
        self.initialBox2.setLeft(self.initialBox1)
        self.initialBox2.setRight(self.initialBox3)
        self.initialBox3.setLeft(self.initialBox2)
        self.initialBox2.setText("Test Value1")
        self.initialBox1.setText("Test Name")
        self.initialBox3.setText("Test Value2")

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
        self.initialBox1.move(10, 35)
        self.initialBox2.move(110, 35)
        self.initialBox3.move(210, 35)
        self.initialBox1.setLocation(10, 35)
        self.initialBox2.setLocation(110, 35)
        self.initialBox3.setLocation(220, 35)

        self.RowLabel.setFont(self.LabelFont)
        self.ColumnLabel.setFont(self.LabelFont)

        self.verticalLayout.addWidget(self.scrollArea)

        self.ColumnPlusButton.clicked.connect(self.addColumnClicked)
        self.ColumnMinusButton.clicked.connect(self.removeColumnClicked)
        self.RowPlusButton.clicked.connect(self.addRowClicked)

    def addColumnClicked(self):
        if self.DataType.currentText() == "Ordinal" and self.columnNumber < 6:
            temp = self.pointerBox
            for i in range(self.columnNumber - 1):
                temp = temp.getRight()
            for i in range(self.rowNumber):
                #Making text box appear magic happen
                temp2 = textBoxWrapper()
                temp2.setParent(self.scrollArea)
                temp2.setText("Test" + str(i) + str(self.columnNumber))
                temp2.move(temp.getXLocation()+self.columnDistance, temp.getYLocation())
                temp2.setLocation(temp.getXLocation() + self.columnDistance, temp.getYLocation())
                temp2.show()
                #Linking
                #temp <-> temp2
                temp.setRight(temp2)
                temp2.setLeft(temp)
                #Some element above
                #<->
                #temp2
                if temp.getTop() is not None:
                    temp = temp.getTop()
                    temp = temp.getRight()
                    temp.setBottom(temp2)
                    temp2.setTop(temp)
                    temp = temp2.getRight()
                #move temp
                if temp.getBottom() is not None:
                    temp = temp.getBottom()
            #increment counter
            self.columnNumber = self.columnNumber + 1

    def removeColumnClicked(self):
        if self.columnNumber > 3:
            temp = self.pointerBox
            for i in range(self.columnNumber - 2):
                temp = temp.getRight()
            for i in range(self.rowNumber):
                temp2 = temp.getRight()
                temp.setRight(None)
                temp2.deleteLater()
                temp = temp.getBottom()
            self.columnNumber = self.columnNumber - 1

    def addRowClicked(self):
        temp = self.pointerBox
        for i in range(self.rowNumber - 1):
            temp = temp.getBottom()
        for i in range(self.columnNumber):
            #Making text box appear magic happen
            temp2 = textBoxWrapper()
            temp2.setParent(self.scrollArea)
            temp2.setText("Test" + str(self.rowNumber) + str(i))
            temp2.move(temp.getXLocation(), temp.getYLocation() + self.rowDistance)
            temp2.setLocation(temp.getXLocation(), temp.getYLocation() + self.rowDistance)
            temp2.show()
            #Linking
            #temp
            #<->
            #temp2
            temp.setBottom(temp2)
            temp2.setTop(temp)
            #some element to the left <-> temp2
            if temp.getLeft() is not None:
                temp = temp.getLeft()
                temp = temp.getBottom()
                temp.setRight(temp2)
                temp2.setLeft(temp)
                temp = temp2.getTop()
            if temp.getRight() is not None:
                temp = temp.getRight()
        self.rowNumber = self.rowNumber + 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ManualDataEntry()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())