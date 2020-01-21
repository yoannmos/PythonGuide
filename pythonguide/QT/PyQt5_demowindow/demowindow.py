import sys

from PyQt5 import QtCore, QtWidgets

# from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class DemoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(DemoWindow, self).__init__()
        loadUi(r"pythonguide\QT\PyQt5_demowindow\demowindow.ui", self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        self.label.setText(self.lineEdit.text())


app = QtWidgets.QApplication(sys.argv)
myDemoWindow = DemoWindow()
myDemoWindow.show()
sys.exit(app.exec_())
