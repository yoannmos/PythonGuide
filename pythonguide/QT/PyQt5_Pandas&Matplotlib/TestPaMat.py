import sys
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5 import uic, QtWidgets

qtCreatorFile = r"pythonguide\QT\PyQt5_Pandas&Matplotlib\matplot.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Boutton
        self.BouttonImporter.clicked.connect(self.getCSV)
        self.BouttonGraphique.clicked.connect(self.plot)

    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open file", r"pythonguide\QT\PyQt5_Pandas&Matplotlib\matplot.ui",
        )
        if filePath != "":
            self.df = pd.read_csv(str(filePath))

    def plot(self):
        x = self.df["col1"]
        y = self.df["col2"]
        plt.plot(x, y)
        plt.show()
        estad_st = "Statistique de col2 : " + str(self.df["col2"].describe())
        self.resultado.setText(estad_st)


qApp = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(qApp.exec_())
