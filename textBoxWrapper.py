from PyQt5.QtWidgets import QLineEdit


class textBoxWrapper(QLineEdit):
    def __init__(self):
        super(QLineEdit, self).__init__()
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.xLocation = None
        self.yLocation = None

    def getTop(self):
        return self.top

    def getBottom(self):
        return self.bottom

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setTop(self, newTop):
        self.top = newTop

    def setBottom(self, newBottom):
        self.bottom = newBottom

    def setLeft(self, newLeft):
        self.left = newLeft

    def setRight(self, newRight):
        self.right = newRight

    def setXLocation(self, newX):
        self.xLocation = newX

    def setYLocation(self, newY):
        self.yLocation = newY

    def getXLocation(self):
        return self.xLocation

    def getYLocation(self):
        return self.yLocation

    def setLocation(self, newX, newY):
        self.xLocation = newX
        self.yLocation = newY
