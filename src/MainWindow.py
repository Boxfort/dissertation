import sys
import os
import math
import datetime
import time
import importlib.util
import csv
import numpy as np
import pandas as pd
from pandas_ml import ConfusionMatrix
from collections import defaultdict
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sklearn.metrics import classification_report
from Ui_MainWindow import Ui_MainWindow
from DatasetWindow import DatasetWindow
from ErrorMessage import ErrorMessage
from QBarChart import QBarChart
from QClfSelector import QClfSelector
from QCustomTab import QCustomTab

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.train_set_filename = ''
        self.test_set_filename = ''
        self.labels_filename = ''
        self.folds = None
        self.numeric_cols = []
        self.nominal_cols = []
        self.binary_cols = []

        sys.stdout = self
        self.app = app

        # Tab widget corner button
        self.tabButton = QToolButton(self)
        self.tabButton.setText('+')
        font = self.tabButton.font()
        font.setBold(True)
        self.tabButton.setFont(font)
        self.tab_classifiers.setCornerWidget(self.tabButton)
        self.tabButton.clicked.connect(self.add_page)
        self.tab_classifiers.removeTab(1)

        # Add the first clf tab
        self.test_clf = QClfSelector()
        self.verticalLayout_4.addWidget(self.test_clf)

    def add_page(self):
        tab = QWidget()
        clfWidget = QClfSelector()
        self.tab_classifiers.addTab(tab, str(self.tab_classifiers.count()+1))
        layout = QVBoxLayout(tab)
        layout.addWidget(clfWidget)

    def on_tab_close_requested(self, tab_ix):
        if tab_ix == 0:
            return

        self.tab_classifiers.removeTab(tab_ix)

    def write(self, txt):
        self.plainTextEdit.insertPlainText(txt)
        self.plainTextEdit.verticalScrollBar().setValue(self.plainTextEdit.verticalScrollBar().maximum())
        # Tell the GUI to refresh
        self.app.processEvents()

    def construct_graph(self, stats):
        self.graph = QBarChart(stats, self.tab_2)
        self.gridLayout.addWidget(self.graph, 0, 0, 1, 1)

    def btn_dataset_clicked(self):
        dataset_window = DatasetWindow()

        # Dataset accepted so grab data
        if dataset_window.show(self.train_set_filename, self.test_set_filename, self.labels_filename, self.numeric_cols, self.nominal_cols, self.binary_cols, self.folds) == QDialog.Accepted:

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
                self.txt_dataset.append("K-Fold Cross Validation with " + str(self.folds) + " folds.")

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


    def btn_run_clicked(self):
        # Load datasets
        print("Loading data...")
        try:
            self.load_data()
        except Exception as e:
            msg = ErrorMessage("Failed to load dataset.", str(e))
            msg.show()
            return

        for i in range(self.tab_classifiers.count()):
            if not os.path.isfile(self.tab_classifiers.widget(i).children()[1].txt_alg1.text()):
                msg = ErrorMessage("Tab "+i+": Classifier one file does not exist!")
                msg.show()
                return
            if self.tab_classifiers.widget(i).children()[1].chk_two_stage.isChecked() and not os.path.isfile(self.tab_classifiers.widget(i).children()[1].txt_alg2.text()):
                msg = ErrorMessage("Tab "+i+": Classifier two file does not exist!")
                msg.show()
                return

        results = []

        # Run each tab and gather results
        for i in range(self.tab_classifiers.count()):
            if self.folds:
                results.append(self.tab_classifiers.widget(i).children()[1].run_folds(self.dataset_train_oh, self.folds))
            else:
                results.append(self.tab_classifiers.widget(i).children()[1].run_testing_set(self.dataset_train_oh, self.dataset_test_oh))

        #print(classification_report(expected['labels'], results))
        #print(ConfusionMatrix(expected['labels'],results).stats()['overall']['Accuracy'])
        #print(ConfusionMatrix(expected['labels'],results).stats()['class'].keys())
        #cms = ConfusionMatrix(expected['labels'], results).stats()

        tograph = []

        # TODO: THIS IS TEMPORARY FOR TESTING
        for result in results:
            tograph.append(ConfusionMatrix(self.dataset_train_oh['labels'], result).stats()['class']['normal'])

        self.construct_graph(tograph)

        #self.write_results_to_file([classification_report(expected['labels'], results), ConfusionMatrix(expected['labels'], results)])

    def write_results_to_file(self, results):

        results_folder = os.getcwd() + '/results'

        if not os.path.exists(results_folder):
            os.makedirs(results_folder)

        path = results_folder + '/' + os.path.splitext(os.path.basename(self.txt_alg1.text()))[0] + '_'
        if self.chk_two_stage.isChecked():
            path += os.path.splitext(os.path.basename(self.txt_alg2.text()))[0] + '_'
        path += datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M:%S') + '.txt'

        with open(path, 'w+') as file:
            file.write("CLASSIFIER RESULTS\n\n")
            file.write("TRAINING SET = " + self.train_set_filename + '\n\n')
            if self.folds:
                file.write("K-Folds Cross Validation with " + str(self.folds) + ' folds\n\n')
            else:
                file.write("TESTING SET = " + self.test_set_filename + '\n\n')

            file.write("CLASSIFIER ONE = " + self.txt_alg1.text() + '\n\n')

            if self.chk_two_stage.isChecked():
                file.write("CLASSIFIER TWO = " + self.txt_alg1.text() + '\n\n')

            for result in results:
                file.write(str(result) + '\n\n')

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

    # Create a new algorithm file
    def on_actionAlgorithm(self):
        try:
            filename = QFileDialog.getSaveFileName(self, 'New Classifier', os.getcwd(), 'Python Scripts (*.py)')[0]
            if filename[len(filename)-3:len(filename)] != '.py':
                filename += '.py'

            f = open(filename,"w+")
            f.write("import numpy as np\n")
            f.write("import pandas as pd\n")
            f.write("\n")
            f.write("# Returns an array of classifier predicitons on test set.\n")
            f.write("def run(training_set, testing_set):\n")
            f.write("   raise NotImplementedError('Classifier run method not implemented.')\n")
            f.close()

        except Exception as e:
            msg = ErrorMessage("Could not create file.", str(e))
            msg.show()

        print(filename)

    def on_actionQuit(self):
        QCoreApplication.instance().quit()

