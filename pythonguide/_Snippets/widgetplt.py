import sys

# import matplotlib.pyplot as plt
import matplotlib.cm as cm

# E1101:Module 'matplotlib.cm' has no 'rainbow' member
# ----> Is ok, matplotlib.cm does the following to adds its attributes:
import matplotlib

# import matplotlib.figure
import numpy as np

# DIFF ???? from matplotlib.backends.qt_compat import QtWidgets
from PySide2 import QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from matplotlib.collections import PatchCollection


class WidgetPlt(QtWidgets.QWidget):
    def __init__(self, tool=1):
        super().__init__()
        self.tool = tool
        self.initUi()

    def initUi(self):
        layout = QtWidgets.QVBoxLayout()

        # ----------------------------------------------------------

        self.figure = matplotlib.figure.Figure(figsize=(4, 2))
        self.canvas = FigureCanvas(self.figure)
        # self.canvas = FigureCanvas(Figure(figsize=(4, 2)))
        # ----------------------------------------------------------
        layout.addWidget(self.canvas)
        if self.tool == 1:
            layout.addWidget(NavigationToolbar(self.canvas, self))
        self.setLayout(layout)

    def simpleplot(self, x, y):
        self.canvas.figure.clf()

        self.canvas.figure.subplots().plot(x, y, "-")
        self.canvas.draw()

    def plotpanda(self, df, first_data_label, other_data_label, selectspeed):
        self.canvas.figure.clf()
        ax = self.canvas.figure.subplots()
        # pylint: disable=maybe-no-member
        colors = iter(cm.rainbow(np.linspace(0, 1, len(df.columns))))
        # pylint: enable=maybe-no-member
        for i in range(1, len(df.columns)):
            ax.plot(df.iloc[:, 0], df.iloc[:, i], "o-", color=next(colors))

        ax.legend()
        ax.set_xlabel(first_data_label)
        ax.set_ylabel(other_data_label)
        ax.set_title(selectspeed)

        self.canvas.draw()

    def plotpatchcollection(self, mypatches, mycolors=[], mylw=[]):
        self.canvas.figure.clf()
        ax = self.canvas.figure.subplots()

        p = PatchCollection(mypatches)  # , alpha=0.4)
        p.set_facecolor(tuple(mycolors))
        p.set_linewidth(mylw)

        ax.add_collection(p)
        ax.autoscale(enable=True, axis="both", tight=None)

        self.canvas.draw()

    def plotimage(self, image, marker=[]):
        self.canvas.figure.clf()
        ax = self.canvas.figure.subplots()

        if marker != []:
            markers = marker
            x, y = zip(*markers)
            ax.plot(x, y, "o", color="red")

        ax.imshow(image)
        ax.axis("off")

        self.canvas.draw()


if __name__ == "__main__":

    import numpy as np

    x = np.linspace(start=0, stop=np.pi, num=101)
    y = np.sin(2 * x)
    qapp = QtWidgets.QApplication(sys.argv)
    app = WidgetPlt()
    app.simpleplot(x, y)
    app.show()
    qapp.exec_()
