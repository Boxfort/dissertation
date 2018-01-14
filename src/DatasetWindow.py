import sys
import csv
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

    def move_label(self):

        sender = self.sender().objectName()

        if sender == 'btn_numeric_to_nominal':
            items = self.lst_numeric.selectedItems()
            for item in items:
                self.lst_nominal.addItem(self.lst_numeric.takeItem(self.lst_numeric.row(item)))
        elif sender == 'btn_nominal_to_numeric':
            items = self.lst_nominal.selectedItems()
            for item in items:
                self.lst_numeric.addItem(self.lst_nominal.takeItem(self.lst_nominal.row(item)))
        elif sender == 'btn_nominal_to_binary':
            items = self.lst_nominal.selectedItems()
            for item in items:
                self.lst_binary.addItem(self.lst_nominal.takeItem(self.lst_nominal.row(item)))
        else:
            items = self.lst_binary.selectedItems()
            for item in items:
                self.lst_nominal.addItem(self.lst_binary.takeItem(self.lst_binary.row(item)))

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
            try:
                self.txt_labels.setText(filename[0])
                self.lst_numeric.clear()
                with open(filename[0], 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        self.lst_numeric.addItem(row[0])
            except Exception:
                print("Could not load file.")

        self.lst_nominal.addItem("Test")
        self.lst_binary.addItem("test")

