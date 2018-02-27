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

class TestDatasetWindow(unittest.TestCase):

    def setUp(self):
        self.test_window = DatasetWindow()

    def set_window_defaults(self):
        self.test_window.train_set_filename = ['','']
        self.test_window.test_set_filename = ['','']
        self.test_window.labels_filename = ['','']
        self.test_window.attacks_filename = ['','']

        self.test_window.txt_train_set.setText('')
        self.test_window.txt_test_set.setText('')
        self.test_window.txt_labels.setText('')
        self.test_window.txt_attacks.setText('')

        self.test_window.spn_folds.setValue(1)
        self.test_window.spn_runs.setValue(1)

        self.test_window.lst_numeric.clear()
        self.test_window.lst_nominal.clear()
        self.test_window.lst_binary.clear()

        self.test_window.spn_folds.setEnabled(True)
        self.test_window.lbl_folds.setEnabled(True)
        self.test_window.txt_test_set.setEnabled(False)
        self.test_window.lbl_testing.setEnabled(False)
        self.test_window.btn_test_set.setEnabled(False)


    def test_window_defaults(self):
        self.assertEqual(self.test_window.train_set_filename, ['',''])
        self.assertEqual(self.test_window.test_set_filename, ['',''])
        self.assertEqual(self.test_window.labels_filename, ['',''])
        self.assertEqual(self.test_window.attacks_filename, ['',''])

        self.assertEqual(self.test_window.txt_train_set.text(), '')
        self.assertEqual(self.test_window.txt_test_set.text(), '')
        self.assertEqual(self.test_window.txt_labels.text(), '')
        self.assertEqual(self.test_window.txt_attacks.text(), '')

        self.assertEqual(self.test_window.spn_folds.value(), 1)
        self.assertEqual(self.test_window.spn_runs.value(), 1)

        self.assertEqual(self.test_window.lst_numeric.count(), 0)
        self.assertEqual(self.test_window.lst_nominal.count(), 0)
        self.assertEqual(self.test_window.lst_binary.count(), 0)

        self.assertTrue(self.test_window.spn_folds.isEnabled())
        self.assertTrue(self.test_window.lbl_folds.isEnabled())
        self.assertFalse(self.test_window.txt_test_set.isEnabled())
        self.assertFalse(self.test_window.lbl_testing.isEnabled())
        self.assertFalse(self.test_window.btn_test_set.isEnabled())


    def test_chk_folds_toggled(self):
        self.set_window_defaults()
        self.test_window.chk_folds_toggled()
        self.assertFalse(self.test_window.spn_folds.isEnabled())
        self.assertFalse(self.test_window.lbl_folds.isEnabled())
        self.assertTrue(self.test_window.txt_test_set.isEnabled())
        self.assertTrue(self.test_window.lbl_testing.isEnabled())
        self.assertTrue(self.test_window.btn_test_set.isEnabled())

    def test_rc_move_numeric_from_numeric(self):
        self.set_window_defaults()
        self.test_window.load_cols(TEST_FIELDS)
        self.test_window.lst_numeric.setCurrentRow(0)
        self.test_window.lastList = self.test_window.lst_numeric
        self.test_window.rc_move_numeric()
        self.assertEqual(self.test_window.lst_nominal.count(), 1)
        self.assertEqual(self.test_window.lst_binary.count(), 2)
        self.assertEqual(self.test_window.lst_numeric.count(), 1)

    def test_rc_move_numeric_from_binary(self):
        self.set_window_defaults()
        self.test_window.load_cols(TEST_FIELDS)
        self.test_window.lst_binary.setCurrentRow(0)
        self.test_window.lastList = self.test_window.lst_binary
        self.test_window.rc_move_numeric()
        self.assertEqual(self.test_window.lst_nominal.count(), 1)
        self.assertEqual(self.test_window.lst_binary.count(), 1)
        self.assertEqual(self.test_window.lst_numeric.count(), 2)

    def test_rc_move_numeric_from_nominal(self):
        self.set_window_defaults()
        self.test_window.load_cols(TEST_FIELDS)
        self.test_window.lst_nominal.setCurrentRow(0)
        self.test_window.lastList = self.test_window.lst_nominal
        self.test_window.rc_move_numeric()
        self.assertEqual(self.test_window.lst_nominal.count(), 0)
        self.assertEqual(self.test_window.lst_binary.count(), 2)
        self.assertEqual(self.test_window.lst_numeric.count(), 2)

    def test_rc_move_binary_from_numeric(self):
        self.set_window_defaults()
        self.test_window.load_cols(TEST_FIELDS)
        self.test_window.lst_numeric.setCurrentRow(0)
        self.test_window.lastList = self.test_window.lst_numeric
        self.test_window.rc_move_binary()
        self.assertEqual(self.test_window.lst_nominal.count(), 1)
        self.assertEqual(self.test_window.lst_binary.count(), 3)
        self.assertEqual(self.test_window.lst_numeric.count(), 0)

    def test_rc_move_binary_from_binary(self):
        self.set_window_defaults()
        self.test_window.load_cols(TEST_FIELDS)
        self.test_window.lst_binary.setCurrentRow(0)
        self.test_window.lastList = self.test_window.lst_binary
        self.test_window.rc_move_binary()
        self.assertEqual(self.test_window.lst_nominal.count(), 1)
        self.assertEqual(self.test_window.lst_binary.count(), 2)
        self.assertEqual(self.test_window.lst_numeric.count(), 1)

    def test_rc_move_binary_from_nominal(self):
        self.set_window_defaults()
        self.test_window.load_cols(TEST_FIELDS)
        self.test_window.lst_nominal.setCurrentRow(0)
        self.test_window.lastList = self.test_window.lst_nominal
        self.test_window.rc_move_binary()
        self.assertEqual(self.test_window.lst_nominal.count(), 0)
        self.assertEqual(self.test_window.lst_binary.count(), 3)
        self.assertEqual(self.test_window.lst_numeric.count(), 1)

    def test_rc_move_nominal_from_numeric(self):
        self.set_window_defaults()
        self.test_window.load_cols(TEST_FIELDS)
        self.test_window.lst_numeric.setCurrentRow(0)
        self.test_window.lastList = self.test_window.lst_numeric
        self.test_window.rc_move_nominal()
        self.assertEqual(self.test_window.lst_nominal.count(), 2)
        self.assertEqual(self.test_window.lst_binary.count(), 2)
        self.assertEqual(self.test_window.lst_numeric.count(), 0)

    def test_rc_move_nominal_from_binary(self):
        self.set_window_defaults()
        self.test_window.load_cols(TEST_FIELDS)
        self.test_window.lst_binary.setCurrentRow(0)
        self.test_window.lastList = self.test_window.lst_binary
        self.test_window.rc_move_nominal()
        self.assertEqual(self.test_window.lst_nominal.count(), 2)
        self.assertEqual(self.test_window.lst_binary.count(), 1)
        self.assertEqual(self.test_window.lst_numeric.count(), 1)

    def test_rc_move_nominal_from_nominal(self):
        self.set_window_defaults()
        self.test_window.load_cols(TEST_FIELDS)
        self.test_window.lst_nominal.setCurrentRow(0)
        self.test_window.lastList = self.test_window.lst_nominal
        self.test_window.rc_move_nominal()
        self.assertEqual(self.test_window.lst_nominal.count(), 1)
        self.assertEqual(self.test_window.lst_binary.count(), 2)
        self.assertEqual(self.test_window.lst_numeric.count(), 1)

    def test_load_cols(self):
        self.set_window_defaults()
        self.test_window.load_cols(TEST_FIELDS)
        self.assertEqual(self.test_window.lst_nominal.count(), 1)
        self.assertEqual(self.test_window.lst_binary.count(), 2)
        self.assertEqual(self.test_window.lst_numeric.count(), 1)

if __name__ == '__main__':
    unittest.main()
