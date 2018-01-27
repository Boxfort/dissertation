import importlib.util
import math
import os
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Ui_clfSelector import Ui_clfSelector

class QClfSelector(QWidget, Ui_clfSelector):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btn_alg1_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File', os.getcwd(), 'Python scripts (*.py);; All Files (*.*)')
        if filename:
            self.txt_alg1.setText(filename[0])

    def btn_alg2_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File', os.getcwd(), 'Python scripts (*.py);; All files (*.*)')
        if filename:
            self.txt_alg2.setText(filename[0])

    def chk_two_stage_toggled(self):
        self.label.setEnabled(not self.label.isEnabled())
        self.txt_alg2.setEnabled(not self.txt_alg2.isEnabled())
        self.btn_alg2.setEnabled(not self.btn_alg2.isEnabled())

    def run_folds(self, training_set, folds):

        results = []

        if folds == 1:
            results = self.run_classifiers(training_set, training_set)
        else:
            fold_results = []

            # Partitioning Dataset
            fold_size = len(training_set.index) / folds

            for i in range(0, folds):
                print("Running fold " + str(i+1) + " of " + str(folds))
                start = math.floor(i * fold_size)
                end = math.floor((i + 1) * fold_size)
                fold_test_set = training_set[start:end]
                fold_train_set = training_set.copy().drop(training_set.index[start:end])
                result = self.run_classifiers(fold_train_set, fold_test_set)

                if result == []:
                    return

                results += list(result)

        return results

    def run_testing_set(self, training_set, testing_set):
        result = self.run_classifiers(training_set, testing_set)
        return result

    def run_classifiers(self, training_set, testing_set):

        print("Running classfier one...")
        classifier = self.load_module(self.txt_alg1.text())

        stage_one_result = []

        if self.chk_two_stage.isChecked():
            testing_set_flattened = self.flatten_attacks(testing_set)
            training_set_flattened = self.flatten_attacks(training_set)
            stage_one_result = classifier.run(training_set_flattened, testing_set_flattened)
        else:
            stage_one_result = classifier.run(training_set, testing_set)

        if self.chk_two_stage.isChecked():
            # Run second stage
            # Get indices of results where an attack is classified, and construct a new test dataset of only attacks for stage two
            print("Running classifier two...")
            dataset_second_test = testing_set[stage_one_result != 'normal']
            dataset_second_train = training_set[training_set['labels'] != 'normal']

            classifier_two = self.load_module(self.txt_alg2.text())
            stage_two_result = classifier_two.run(dataset_second_train, testing_set)

            stage_two_result[ np.where(stage_one_result == 'normal') ] = 'normal'

            return stage_two_result
        else:
            # Get results from stage one
            return stage_one_result

    def load_module(self, filename):
        spec = importlib.util.spec_from_file_location("module.name", filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def flatten_attacks(self, dataset):
        dataset_flat = dataset.copy() # Copy instead of reference
        mask = dataset_flat['labels'] != 'normal'
        column_name = 'labels'
        dataset_flat.loc[mask, column_name] = 'attack'
        return dataset_flat

