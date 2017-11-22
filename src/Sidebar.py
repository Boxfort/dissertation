from PyQt5.QtWidgets import *
from Ui_Sidebar import Ui_Sidebar

class Sidebar(QWidget, Ui_Sidebar):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        # Set up button triggers
        self.btnDataset.clicked.connect(onbtnDatasetClicked)
        self.btnOther.clicked.connect(onbtnOtherClicked)

    def onbtnDatasetClicked(self):
        print("Ya done clicked me ")

    def onbtnOtherClicked(self):
        print("Other clicked")

