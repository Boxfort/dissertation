from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_Dataset(object):

    def initUI(self):
        self.setWindowTitle("Dataset")
        self.setGeometry(300,250,300,300)
        self.setWindowModality(Qt.ApplicationModal)
        self.setSizeGripEnabled(True)

        label = QLabel('My Label') 
        line_edit = QLineEdit()
        form_layout = QFormLayout() 
        form_layout.addRow(label, line_edit) 
        close_button = QPushButton('Close')
        execute_button = QPushButton('Execute')

        button_layout = QHBoxLayout()
        button_layout.addWidget(close_button)
        button_layout.addWidget(execute_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
