from __future__ import unicode_literals
import sys
import os
import random
import matplotlib

# Make sure that we are using QT5
matplotlib.use("Qt5Agg")
from PySide2 import QtCore, QtWidgets  # , uic

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

qtCreatorFile = r"pythonguide\QT\PyQt5_Matplotlib\matdemo2.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(
            self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)


class ApplicationWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Matplotlib Widget
        self.main_widget = QtWidgets.QWidget(self)
        # layoutw = QtWidgets.QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=50, height=40, dpi=100)
        self.plotLayout.addWidget(sc)

        # self.Mpl_widget = MyStaticMplCanvas


# ----Main----#
qApp = QtWidgets.QApplication(sys.argv)
aw = ApplicationWindow()
aw.show()
sys.exit(qApp.exec_())
