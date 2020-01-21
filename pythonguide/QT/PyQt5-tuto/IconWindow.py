import sys

# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtGui


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QtGui.QIcon(r"pythonguide\QT\PyQt5-tuto\icon.png"))

        self.show()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
