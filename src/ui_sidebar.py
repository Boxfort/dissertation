from PyQt5.QtWidgets import *

class ui_sidebar(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.createGridLayout()

    def createGridLayout(self):
        layout = QGridLayout()
        layout.setColumnStretch(1, 0)
        layout.setColumnStretch(2, 0)

        btnDataset = QPushButton('Dataset')
        btnDataset.clicked.connect(self.onbtnDatasetClicked)

        layout.addWidget(btnDataset)
        layout.addWidget(QPushButton('Other Button'),1,0)

        self.setLayout(layout)

    def onbtnDatasetClicked(self):
        print("Ya done clicked me ")
