from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import random

conf_arr = np.array([[33,2,0,0,0,0,0,0,0,1,3],
            [3,31,0,0,0,0,0,0,0,0,0],
            [0,4,41,0,0,0,0,0,0,0,1],
            [0,1,0,30,0,6,0,0,0,0,1],
            [0,0,0,0,38,10,0,0,0,0,0],
            [0,0,0,3,1,39,0,0,0,0,4],
            [0,2,2,0,4,1,31,0,0,0,2],
            [0,1,0,0,0,0,0,36,0,2,0],
            [0,0,0,0,0,0,1,5,37,5,1],
            [3,0,0,0,0,0,0,0,0,39,0],
            [0,0,0,0,0,0,0,0,0,0,38]])

class PlotCanvas(FigureCanvas):

    # Take in confusion matrix
    def __init__(self, parent=None, width=5, height=5, dpi=100, matrix):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        ax = self.figure.add_subplot(111)
        width, height = conf_arr.shape

        norm_conf = []
        for i in conf_arr:
            a = 0
            tmp_arr = []
            a = sum(i, 0)
            for j in i:
                tmp_arr.append(float(j)/float(a))
            norm_conf.append(tmp_arr)

        for x in range(width):
            for y in range(height):
                ax.annotate(str(conf_arr[x][y]), xy=(y, x), 
                            horizontalalignment='center',
                            verticalalignment='center')
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        res = ax.imshow(np.array(norm_conf), cmap=plt.cm.jet, 
                interpolation='nearest')

        self.fig.colorbar(res)

        ax.set_xticks(range(width))
        ax.set_xticklabels(alphabet[:width])
        ax.set_yticks(range(width))
        ax.set_yticklabels(alphabet[:width])
        ax.set_ylabel('True Label')
        ax.set_xlabel('Predicted Label')

        ax.set_title('Please help me')
        self.draw()
