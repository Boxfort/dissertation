import sys
import os
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_DatasetWindow import Ui_Dialog

class DatasetWindow(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.train_set_filename = ['','']
        self.test_set_filename = ['','']
        self.labels_filename = ['','']

    def show(self):
        self.setupUi(self)
        return self.exec_()

    def on_accept(self):

        if not os.path.isfile(self.train_set_filename[0]) and not os.path.isfile(self.labels_filename[0]):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("File does not exist.")
            msg.setInformativeText("")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.accept()

    def show_right_click_context(self, pos):
        self.popMenu = QMenu(self)
        self.lastList = self.sender()

        move_numeric = QAction('Move to numerical', self)
        move_nominal = QAction('Move to nominal', self)
        move_binary = QAction('Move to binary', self)
        move_numeric.triggered.connect(self.rc_move_numeric)
        move_nominal.triggered.connect(self.rc_move_nominal)
        move_binary.triggered.connect(self.rc_move_binary)

        self.popMenu.addAction(move_numeric)
        self.popMenu.addAction(move_nominal)
        self.popMenu.addAction(move_binary)
        self.popMenu.addSeparator()
        self.popMenu.addAction(QAction('Cancel', self))
        self.popMenu.exec_(self.sender().mapToGlobal(pos))

    # TODO: Theres definetly a better way of moving between lists
    #     : Could probably condense rc_move and move_label methods into one method

    def rc_move_numeric(self, extra):
        items = self.lastList.selectedItems()
        for item in items:
            self.lst_numeric.addItem(self.lastList.takeItem(self.lastList.row(item)))

    def rc_move_nominal(self):
        items = self.lastList.selectedItems()
        for item in items:
            self.lst_nominal.addItem(self.lastList.takeItem(self.lastList.row(item)))

    def rc_move_binary(self):
        items = self.lastList.selectedItems()
        for item in items:
            self.lst_binary.addItem(self.lastList.takeItem(self.lastList.row(item)))

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
        filename = QFileDialog.getOpenFileName(self, 'Select File', os.getcwd(), 'Comma-seperated values (*.csv);;All Files (*.*)')

        self.train_set_filename = filename
        self.txt_train_set.setText(filename[0])


    def btn_test_set_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File', os.getcwd(), 'Comma-seperated values (*.csv);;All Files (*.*)')

        self.test_set_filename = filename
        self.txt_test_set.setText(filename[0])

    def btn_labels_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File', os.getcwd(), 'Comma-seperated values (*.csv);;All Files (*.*)')

        self.labels_filename = filename
        self.txt_labels.setText(filename[0])
        self.lst_numeric.clear()

        # If a file was selected
        if filename:
            try:
                with open(filename[0], 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        self.lst_numeric.addItem(row[0])
            except Exception:
                print("Could not load file.")

