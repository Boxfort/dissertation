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
from MainWindow import MainWindow

app = QApplication(sys.argv)
TEST_FIELDS = os.path.join(os.path.dirname(__file__), 'data/testfields.csv')
TEST_DATASET = os.path.join(os.path.dirname(__file__), 'data/testdataset.csv')
TEST_DATASET2 = os.path.join(os.path.dirname(__file__), 'data/testdataset2.csv')
TEST_ATTACKS = os.path.join(os.path.dirname(__file__), 'data/testattacks.csv')
DUMMY_CLASSIFIER = os.path.join(os.path.dirname(__file__), 'data/dummyclf.py')

class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self.stdout = sys.stdout
        self.test_window = MainWindow(app)
        sys.stdout = self.stdout #Reset stdout as it breaks testing

    def set_window_defaults(self):
        self.test_window.txt_dataset.setText("")
        self.test_window.plainTextEdit.setPlainText("")
        self.test_window.attacks_filename = ''
        self.test_window.labels_filename = ''
        self.test_window.train_set_filename = ''
        self.test_window.test_set_filename = ''
        self.test_window.runs = 0
        self.test_window.folds = None
        self.graph = None
        self.attacks = defaultdict(list)
        self.test_window.results = []
        self.test_window.binary_cols = []
        self.test_window.nominal_cols = []
        self.test_window.numeric_cols = []

    def test_window_defaults(self):
        self.assertEqual(self.test_window.txt_dataset.toPlainText(),"")
        self.assertEqual(self.test_window.plainTextEdit.toPlainText(),"")
        self.assertEqual(self.test_window.attacks_filename,"")
        self.assertEqual(self.test_window.labels_filename,"")
        self.assertEqual(self.test_window.train_set_filename,"")
        self.assertEqual(self.test_window.test_set_filename,"")
        self.assertEqual(self.test_window.runs,0)
        self.assertEqual(self.test_window.folds,None)
        self.assertEqual(self.test_window.graph,None)
        self.assertEqual(self.test_window.attacks,defaultdict(list))
        self.assertEqual(self.test_window.binary_cols,[])
        self.assertEqual(self.test_window.nominal_cols,[])
        self.assertEqual(self.test_window.numeric_cols,[])
        self.assertEqual(self.test_window.results,[])

    def test_add_page(self):
        self.set_window_defaults()
        self.test_window.add_page()
        self.assertEqual(self.test_window.tab_classifiers.count(), 2)

    def test_on_tab_close_requested(self):
        self.test_window.on_tab_close_requested(1)
        self.assertEqual(self.test_window.tab_classifiers.count(),1)

    def test_add_result_tab(self):
        self.set_window_defaults()
        tab_name = "Test"
        tab_content = "Test"
        self.test_window.add_result_tab(tab_name, tab_content)
        self.assertEqual(self.test_window.tabWidget.count(), 2)
        self.assertEqual(self.test_window.tabWidget.widget(1).children()[1].toPlainText(), "Test")

    def test_construct_graph(self):
        self.set_window_defaults()
        stats = [{'FP: False Positive':100,'FN: False Negative':100,'TP: True Positive':100,'TN: True Negative':100}]
        stochastic = [False]
        self.test_window.construct_graph(stats, stochastic)
        self.assertTrue(self.test_window.graph != None)

    def test_load_columns_from_file(self):
        self.set_window_defaults()
        columns = ['a','b','c','d','labels']
        result = self.test_window.load_columns_from_file(TEST_FIELDS)
        self.assertEqual(result, columns)

    def test_load_dataset_from_file(self):
        self.set_window_defaults()
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        result = self.test_window.load_dataset_from_file(TEST_DATASET, fields)

    def test_one_hot_encoding(self):
        self.set_window_defaults()
        column_names = ['a_a','a_b','a_c','a_d','b','c','d','labels']
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset_oh = self.test_window.one_hot_encoding(dataset)
        self.assertEqual(list(dataset_oh.columns), column_names)

    def test_clean_testing_set(self):
        self.set_window_defaults()
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
        self.assertEqual(list(dataset2_oh.columns), column_names)

    def test_clean_testing_set_no_new_columns(self):
        self.set_window_defaults()
        column_names = ['a_a','a_b','a_c','a_d','b','c','d','labels']
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset_oh = self.test_window.one_hot_encoding(dataset)
        dataset2_oh = self.test_window.clean_testing_set(dataset_oh, dataset_oh)
        self.assertEqual(list(dataset2_oh.columns), column_names)

    def test_load_data_with_folds(self):
        self.set_window_defaults()
        self.test_window.labels_filename = TEST_FIELDS
        self.test_window.train_set_filename = TEST_DATASET
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        self.test_window.folds = 2
        self.test_window.load_data()

    def test_load_data_with_test_set(self):
        self.set_window_defaults()
        self.test_window.labels_filename = TEST_FIELDS
        self.test_window.train_set_filename = TEST_DATASET
        self.test_window.test_set_filename = TEST_DATASET2
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        self.test_window.folds = None
        self.test_window.load_data()

    def test_load_data_with_attacks(self):
        self.set_window_defaults()
        attacks = {'class1':['attack1', 'attack2'], 'class2':['attack3']}
        self.test_window.labels_filename = TEST_FIELDS
        self.test_window.train_set_filename = TEST_DATASET
        self.test_window.attacks_filename = TEST_ATTACKS
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        self.test_window.folds = 2
        self.test_window.load_data()
        self.assertEqual(self.test_window.attacks, attacks)

    def test_get_attack_stats(self):
        self.set_window_defaults()
        expected = ['attack1','attack2','attack3','attack2', 'normal']
        results = ['attack1', 'attack2', 'attack2', 'attack2', 'normal']
        cm = ConfusionMatrix(expected, results)
        self.test_window.get_attacks_stats(cm)

    def test_populate_graph_combo(self):
        self.set_window_defaults()
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset_oh = self.test_window.one_hot_encoding(dataset)
        self.test_window.dataset_train_oh = dataset_oh
        self.test_window.populate_graph_combo()
        items = [self.test_window.cmb_graph_class.itemText(i) for i in range(self.test_window.cmb_graph_class.count())]
        self.assertEqual(['attack1', 'attack2', 'attack3', 'normal'], items)

    def test_btn_show_graph_clicked_single(self):
        self.set_window_defaults()
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset_oh = self.test_window.one_hot_encoding(dataset)
        self.test_window.dataset_train_oh = dataset_oh
        self.test_window.populate_graph_combo()
        self.test_window.results = [[['attack1','attack2','attack3','attack2', 'normal', 'normal'], False]]
        self.test_window.btn_show_graph_clicked()
        self.assertTrue(self.test_window.graph != None)

    def test_btn_show_graph_clicked_multiple(self):
        self.set_window_defaults()
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset_oh = self.test_window.one_hot_encoding(dataset)
        self.test_window.dataset_train_oh = dataset_oh
        self.test_window.populate_graph_combo()
        self.test_window.results = [[['attack1','attack2','attack3','attack2', 'normal', 'normal'], False], [['attack1', 'attack2', 'attack3', 'attack2', 'normal', 'normal'],False]]
        self.test_window.btn_show_graph_clicked()
        self.assertTrue(self.test_window.graph != None)

    def test_btn_show_graph_clicked_stochastic(self):
        self.set_window_defaults()
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        self.test_window.runs = 2
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset_oh = self.test_window.one_hot_encoding(dataset)
        self.test_window.dataset_train_oh = dataset_oh
        self.test_window.populate_graph_combo()
        self.test_window.results = [[['attack1','attack2','attack3','attack2','normal', 'normal','attack1','attack2','attack3','attack2', 'normal','normal'], True]]
        self.test_window.btn_show_graph_clicked()
        self.assertTrue(self.test_window.graph != None)

    def test_btn_run_clicked_single_classifier_single_stage(self):
        self.set_window_defaults()
        self.test_window.labels_filename = TEST_FIELDS
        self.test_window.train_set_filename = TEST_DATASET
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        self.test_window.folds = 1
        self.test_window.load_data()
        self.test_window.tab_classifiers.widget(0).children()[1].txt_alg1.setText(DUMMY_CLASSIFIER)
        self.test_window.btn_run_clicked()

    def test_btn_run_clicked_single_classifier_two_stage(self):
        self.set_window_defaults()
        self.test_window.labels_filename = TEST_FIELDS
        self.test_window.train_set_filename = TEST_DATASET
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        self.test_window.folds = 1
        self.test_window.load_data()
        self.test_window.tab_classifiers.widget(0).children()[1].txt_alg1.setText(DUMMY_CLASSIFIER)
        self.test_window.tab_classifiers.widget(0).children()[1].chk_two_stage.setChecked(True)
        self.test_window.tab_classifiers.widget(0).children()[1].txt_alg2.setText(DUMMY_CLASSIFIER)
        self.test_window.btn_run_clicked()

    def test_btn_run_clicked_multiple_classifiers(self):
        self.set_window_defaults()
        self.test_window.labels_filename = TEST_FIELDS
        self.test_window.train_set_filename = TEST_DATASET
        self.test_window.binary_cols = ['b','c']
        self.test_window.nominal_cols = ['a']
        self.test_window.numeric_cols = ['d']
        self.test_window.folds = 1
        self.test_window.load_data()
        self.test_window.add_page()
        self.test_window.tab_classifiers.widget(0).children()[1].txt_alg1.setText(DUMMY_CLASSIFIER)
        self.test_window.tab_classifiers.widget(1).children()[1].txt_alg1.setText(DUMMY_CLASSIFIER)
        self.test_window.btn_run_clicked()
        self.test_window.on_tab_close_requested(1)

if __name__ == '__main__':
    unittest.main()
