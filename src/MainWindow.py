import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

        # Set up triggers.
        self.exitAction.triggered.connect(qApp.quit)
        self.newAlgorithmAction.triggered.connect(self.onTestButtonPressed)
        self.settingsAction.triggered.connect(self.onTestButtonPressed)

    def onTestButtonPressed(self):
        print("Test button pressed!")
