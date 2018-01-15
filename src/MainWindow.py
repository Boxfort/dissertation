import sys
import os
import importlib.util
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from comniaUtils import *
from Ui_MainWindow import Ui_MainWindow
from DatasetWindow import DatasetWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btn_dataset_clicked(self):
        dataset_window = DatasetWindow()

        if dataset_window.show() == QDialog.Accepted:
            # Dataset accepted so grab data
            # TODO: Get column types set by user
            self.train_set_filename = dataset_window.train_set_filename[0]
            with open(self.train_set_filename, 'r') as file:
                row_count = sum(1 for row in file)
                self.txt_dataset.append("Training set rows: "+str(row_count))

            # Training is optional so check
            if not dataset_window.test_set_filename[0] == '':
                self.test_set_filename = dataset_window.test_set_filename[0]
                with open(self.test_set_filename, 'r') as file:
                    row_count = sum(1 for row in file)
                    self.txt_dataset.append("Training set rows: "+str(row_count))

            self.labels_filename = dataset_window.labels_filename[0]
            with open(self.labels_filename, 'r') as file:
                row_count = sum(1 for row in file)
                self.txt_dataset.append("Labels: "+str(row_count))



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
        print('Toggled!')

    def btn_run_clicked(self):
        # Determine whether 1 or 2 stage
        # Load algorithms
        # Load datasets
        # Optionally flatten 1st stage
        # Get results from stage 1
        # Pass results from stage 1 to stage 2
        # Get results from stage 2
        # Display
        self.load_data()

        if os.path.isfile(self.txt_alg1.text()):
            try:
                classifier = self.load_module(self.txt_alg1.text())
                classifier.run()
            except Exception as e:
                self.show_error("Failed to run classifier one.")
        else:
            self.show_error("Classifier one file does not exist!")

        print('Run!')

    def load_data(self):
        # Load column names
        load_cols(self.labels_filename)
        # Load training set
        self.dataset_train = load_dataset(self.train_set_filename, dataset_cols)
        self.dataset_train_oh = one_hot_encoding(self.dataset_train, nominal_cols)
        # Load testing set
        # TODO: Sample training set to get testing set, if no testing set chosen
        self.dataset_test = load_dataset(self.test_set_filename, dataset_cols)
        self.dataset_test_oh = one_hot_encoding(self.dataset_test, nominal_cols)
        self.dataset_test_oh = clean_testing_set(self.dataset_train_oh, self.dataset_test_oh)

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def load_module(self, filename):
        spec = importlib.util.spec_from_file_location("module.name", filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
