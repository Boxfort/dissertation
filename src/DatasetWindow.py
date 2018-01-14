import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_DatasetWindow import Ui_Dialog

class DatasetWindow(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()

    def show(self):
        self.setupUi(self)
        return self.exec_()

    def show_right_click_context(self, pos):
        self.popMenu = QMenu(self)
        self.popMenu.addAction(QAction('test0', self))
        self.popMenu.addAction(QAction('test1', self))
        self.popMenu.addSeparator()
        self.popMenu.addAction(QAction('test2', self))
        self.popMenu.exec_(self.sender().mapToGlobal(pos))


    def btn_train_set_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File')
        self.txt_train_set.setText(filename[0])

    def btn_test_set_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File')
        self.txt_test_set.setText(filename[0])

    def btn_labels_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File')

        # If a file was selected
        if filename:
            self.txt_labels.setText(filename[0])
            self.lst_numeric.clear()
            self.lst_numeric.addItem("Test1")
            self.lst_numeric.addItem("Test2")
            self.lst_numeric.addItem("Test3")
            self.lst_numeric.addItem("Test4")
