import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_MainWindow import Ui_MainWindow
from Ui_DatasetWindow import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btn_dataset_clicked(self):
        dataset_window = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(dataset_window)
        dataset_window.exec_()

    def btn_alg1_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File')

    def btn_alg2_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File')

    def chk_two_stage_toggled(self):
        print('Toggled!')

    def btn_run_clicked(self):
        print('Run!')
