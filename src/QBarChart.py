from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

WIDTH = 5
HEIGHT = 4
DPI = 100

class QBarChart(FigureCanvas):

    def __init__(self, stats, parent=None ):
        self.fig = Figure(figsize=(WIDTH, HEIGHT), dpi=DPI)
        self.stats = stats
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        ax = self.figure.add_subplot(111)
        ax.set_yscale("log", nonposy='clip')

        x=[4,9,2]
        y=[1,2,3]
        z=[11,12,13]

        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

        a = np.arange(4)

        series = []

        count = 0

        for stat in self.stats:
            values = [stat['TP: True Positive'], stat['TN: True Negative'], stat['FP: False Positive'], stat['FN: False Negative']]
            bar = ax.bar(a+(.25*count), values, width=0.2, color=[colors[count]], align='center')
            #self.autolabel(bar, ax)
            count += 1
            print(values)

        #s1 = ax.bar(a-.25, x, width=0.2, color='r', align='center')
        #s2 = ax.bar(a, y, width=0.2, color='g', align='center')
        #s3 = ax.bar(a+.25, z, width=0.2, color='b', align='center')

        #p1 = ax.bar(ind, menMeans, width, color='#d62728', yerr=menStd)
        #p2 = ax.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)

        ax.set_ylabel('Number of Detections')
        ax.set_title('Detection Rate', fontsize=24)
        ax.set_xticks(np.arange(4))
        ax.set_xticklabels(['TP', 'TN', 'FP', 'FN'])
        #ax.legend((s1[0], s2[0], s3[0]), ('x', 'y', 'z'))
        #ax.set_xticklabels(np.arrange(len(series)))
        #ax.legend(series, np.arrange(len(series)))

        self.draw()


    def autolabel(self, rects, ax):
        # Get y-axis height to calculate label position from.
        (y_bottom, y_top) = ax.get_ylim()
        y_height = y_top - y_bottom

        for rect in rects:
            height = rect.get_height()

            # Fraction of axis height taken up by this rectangle
            p_height = (height / y_height)

            # If we can fit the label above the column, do that;
            # otherwise, put it inside the column.
            if p_height > 0.95: # arbitrary; 95% looked good to me.
                label_position = height - (y_height * 0.15)
            else:
                label_position = height + (y_height * 0.01)

            ax.text(rect.get_x() + rect.get_width()/2., label_position,
                    '%d' % int(height),
                    ha='center', va='bottom')

    def autolabel2(self, rects, ax):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%d' % int(height),
                    ha='center', va='bottom')


