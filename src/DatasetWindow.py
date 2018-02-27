import sys
import os
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_DatasetWindow import Ui_Dialog
from ErrorMessage import ErrorMessage

# TODO: Let user select label field
class DatasetWindow(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.train_set_filename = ['','']
        self.test_set_filename = ['','']
        self.labels_filename = ['','']
        self.attacks_filename = ['','']

        self.txt_train_set.setText('')
        self.txt_test_set.setText('')
        self.txt_labels.setText('')
        self.txt_attacks.setText('')

        self.spn_folds.setValue(1)
        self.spn_runs.setValue(1)

        self.lst_numeric.clear()
        self.lst_nominal.clear()
        self.lst_binary.clear()


    def show(self, train_filename = '', test_filename = '', labels_filename = '', attacks_filename = '', numeric = [], nominal = [], binary = [], folds = 1):
        self.train_set_filename = [train_filename,'']
        self.test_set_filename = [test_filename,'']
        self.labels_filename = [labels_filename,'']
        self.attacks_filename = [attacks_filename,'']

        self.txt_train_set.setText(train_filename)
        self.txt_test_set.setText(test_filename)
        self.txt_labels.setText(labels_filename)
        self.txt_attacks.setText(attacks_filename)

        if folds:
            self.spn_folds.setValue(folds)

        if numeric:
            for item in numeric:
                self.lst_numeric.addItem(item)
        if nominal:
            for item in nominal:
                self.lst_nominal.addItem(item)
        if binary:
            for item in binary:
                self.lst_binary.addItem(item)

        return self.exec_()

    def chk_folds_toggled(self):
        self.spn_folds.setEnabled(not self.spn_folds.isEnabled())
        self.lbl_folds.setEnabled(not self.lbl_folds.isEnabled())
        self.txt_test_set.setEnabled(not self.txt_test_set.isEnabled())
        self.lbl_testing.setEnabled(not self.lbl_testing.isEnabled())
        self.btn_test_set.setEnabled(not self.btn_test_set.isEnabled())

    def on_accept(self):

        if not os.path.isfile(self.train_set_filename[0]):
            msg = ErrorMessage("Training set file does not exist!")
            msg.show()
            return

        if not self.chk_folds.isChecked() and not os.path.isfile(self.test_set_filename[0]):
            msg = ErrorMessage("Testing set file does not exist!")
            msg.show()
            return

        if not os.path.isfile(self.labels_filename[0]):
            msg = ErrorMessage("Field names file does not exist!")
            msg.show()
            return

        if not os.path.isfile(self.attacks_filename[0]) and not self.attacks_filename[0] == '':
            msg = ErrorMessage("Attacks filepath does not exist!")
            msg.show()
            return

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
    def rc_move_numeric(self):
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

    def btn_attacks_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File', os.getcwd(), 'Comma-seperated values (*.csv);;All Files (*.*)')

        self.attacks_filename = filename
        self.txt_attacks.setText(filename[0])


    def btn_labels_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select File', os.getcwd(), 'Comma-seperated values (*.csv);;All Files (*.*)')

        self.labels_filename = filename
        self.txt_labels.setText(filename[0])
        self.lst_numeric.clear()

        # If a file was selected
        if filename:
            load_cols(filename[0])

    def load_cols(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    # TODO: Remove hardcoded label column
                    if row[0] == 'labels':
                        continue
                    try:
                        if row[1] in ['binary', 'b']:
                            self.lst_binary.addItem(row[0])
                        elif row[1] in ['symbolic', 'nominal', 'categorical', 'cat', 's', 'c']:
                            self.lst_nominal.addItem(row[0])
                        else:
                            self.lst_numeric.addItem(row[0])
                    except Exception:
                        self.lst_numeric.addItem(row[0])

        except Exception:
            print("Could not load file.")

