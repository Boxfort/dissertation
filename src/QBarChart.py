from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class QBarChart(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
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

        N = 3
        menMeans = (20, 35, 30, 35, 27)
        womenMeans = (25, 32, 34, 20, 25)
        menStd = (2, 3, 4, 1, 2)
        womenStd = (3, 5, 2, 3, 3)
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence

        pos = [0, 1, 2]

        x=[4,9,2]
        y=[1,2,3]
        z=[11,12,13]

        a = np.arange(3)

        s1 = ax.bar(a-.25, x, width=0.2, color='r', align='center')
        s2 = ax.bar(a, y, width=0.2, color='g', align='center')
        s3 = ax.bar(a+.25, z, width=0.2, color='b', align='center')

        #p1 = ax.bar(ind, menMeans, width, color='#d62728', yerr=menStd)
        #p2 = ax.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)

        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(np.arange(3))
        ax.set_xticklabels(['x', 'y', 'z'])
        ax.legend((s1[0], s2[0], s3[0]), ('x', 'y', 'z'))

        self.draw()
