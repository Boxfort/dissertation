import unittest
from pandas_ml import ConfusionMatrix
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
TEST_DATASET2 = os.path.join(os.path.dirname(__file__), 'data/testdataset2.csv')
TEST_ATTACKS = os.path.join(os.path.dirname(__file__), 'data/testattacks.csv')

class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self.stdout = sys.stdout
        self.test_window = MainWindow(app)
        self.set_window_defaults()

    def set_window_defaults(self):
        self.test_window.txt_dataset.setText("")
        self.test_window.plainTextEdit.setPlainText("")
        self.test_window.attacks_filename = ''
        self.test_window.labels_filename = ''
        self.test_window.train_set_filename = ''
        self.test_window.test_set_filename = ''
        self.test_window.runs = 0
        self.test_window.folds = None
        self.test_window.binary_cols = []
        self.test_window.nominal_cols = []
        self.test_window.numeric_cols = []

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
        self.assertTrue(to_write in self.test_window.plainTextEdit.toPlainText())

    def test_construct_graph(self):
        stats = [{'FP: False Positive':100,'FN: False Negative':100,'TP: True Positive':100,'TN: True Negative':100}]
        stochastic = [False]
        self.test_window.construct_graph(stats, stochastic)
        self.assertTrue(self.test_window.graph != None)

    def test_load_columns_from_file(self):
        result = self.test_window.load_columns_from_file(TEST_FIELDS)
        self.assertTrue(result == ['a','b','c','d','labels'])

    def test_load_dataset_from_file(self):
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        result = self.test_window.load_dataset_from_file(TEST_DATASET, fields)

    def test_one_hot_encoding(self):
        column_names = ['a_a','a_b','a_c','a_d','b','c','d','labels']
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset_oh = self.test_window.one_hot_encoding(dataset)
        self.assertTrue(list(dataset_oh.columns) == column_names)

    def test_clean_testing_set(self):
        column_names = ['a_a','a_b','a_c','a_d','b','c','d','labels']
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset2 = self.test_window.load_dataset_from_file(TEST_DATASET2, fields)
        dataset_oh = self.test_window.one_hot_encoding(dataset)
        dataset2_oh = self.test_window.one_hot_encoding(dataset2)
        self.assertFalse(list(dataset2_oh.columns) == column_names)
        dataset2_oh = self.test_window.clean_testing_set(dataset_oh, dataset2_oh)
        self.assertTrue(list(dataset2_oh.columns) == column_names)

    def test_clean_testing_set_no_new_columns(self):
        column_names = ['a_a','a_b','a_c','a_d','b','c','d','labels']
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset_oh = self.test_window.one_hot_encoding(dataset)
        dataset2_oh = self.test_window.clean_testing_set(dataset_oh, dataset_oh)
        self.assertTrue(list(dataset2_oh.columns) == column_names)

    def test_load_data_with_folds(self):
        self.test_window.labels_filename = TEST_FIELDS
        self.test_window.train_set_filename = TEST_DATASET
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        self.test_window.folds = 2
        self.test_window.load_data()

    def test_load_data_with_test_set(self):
        self.test_window.labels_filename = TEST_FIELDS
        self.test_window.train_set_filename = TEST_DATASET
        self.test_window.test_set_filename = TEST_DATASET2
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        self.test_window.folds = None
        self.test_window.load_data()

    def test_load_data_with_attacks(self):
        attacks = {'class1':['attack1', 'attack2'], 'class2':['attack3']}
        self.test_window.labels_filename = TEST_FIELDS
        self.test_window.train_set_filename = TEST_DATASET
        self.test_window.attacks_filename = TEST_ATTACKS
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        self.test_window.folds = 2
        self.test_window.load_data()
        self.assertTrue(self.test_window.attacks == attacks)

    def test_get_attack_stats(self):
        expected = ['attack1','attack2','attack3','attack2']
        results = ['attack1', 'attack2', 'attack2', 'attack2']
        cm = ConfusionMatrix(expected, results)
        self.test_window.get_attacks_stats(cm)

    def test_populate_graph_combo(self):
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset_oh = self.test_window.one_hot_encoding(dataset)
        self.test_window.dataset_train_oh = dataset_oh
        self.test_window.populate_graph_combo()
        items = [self.test_window.cmb_graph_class.itemText(i) for i in range(self.test_window.cmb_graph_class.count())]
        self.assertEqual(['attack1', 'attack2', 'attack3'], items)
        pass

if __name__ == '__main__':
    unittest.main()
