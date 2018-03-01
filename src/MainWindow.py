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
from pandas_ml.confusion_matrix.bcm import BinaryConfusionMatrix
from collections import defaultdict, OrderedDict
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sklearn.metrics import classification_report
from Ui_MainWindow import Ui_MainWindow
from DatasetWindow import DatasetWindow
from ErrorMessage import ErrorMessage
from QBarChart import QBarChart
from QClfSelector import QClfSelector

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.train_set_filename = ''
        self.test_set_filename = ''
        self.labels_filename = ''
        self.attacks_filename = ''
        self.folds = None
        self.runs = 0
        self.graph = None
        self.results = []
        self.numeric_cols = []
        self.nominal_cols = []
        self.binary_cols = []
        self.attacks = defaultdict(list)

        #sys.stdout = self
        self.app = app

        self.splitter_2.setSizes([200, 600])
        self.splitter.setSizes([700, 100])

        # Tab widget corner button
        self.tabButton = QToolButton(self)
        self.tabButton.setText('+')
        font = self.tabButton.font()
        font.setBold(True)
        self.tabButton.setFont(font)
        self.tab_classifiers.setCornerWidget(self.tabButton)
        self.tabButton.clicked.connect(self.add_page)
        self.tab_classifiers.removeTab(1)
        self.tabWidget.removeTab(0)

        # Add the first clf tab
        self.test_clf = QClfSelector()
        self.verticalLayout_4.addWidget(self.test_clf)

    def add_page(self):
        tab = QWidget()
        clfWidget = QClfSelector()
        self.tab_classifiers.addTab(tab, str(self.tab_classifiers.count()+1))
        layout = QVBoxLayout(tab)
        layout.addWidget(clfWidget)

    def add_result_tab(self, tabname, content):
        tab = QWidget()
        txtbox = QPlainTextEdit()
        self.tabWidget.addTab(tab, str(tabname))
        layout = QVBoxLayout(tab)
        layout.addWidget(txtbox)
        txtbox.setPlainText(content)
        txtbox.setReadOnly(True)
        f = QFont("unexistent")
        f.setStyleHint(QFont.Monospace)
        txtbox.setFont(f);

    def on_tab_close_requested(self, tab_ix):
        if tab_ix == 0:
            return

        self.tab_classifiers.removeTab(tab_ix)

    def write(self, txt):
        self.plainTextEdit.insertPlainText(txt)
        self.plainTextEdit.verticalScrollBar().setValue(self.plainTextEdit.verticalScrollBar().maximum())
        # Tell the GUI to refresh
        self.app.processEvents()

    def flush(self):
        pass

    def construct_graph(self, stats, stochastic):
        self.graph = QBarChart(stats, self.runs, stochastic, self.tab_2)
        self.gridLayout.addWidget(self.graph, 0, 0, 1, 1)

    def btn_show_graph_clicked(self):
        tograph = []
        the_class = str(self.cmb_graph_class.currentText())
        stochastic = []

        for result in self.results:

            cm = None
            stochastic.append(result[1])

            if result[1]:
                multi_dataset = self.dataset_train_oh.copy()
                for i in range(self.runs - 1):
                    multi_dataset = multi_dataset.append(self.dataset_train_oh)

                cm = ConfusionMatrix(multi_dataset['labels'], result[0])

            else:
                cm = ConfusionMatrix(self.dataset_train_oh['labels'], result[0])

            tograph.append(cm.stats()['class'][the_class])

        self.construct_graph(tograph, stochastic)

    def btn_dataset_clicked(self):
        dataset_window = DatasetWindow()

        # Dataset accepted so grab data
        if dataset_window.show(self.train_set_filename, self.test_set_filename, self.labels_filename, self.attacks_filename, self.numeric_cols, self.nominal_cols, self.binary_cols, self.folds) == QDialog.Accepted:

            self.txt_dataset.clear()
            self.test_set_filename = ''
            self.folds = None

            # Grab training set
            self.train_set_filename = dataset_window.train_set_filename[0]
            with open(self.train_set_filename, 'r') as file:
                row_count = sum(1 for row in file)
                self.txt_dataset.append("Training set rows: "+str(row_count))

            if not dataset_window.test_set_filename[0] == '':
                # Grab test set
                self.test_set_filename = dataset_window.test_set_filename[0]
                with open(self.test_set_filename, 'r') as file:
                    row_count = sum(1 for row in file)
                    self.txt_dataset.append("Training set rows: "+str(row_count))

            # attacks
            if not dataset_window.attacks_filename[0] == '':
                self.attacks_filename = dataset_window.attacks_filename[0]
                

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

            # Grab runs
            self.runs = dataset_window.spn_runs.value()

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
            return msg

        for i in range(self.tab_classifiers.count()):
            if not os.path.isfile(self.tab_classifiers.widget(i).children()[1].txt_alg1.text()):
                msg = ErrorMessage("Tab "+str(i)+": Classifier one file does not exist!")
                msg.show()
                return msg
            if self.tab_classifiers.widget(i).children()[1].chk_two_stage.isChecked() and not os.path.isfile(self.tab_classifiers.widget(i).children()[1].txt_alg2.text()):
                msg = ErrorMessage("Tab "+str(i)+": Classifier two file does not exist!")
                msg.show()
                return msg

        results = []

        # Run each tab and gather results
        for i in range(self.tab_classifiers.count()):

            self.tab_classifiers.widget(i).children()[1].load_modules()

            # If the classfiers are stochastic run them multiple times
            if self.tab_classifiers.widget(i).children()[1].classifier_one.stochastic or (self.tab_classifiers.widget(i).children()[1].chk_two_stage.isChecked() and self.tab_classifiers.widget(i).children()[1].classifier_two.stochastic):

                sub_result = []

                for j in range(self.runs):
                    if self.folds:
                        sub_result = sub_result + list(self.tab_classifiers.widget(i).children()[1].run_folds(self.dataset_train_oh, self.folds))
                    else:
                        sub_result = sub_result + list(self.tab_classifiers.widget(i).children()[1].run_testing_set(self.dataset_train_oh, self.dataset_test_oh))

                results.append([sub_result, True])

            else:

                if self.folds:
                    results.append([self.tab_classifiers.widget(i).children()[1].run_folds(self.dataset_train_oh, self.folds), False])
                else:
                    results.append([self.tab_classifiers.widget(i).children()[1].run_testing_set(self.dataset_train_oh, self.dataset_test_oh), False])

            self.write_results_to_file(results[i], self.tab_classifiers.widget(i).children()[1])

        if self.tabWidget.count() > 1:
            for i in range(1, self.tabWidget.count()):
                self.tabWidget.removeTab(1)

        count = 1
        for result in results:
            expected = None
            text = ''
            if result[1]:
                expected = self.dataset_train_oh.copy()['labels']
                for i in range(self.runs - 1):
                    expected = expected.append(self.dataset_train_oh['labels'])
            else:
                expected = self.dataset_train_oh['labels']

            cm = ConfusionMatrix(expected, result[0])

            with pd.option_context('display.max_rows', None, 'display.max_columns', 100):
                text += str(classification_report(expected, result[0])) + '\n\n'
                text += str(self.get_attacks_stats(cm)) + '\n\n'
                text += str(cm.stats())

            self.add_result_tab(count, text)
            count += 1

        self.results = results
        self.populate_graph_combo()


    def populate_graph_combo(self):
        self.cmb_graph_class.setEnabled(True)
        self.btn_show_graph.setEnabled(True)
        self.cmb_graph_class.addItems(self.dataset_train_oh['labels'].unique())


    def write_results_to_file(self, result, clfinfo):

        results_folder = os.getcwd() + '/results'

        if not os.path.exists(results_folder):
            os.makedirs(results_folder)

        path = results_folder + '/' + os.path.splitext(os.path.basename(clfinfo.txt_alg1.text()))[0] + '_'
        if clfinfo.chk_two_stage.isChecked():
            path += os.path.splitext(os.path.basename(clfinfo.txt_alg2.text()))[0] + '_'
        path += datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M:%S') + '.txt'

        with open(path, 'w+') as file:
            file.write("CLASSIFIER RESULTS\n\n")
            file.write("TRAINING SET = " + self.train_set_filename + '\n\n')
            if self.folds:
                file.write("K-Folds Cross Validation with " + str(self.folds) + ' folds\n\n')
            else:
                file.write("TESTING SET = " + self.test_set_filename + '\n\n')

            file.write("CLASSIFIER ONE = " + clfinfo.txt_alg1.text() + '\n\n')

            if clfinfo.chk_two_stage.isChecked():
                file.write("CLASSIFIER TWO = " + clfinfo.txt_alg2.text() + '\n\n')

            expected = None

            if result[1]:
                expected = self.dataset_train_oh.copy()['labels']
                for i in range(self.runs - 1):
                    expected = expected.append(self.dataset_train_oh['labels'])
            else:
                expected = self.dataset_train_oh['labels']

            cm = ConfusionMatrix(expected, result[0])

            with pd.option_context('display.max_rows', None, 'display.max_columns', 100):
                file.write(str(classification_report(expected, result[0])) + '\n\n')
                if self.attacks_filename != '':
                    file.write(str(self.get_attacks_stats(cm)) + '\n\n')
                file.write(str(cm) + '\n\n')
                file.write(str(cm.stats()))

    def get_attacks_stats(self, cm):

        columns = ['precision', 'recall', 'f1-score', 'fp-rate', 'TP','TN','FP','FN', 'support']
        class_df = pd.DataFrame(columns=columns)

        cms = cm.stats()['class']

        for k in self.attacks.keys():
            df = cms[self.attacks[k]]
            fp = df[df.index.str.startswith('FP: False Positive')].iloc[0].tolist()
            tn = df[df.index.str.startswith('TN: True Negative')].iloc[0].tolist()
            fn = df[df.index.str.startswith('FN: False Negative')].iloc[0].tolist()
            tp = df[df.index.str.startswith('TP: True Positive')].iloc[0].tolist()

            p = list()
            r = list()
            f1 = list()
            fpr = list()
            s = list()

            for i in range(len(fp)):
                # Precision (TP / (TP + FP))
                p.append(tp[i] / (tp[i] + fp[i]))
                # Recall ( TP / (TP + FN))
                r.append(tp[i]/ (tp[i] + fn[i]))
                # f1-score ( 2 * ((P * R) / (P + R)))
                f1.append(2 * ((p[i] * r[i]) / (p[i] + r[i])))
                # fp-rate ( FP / (TN + FP))
                fpr.append((fp[i] / (tn[i] + fp[i])) * 100)
                # support (TP+FN)
                s.append(tp[i] + fn[i])

            p = np.nan_to_num(p)
            r = np.nan_to_num(r)
            f1 = np.nan_to_num(f1)
            fpr = np.nan_to_num(fpr)

            pavg = sum(p) / len(p)
            ravg = sum(r) / len(r)
            f1avg = sum(f1) / len(f1)
            fpravg = sum(fpr) / len(fpr)

            class_df.loc[k] = [round(pavg,2),round(ravg,2),round(f1avg,2),round(fpravg,4),sum(tp),sum(tn),sum(fp),sum(fn), sum(s)]

        return class_df


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

        if not self.attacks_filename == '':
            labellist = self.dataset_train_oh['labels'].unique()
            # Fix attack list
            with open(self.attacks_filename, 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[0] in labellist:
                            self.attacks[row[1]].append(row[0])

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

    def on_actionQuit(self):
        QCoreApplication.instance().quit()

