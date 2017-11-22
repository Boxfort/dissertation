from PyQt5.QtWidgets import *

class Ui_Sidebar(object):

    def __init__(self, parent):
        # Define layout
        layout = QGridLayout()
        layout.setColumnStretch(1, 0)
        layout.setColumnStretch(2, 0)

        # Define contents
        self.btnDataset = QPushButton('Dataset')
        self.btnOther = QPushButton('Other Button')
        # Add contents to layout
        layout.addWidget(self.btnDataset)
        layout.addWidget(self.btnOther)
        self.setLayout(layout)

        # Retranslate UI to parent
        self.retranslateUi(parent)
