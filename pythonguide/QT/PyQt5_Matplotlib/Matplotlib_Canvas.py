
import sys
import numpy as np

from PySide2 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class QtMplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        # Standard Matplotlib code to generate the plot
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.x = np.arange(0.0, 3.0, 0.01)
        self.y = np.cos(2*np.pi*self.x)
        self.axes.plot(self.x, self.y)
        # initialize the canvas where the Figure renders into
        FigureCanvasQTAgg.__init__(self, self.fig)

# Create the GUI application
qApp = QtWidgets.QApplication(sys.argv)
# Create the Matplotlib widget
mpl = QtMplCanvas()
# show the widget
mpl.show()
# start the Qt main loop execution, exiting from this script with the same return code of Qt application
sys.exit(qApp.exec_())