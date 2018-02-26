import unittest
from pandas_ml import ConfusionMatrix
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from collections import defaultdict
import pandas as pd
import sys
import os
sys.path.append('../src/')
from QBarChart import QBarChart

app = QApplication(sys.argv)
TEST_FIELDS = os.path.join(os.path.dirname(__file__), 'data/testfields.csv')
TEST_DATASET = os.path.join(os.path.dirname(__file__), 'data/testdataset.csv')
TEST_DATASET2 = os.path.join(os.path.dirname(__file__), 'data/testdataset2.csv')
TEST_ATTACKS = os.path.join(os.path.dirname(__file__), 'data/testattacks.csv')
DUMMY_CLASSIFIER = os.path.join(os.path.dirname(__file__), 'data/dummyclf.py')

class TestQBarChart(unittest.TestCase):

    def test_plot_one_not_stochastic(self):
        stats = [{'FP: False Positive':100,'FN: False Negative':100,'TP: True Positive':100,'TN: True Negative':100}]
        stochastic = [False]
        runs = 1
        test_chart = QBarChart(stats, runs, stochastic)
        test_chart.plot()

    def test_plot_one_stochastic(self):
        stats = [{'FP: False Positive':100,'FN: False Negative':100,'TP: True Positive':100,'TN: True Negative':100}]
        stochastic = [True]
        runs = 2
        test_chart = QBarChart(stats, runs, stochastic)
        test_chart.plot()

    def test_plot_multiple_stochastic(self):
        stats = [{'FP: False Positive':100,'FN: False Negative':100,'TP: True Positive':100,'TN: True Negative':100},{'FP: False Positive':100,'FN: False Negative':100,'TP: True Positive':100,'TN: True Negative':100}]
        stochastic = [True, True]
        runs = 2
        test_chart = QBarChart(stats, runs, stochastic)
        test_chart.plot()

    def test_plot_multiple_not_stochastic(self):
        stats = [{'FP: False Positive':100,'FN: False Negative':100,'TP: True Positive':100,'TN: True Negative':100},{'FP: False Positive':100,'FN: False Negative':100,'TP: True Positive':100,'TN: True Negative':100}]
        stochastic = [False, False]
        runs = 2
        test_chart = QBarChart(stats, runs, stochastic)
        test_chart.plot()

    def test_plot_zero(self):
        stats = [{'FP: False Positive':0,'FN: False Negative':0,'TP: True Positive':0,'TN: True Negative':10}]
        stochastic = [False]
        runs = 2
        test_chart = QBarChart(stats, runs, stochastic)
        test_chart.plot()

    def test_plot_zero_stochastic(self):
        stats = [{'FP: False Positive':0,'FN: False Negative':0,'TP: True Positive':0,'TN: True Negative':10}]
        stochastic = [True]
        runs = 2
        test_chart = QBarChart(stats, runs, stochastic)
        test_chart.plot()


if __name__ == '__main__':
    unittest.main()
