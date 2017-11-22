from PyQt5.QtWidgets import *

class Ui_Sidebar(object):

    def initUI(self):
        # Define layout
        layout = QGridLayout()
        layout.setColumnStretch(1, 0)
        layout.setColumnStretch(2, 0)

        # Define contents
        self.btnDataset = QPushButton('Dataset')
        self.btnOther = QPushButton('Other Button')

        # Add contents to layout
        layout.addWidget(self.btnDataset, 1, 0)
        layout.addWidget(self.btnOther, 2, 0)
        self.setLayout(layout)
