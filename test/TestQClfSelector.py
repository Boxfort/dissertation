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
from QClfSelector import QClfSelector

app = QApplication(sys.argv)
TEST_FIELDS = os.path.join(os.path.dirname(__file__), 'data/testfields.csv')
TEST_DATASET = os.path.join(os.path.dirname(__file__), 'data/testdataset.csv')
TEST_DATASET2 = os.path.join(os.path.dirname(__file__), 'data/testdataset2.csv')
TEST_ATTACKS = os.path.join(os.path.dirname(__file__), 'data/testattacks.csv')
DUMMY_CLASSIFIER = os.path.join(os.path.dirname(__file__), 'data/dummyclf.py')

class TestQClfSelector(unittest.TestCase):

    def setUp(self):
        self.stdout = sys.stdout
        self.test_widget = QClfSelector()
        self.test_window = MainWindow(app)
        sys.stdout = self.stdout #Reset stdout as it breaks testing

    def set_widget_defaults(self):
        self.test_widget.txt_alg1.setText("")
        self.test_widget.txt_alg2.setText("")
        self.test_widget.chk_two_stage.setChecked(False)
        self.test_widget.label.setEnabled(False)
        self.test_widget.txt_alg2.setEnabled(False)
        self.test_widget.btn_alg2.setEnabled(False)
        self.test_widget.classifier_one = None
        self.test_widget.classifier_one = None

    def test_widget_defaults(self):
        self.assertEqual(self.test_widget.txt_alg1.text(), "")
        self.assertEqual(self.test_widget.txt_alg2.text(), "")
        self.assertFalse(self.test_widget.chk_two_stage.isChecked())
        self.assertFalse(self.test_widget.label.isEnabled())
        self.assertFalse(self.test_widget.txt_alg2.isEnabled())
        self.assertFalse(self.test_widget.btn_alg2.isEnabled())
        self.assertEqual(self.test_widget.classifier_one, None)
        self.assertEqual(self.test_widget.classifier_two, None)

    def test_flatten_attacks(self):
        self.set_widget_defaults()
        labels = ['attack','attack','attack','attack','normal','normal']
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        dataset_flat = self.test_widget.flatten_attacks(dataset)
        self.assertEqual(list(dataset_flat['labels']), labels)

    def test_chk_two_stage_toggled(self):
        self.test_widget.chk_two_stage_toggled()
        self.assertTrue(self.test_widget.label.isEnabled())
        self.assertTrue(self.test_widget.txt_alg2.isEnabled())
        self.assertTrue(self.test_widget.btn_alg2.isEnabled())

    def test_load_module(self):
        self.set_widget_defaults()
        result = self.test_widget.load_module(DUMMY_CLASSIFIER)
        self.assertTrue(result != None)

    def test_load_modules_single(self):
        self.set_widget_defaults()
        self.test_widget.txt_alg1.setText(DUMMY_CLASSIFIER)
        self.test_widget.txt_alg2.setText(DUMMY_CLASSIFIER)
        self.test_widget.load_modules()

    def test_load_modules_two_stage(self):
        self.set_widget_defaults()
        self.test_widget.txt_alg1.setText(DUMMY_CLASSIFIER)
        self.test_widget.chk_two_stage.setChecked(True)
        self.test_widget.txt_alg2.setText(DUMMY_CLASSIFIER)
        self.test_widget.load_modules()

    def test_self_run_classifiers(self):
        self.set_widget_defaults()
        labels = ['attack1','attack2','attack3','attack2','normal','normal']
        self.test_widget.txt_alg1.setText(DUMMY_CLASSIFIER)
        self.test_widget.load_modules()
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        result = self.test_widget.run_classifiers(dataset,dataset)
        self.assertEqual(list(result),labels)

    def test_self_run_classifiers_two_stage(self):
        self.set_widget_defaults()
        labels = ['attack1','attack2','attack3','attack2','normal','normal']
        self.test_widget.txt_alg1.setText(DUMMY_CLASSIFIER)
        self.test_widget.chk_two_stage.setChecked(True)
        self.test_widget.txt_alg2.setText(DUMMY_CLASSIFIER)
        self.test_widget.load_modules()
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        result = self.test_widget.run_classifiers(dataset,dataset.copy())
        self.assertEqual(list(result),labels)

    def test_run_folds_one(self):
        self.set_widget_defaults()
        labels = ['attack1','attack2','attack3','attack2','normal','normal']
        self.test_widget.txt_alg1.setText(DUMMY_CLASSIFIER)
        self.test_widget.load_modules()
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        result = self.test_widget.run_folds(dataset, 1)
        self.assertEqual(list(result), labels)

    def test_run_folds_many(self):
        self.set_widget_defaults()
        labels = ['attack1','attack2','attack3','attack2','normal','normal']
        self.test_widget.txt_alg1.setText(DUMMY_CLASSIFIER)
        self.test_widget.load_modules()
        fields = self.test_window.load_columns_from_file(TEST_FIELDS)
        dataset = self.test_window.load_dataset_from_file(TEST_DATASET, fields)
        result = self.test_widget.run_folds(dataset, 2)
        self.assertEqual(result, labels)

if __name__ == '__main__':
    unittest.main()
