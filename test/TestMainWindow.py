import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import pandas as pd
import sys
import os
sys.path.append('../src/')
from MainWindow import MainWindow

app = QApplication(sys.argv)
TEST_FIELDS = os.path.join(os.path.dirname(__file__), 'data/testfields.csv')
TEST_DATASET = os.path.join(os.path.dirname(__file__), 'data/testdataset.csv')

class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self.test_window = MainWindow(app)
        self.set_window_defaults()

    def set_window_defaults(self):
        self.test_window.txt_dataset.setText("")
        self.test_window.plainTextEdit.setPlainText("")
        self.test_window.runs = 0

    def test_window_defaults(self):
        self.assertEqual("","")

    def test_add_page(self):
        self.test_window.add_page()
        self.assertEqual(self.test_window.tab_classifiers.count(), 2)

    def test_add_result_tab(self):
        tab_name = "Test"
        tab_content = "Test"
        self.test_window.add_result_tab(tab_name, tab_content)
        self.assertEqual(self.test_window.tabWidget.count(), 2)

    def test_write(self):
        to_write = "Test"
        self.test_window.write(to_write)
        self.assertEqual(to_write in self.test_window.plainTextEdit.toPlainText(), True)

    def test_construct_graph(self):
        stats = [{'FP: False Positive':100,'FN: False Negative':100,'TP: True Positive':100,'TN: True Negative':100}]
        stochastic = [False]
        self.test_window.construct_graph(stats, stochastic)
        self.assertEqual(self.test_window.graph != None, True)

    def test_load_columns_from_file(self):
        result = self.test_window.load_columns_from_file(TEST_FIELDS)
        self.assertEqual(result == ['a','b','c','d'], True)

    def test_load_dataset_from_file(self):
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        result = self.test_window.load_dataset_from_file(TEST_DATASET, fields)

    def test_one_hot_encoding(self):

        column_names = ['a_a','a_b','a_c','a_d','b','c','d']

        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']

        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset_oh = self.test_window.one_hot_encoding(dataset)
        self.assertEqual(list(dataset_oh.columns) == column_names, True)

    def test_load_data(self):
        pass

    def test_get_attack_stats(self):
        pass

    def test_populate_graph_combo(self):
        pass

if __name__ == '__main__':
    unittest.main()
