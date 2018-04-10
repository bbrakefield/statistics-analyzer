from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from textBoxWrapper import textBoxWrapper



class ManualDataEntry(QDialog):
    def __init__(self):
        super().__init__()

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
        self.rowDistance = 30

    def setupUi(self, Dialog):


        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
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
        self.initialBox3.setLocation(210, 35)

        self.RowLabel.setFont(self.LabelFont)
        self.ColumnLabel.setFont(self.LabelFont)

        self.verticalLayout.addWidget(self.scrollArea)

        self.ColumnPlusButton.clicked.connect(self.addColumnClicked)
        self.ColumnMinusButton.clicked.connect(self.removeColumnClicked)
        self.RowPlusButton.clicked.connect(self.addRowClicked)
        self.RowMinusButton.clicked.connect(self.removeRowClicked)
        self.Submit.clicked.connect(self.submitButtonClicked)

    def addColumnClicked(self):
        if self.DataType.currentText() == "Ordinal" and self.columnNumber < 6:
            temp = self.pointerBox
            for i in range(self.columnNumber - 1):
                temp = temp.getRight()
            for i in range(self.rowNumber):
                #Making text box appear magic happen
                newBox = textBoxWrapper()
                newBox.setParent(self.scrollArea)
                newBox.setText("Test" + str(i) + str(self.columnNumber))
                newBox.move(temp.getXLocation()+self.columnDistance, temp.getYLocation())
                newBox.setLocation(temp.getXLocation() + self.columnDistance, temp.getYLocation())
                newBox.show()
                #Linking
                #temp <-> temp2
                temp.setRight(newBox)
                newBox.setLeft(temp)
                #Some element above
                #<->
                #newBox
                if temp.getTop() is not None:
                    temp = temp.getTop()
                    temp = temp.getRight()
                    temp.setBottom(newBox)
                    newBox.setTop(temp)
                    temp = newBox.getLeft()
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
            newBox = textBoxWrapper()
            newBox.setParent(self.scrollArea)
            newBox.setText("Test" + str(self.rowNumber) + str(i))
            newBox.move(temp.getXLocation(), temp.getYLocation() + self.rowDistance)
            newBox.setLocation(temp.getXLocation(), temp.getYLocation() + self.rowDistance)
            newBox.show()
            #Linking
            #temp
            #<->
            #newBox
            temp.setBottom(newBox)
            newBox.setTop(temp)
            #some element to the left <-> temp2
            if temp.getLeft() is not None:
                temp = temp.getLeft()
                temp = temp.getBottom()
                temp.setRight(newBox)
                newBox.setLeft(temp)
                temp = newBox.getTop()
            if temp.getRight() is not None:
                temp = temp.getRight()
        self.rowNumber = self.rowNumber + 1

    def removeRowClicked(self):
        if self.rowNumber > 1:
            temp = self.pointerBox
            for i in range(self.rowNumber - 2):
                temp = temp.getBottom()
            for i in range(self.columnNumber):
                temp2 = temp.getBottom()
                temp.setBottom(None)
                temp2.deleteLater()
                temp = temp.getRight()
            self.rowNumber = self.rowNumber - 1

    def submitButtonClicked(self):
        str = ""
        column = self.pointerBox
        row = self.pointerBox
        for i in range(self.rowNumber):
            for i in range(self.columnNumber):
                if i != self.columnNumber-1:
                    str = str + column.text() + ", "
                else:
                    str = str + column.text() + "\n"
                column = column.getRight()
            row = row.getBottom()
            column = row


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ManualDataEntry()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())