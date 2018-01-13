import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btn_dataset_clicked(self):
        print("Clicked me!")
