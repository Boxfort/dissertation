from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_Dataset import Ui_Dataset

class DatasetWindow(QDialog, Ui_Dataset):

    def __init__(self, parent):
        super(QDialog, self).__init__(parent)
        self.initUI()
        self.exec_()
