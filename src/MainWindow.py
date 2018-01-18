import sys
import os
import math
import importlib.util
import csv
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from sklearn.metrics import classification_report
from Ui_MainWindow import Ui_MainWindow
from DatasetWindow import DatasetWindow
from ErrorMessage import ErrorMessage

# TODO: k-fold cross validation.
#     : classification reporting
#     : Graphs and results
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.train_set_filename = ''
        self.test_set_filename = ''
        self.labels_filename = ''
        self.numeric_cols = []
        self.nominal_cols = []
        self.binary_cols = []

        sys.stdout = self
        self.app = app

    def write(self, txt):
        self.plainTextEdit.insertPlainText(txt)
        # Tell the GUI to refresh
        self.app.processEvents()

    def btn_dataset_clicked(self):
        dataset_window = DatasetWindow()

        # Dataset accepted so grab data
        if dataset_window.show(self.train_set_filename, self.test_set_filename, self.labels_filename, self.numeric_cols, self.nominal_cols, self.binary_cols) == QDialog.Accepted:

            self.txt_dataset.clear()
            self.test_set_filename = ''
            self.folds = None

            # Grab training set
            self.train_set_filename = dataset_window.train_set_filename[0]
            with open(self.train_set_filename, 'r') as file:
                row_count = sum(1 for row in file)
                self.txt_dataset.append("Training set rows: "+str(row_count))

            # Test is optional so check
            if not dataset_window.test_set_filename[0] == '':
                # Grab test set
                self.test_set_filename = dataset_window.test_set_filename[0]
                with open(self.test_set_filename, 'r') as file:
                    row_count = sum(1 for row in file)
                    self.txt_dataset.append("Training set rows: "+str(row_count))

            # No testing set so grab fold count
            else:
                self.folds = dataset_window.spn_folds.value()

            # Grab labels
            self.labels_filename = dataset_window.labels_filename[0]
            with open(self.labels_filename, 'r') as file:
                row_count = sum(1 for row in file)
                self.txt_dataset.append("Labels: "+str(row_count))

            # Grab categorised labels
            self.nominal_cols = []
            for index in range(dataset_window.lst_nominal.count()):
                self.nominal_cols.append(dataset_window.lst_nominal.item(index).text())

            self.binary_cols = []
            for index in range(dataset_window.lst_binary.count()):
                self.binary_cols.append(dataset_window.lst_binary.item(index).text())

            self.numeric_cols = []
            for index in range(dataset_window.lst_numeric.count()):
                self.numeric_cols.append(dataset_window.lst_numeric.item(index).text())

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

    def btn_run_clicked(self):
        # Load datasets
        print("Loading data...")
        try:
            self.load_data()
        except Exception as e:
            msg = ErrorMessage("Failed to load dataset.", str(e))
            msg.show()
            return

        # Check if the first algorithm file exists
        if not os.path.isfile(self.txt_alg1.text()):
            msg = ErrorMessage("Classifier one file does not exist!")
            msg.show()
            return

        # If two stage is selected check if the second algorithm file exists
        if self.chk_two_stage.isChecked() and not os.path.isfile(self.txt_alg2.text()):
            msg = ErrorMessage("Classifier two file does not exist!")
            msg.show()
            return

        # TODO: Gather and average results from all folds
        if self.folds:
            # Partitioning Dataset
            fold_size = len(self.dataset_train_oh.index) / self.folds

            for i in range(0, self.folds):
                start = math.floor(i * fold_size)
                end = math.floor((i + 1) * fold_size)
                fold_test_set = self.dataset_train_oh[start:end]
                fold_train_set = self.dataset_train_oh.copy().drop(self.dataset_train_oh.index[start:end])
                print("len sub : " + str(len(fold_train_set.index)))
                print("len ful : " + str(len(self.dataset_train_oh.index)))
                self.run_classifiers(fold_train_set, fold_test_set)
        else:
            self.run_classifiers(self.dataset_train_oh, self.dataset_test_oh)


    def run_classifiers(self, training_set, testing_set):
        try:
            print("Running classfier one...")
            classifier = self.load_module(self.txt_alg1.text())

            if self.chk_two_stage.isChecked():
                testing_set_flattened = self.flatten_attacks(testing_set)
                training_set_flattened = self.flatten_attacks(training_set)
                self.stage_one_result = classifier.run(training_set_flattened, testing_set_flattened)
            else:
                self.stage_one_result = classifier.run(training_set, testing_set)

        except Exception as e:
            msg = ErrorMessage("Failed to run classifier one.", str(e))
            msg.show()
            return

        # TODO: If subset has no normal traffic it crashes fix this !
        # Get indices of results where an attack is classified, and construct a new test dataset of only attacks for stage two
        self.dataset_second_test = testing_set.loc[self.stage_one_result != 'normal']
        self.dataset_second_train = training_set.loc[training_set['labels'] != 'normal']

        if self.chk_two_stage.isChecked():
            # Run second stage
            # Get indices of results where an attack is classified, and construct a new test dataset of only attacks for stage two
            print("Running classifier two...")
            self.dataset_second_test = testing_set.loc[self.stage_one_result != 'normal']
            self.dataset_second_train = training_set.loc[training_set['labels'] != 'normal']

            try:
                classifier_two = self.load_module(self.txt_alg2.text())
                self.stage_two_result = classifier_two.run(self.dataset_second_train, self.dataset_second_test)
            except Exception as e:
                msg = ErrorMessage("Failed to run classifier two.", str(e))
                msg.show()
                return

            # Combine results from both stages into one, ensuring testing set labels match result order
            stage_one_test_normal = testing_set[self.stage_one_result == 'normal']
            total_test = testing_set[self.stage_one_result == 'normal'].append(testing_set[self.stage_one_result != 'normal'])
            total_res = np.append(self.stage_one_result[self.stage_one_result=='normal'], self.stage_two_result)

            y_test = total_test['labels']
            print(classification_report(y_test,total_res))
        else:
            # Get results from stage one
            y_test = testing_set['labels']
            print(classification_report(y_test, self.stage_one_result))

    def load_data(self):
        # Load column names
        self.dataset_cols = self.load_columns_from_file(self.labels_filename)
        # Load training set
        self.dataset_train = self.load_dataset_from_file(self.train_set_filename, self.dataset_cols)
        self.dataset_train_oh = self.one_hot_encoding(self.dataset_train)

        if not self.folds:
            # Load testing set
            # TODO: Sample training set to get testing set, if no testing set chosen
            self.dataset_test = self.load_dataset_from_file(self.test_set_filename, self.dataset_cols)
            self.dataset_test_oh = self.one_hot_encoding(self.dataset_test)

            # Add missing columns
            self.dataset_test_oh = self.clean_testing_set(self.dataset_train_oh, self.dataset_test_oh)

    def load_module(self, filename):
        spec = importlib.util.spec_from_file_location("module.name", filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    # loads dataset columns
    def load_columns_from_file(self, path):
        dataset_cols = []
        with open(path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                dataset_cols.append(row[0])
        return dataset_cols

    # loads a dataset and divides into 8 partitions.
    def load_dataset_from_file(self, path, fields):
        return pd.read_csv(path, index_col=False, names=fields)

    # Replaces Nominal Columns with several binary columns
    def one_hot_encoding(self, dataset):
        dataset_oh = dataset
        to_concat = []
        for column in dataset:
            if column in self.nominal_cols:
                df_oh = pd.get_dummies(dataset[column], prefix=column)
                to_concat.append(df_oh)
                dataset_oh = dataset_oh.drop(column, axis=1)
                for column_oh in df_oh:
                    self.binary_cols.append(column_oh)

        to_concat = pd.concat(to_concat, axis=1)
        dataset_oh = pd.concat([to_concat, dataset_oh], axis=1)

        return dataset_oh

    # Adds columns to the testing set which are missing based on its training set, removes errors relating to seperate OHE
    def clean_testing_set(self, train_set, test_set):
        new_test_set = test_set
        for column in list(train_set.columns.values):
            if column not in list(test_set.columns.values):
                idx = train_set.columns.get_loc(column)
                new_test_set.insert(idx, column, 0)
        return new_test_set

    def flatten_attacks(self, dataset):
        dataset_flat = dataset.copy() # Copy instead of reference
        mask = dataset_flat['labels'] != 'normal'
        column_name = 'labels'
        dataset_flat.loc[mask, column_name] = 'attack'
        return dataset_flat

