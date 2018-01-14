import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_MainWindow import Ui_MainWindow
from DatasetWindow import DatasetWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btn_dataset_clicked(self):
        dataset_window = DatasetWindow()

        if dataset_window.show() == QDialog.Accepted:
            print("Accepted")
        else:
            print("Cancelled")

    def btn_alg1_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File')
        print(filename)

    def btn_alg2_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File')
        print(filename)

    def chk_two_stage_toggled(self):
        self.label.setEnabled(not self.label.isEnabled())
        self.txt_alg2.setEnabled(not self.txt_alg2.isEnabled())
        self.btn_alg2.setEnabled(not self.btn_alg2.isEnabled())
        print('Toggled!')

    def btn_run_clicked(self):
        print('Run!')
