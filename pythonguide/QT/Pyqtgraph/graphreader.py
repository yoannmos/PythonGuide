from PyQt5 import QtCore, QtWidgets
#from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi

import sys
import pyqtgraph
import pandas as pd
 
class GraphApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
        super(GraphApp, self).__init__(parent)
        loadUi('graphreader.ui',self)
        self.btnOpen.clicked.connect(self.openfile)
        self.btnLoad.clicked.connect(self.load)
        self.grPlot.plotItem.showGrid(True, True, 0.7)

    def openfile(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.fileDir.setText(str(self.fname[0]))
    
    def load(self):
        df = pd.read_excel(self.fname[0], index_col=None, na_values=['NA'])
        X = df['X']     
        Y = df['Y']         
        pen=pyqtgraph.mkPen(color="b",width=1)
        self.grPlot.plot(X,Y,pen=pen,clear=True)

 

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = GraphApp()
    form.show()
    #form.load() #start with something
    app.exec_()
    print("Program manually closed")