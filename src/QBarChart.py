from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

WIDTH = 5
HEIGHT = 4
DPI = 100

class QBarChart(FigureCanvas):

    def __init__(self, stats, runs, stochastic, parent=None ):
        self.fig = Figure(figsize=(WIDTH, HEIGHT), dpi=DPI)
        self.stats = stats
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.stochastic = stochastic
        self.runs = runs
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
            if self.stochastic[count]:
                values = [stat['TP: True Positive']/self.runs, stat['TN: True Negative']/self.runs, stat['FP: False Positive']/self.runs, stat['FN: False Negative']/self.runs]
            else:
                values = [stat['TP: True Positive'], stat['TN: True Negative'], stat['FP: False Positive'], stat['FN: False Negative']]

            bar = ax.bar(a+(.25*count), values, width=0.2, color=[colors[count]], align='center')
            self.autolabel(bar, ax)
            count += 1

        ax.set_ylabel('Number of Detections')
        ax.set_title('Detection Rate')
        ax.set_xticks(np.arange(4))
        ax.set_xticklabels(['TP', 'TN', 'FP', 'FN'])

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


