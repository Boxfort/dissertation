# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtCreator/clf_selector.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_clfSelector(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 299)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.txt_alg1 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_alg1.sizePolicy().hasHeightForWidth())
        self.txt_alg1.setSizePolicy(sizePolicy)
        self.txt_alg1.setObjectName("txt_alg1")
        self.verticalLayout.addWidget(self.txt_alg1)
        self.btn_alg1 = QtWidgets.QPushButton(Form)
        self.btn_alg1.setObjectName("btn_alg1")
        self.verticalLayout.addWidget(self.btn_alg1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.chk_two_stage = QtWidgets.QCheckBox(Form)
        self.chk_two_stage.setObjectName("chk_two_stage")
        self.verticalLayout.addWidget(self.chk_two_stage)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txt_alg2 = QtWidgets.QLineEdit(Form)
        self.txt_alg2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_alg2.sizePolicy().hasHeightForWidth())
        self.txt_alg2.setSizePolicy(sizePolicy)
        self.txt_alg2.setObjectName("txt_alg2")
        self.verticalLayout.addWidget(self.txt_alg2)
        self.btn_alg2 = QtWidgets.QPushButton(Form)
        self.btn_alg2.setEnabled(False)
        self.btn_alg2.setObjectName("btn_alg2")
        self.verticalLayout.addWidget(self.btn_alg2)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        spacerItem = QtWidgets.QSpacerItem(20, 57, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        self.btn_alg1.clicked.connect(Form.btn_alg1_clicked)
        self.chk_two_stage.toggled['bool'].connect(Form.chk_two_stage_toggled)
        self.btn_alg2.clicked.connect(Form.btn_alg2_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Classifier One"))
        self.btn_alg1.setText(_translate("Form", "Select Classifier...."))
        self.chk_two_stage.setText(_translate("Form", "Two Stage"))
        self.label.setText(_translate("Form", "Classifier Two"))
        self.btn_alg2.setText(_translate("Form", "Select Classifier..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

