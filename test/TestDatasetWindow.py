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
from DatasetWindow import DatasetWindow

app = QApplication(sys.argv)
TEST_FIELDS = os.path.join(os.path.dirname(__file__), 'data/testfields.csv')
TEST_DATASET = os.path.join(os.path.dirname(__file__), 'data/testdataset.csv')
TEST_DATASET2 = os.path.join(os.path.dirname(__file__), 'data/testdataset2.csv')
TEST_ATTACKS = os.path.join(os.path.dirname(__file__), 'data/testattacks.csv')
DUMMY_CLASSIFIER = os.path.join(os.path.dirname(__file__), 'data/dummyclf.py')

class TestDatasetWindow(unittest.TestCase):

    def setUp():
        pass

if __name__ == '__main__':
    unittest.main()
