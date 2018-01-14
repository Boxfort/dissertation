import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_DatasetWindow import Ui_Dialog

class DatasetWindow(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()

    def show(self):
        ui = Ui_Dialog()
        ui.setupUi(self)
        return self.exec_()

    def btn_train_set_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File')

    def btn_test_set_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File')

    def btn_labels_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File')
