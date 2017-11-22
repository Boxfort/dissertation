from PyQt5.QtWidgets import *
from Ui_Sidebar import Ui_Sidebar

class Sidebar(QWidget, Ui_Sidebar):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.initUI()

        # Set up button triggers
        self.btnDataset.clicked.connect(self.onbtnDatasetClicked)
        self.btnOther.clicked.connect(self.onbtnOtherClicked)

    def onbtnDatasetClicked(self):
        print("Ya done clicked me ")

    def onbtnOtherClicked(self):
        print("Other clicked")

