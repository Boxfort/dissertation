# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtCreator/datasetWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1126, 579)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setMinimumSize(QtCore.QSize(300, 0))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.txt_train_set = QtWidgets.QLineEdit(self.widget)
        self.txt_train_set.setReadOnly(True)
        self.txt_train_set.setClearButtonEnabled(False)
        self.txt_train_set.setObjectName("txt_train_set")
        self.verticalLayout_2.addWidget(self.txt_train_set)
        self.btn_train_set = QtWidgets.QPushButton(self.widget)
        self.btn_train_set.setObjectName("btn_train_set")
        self.verticalLayout_2.addWidget(self.btn_train_set)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.chk_folds = QtWidgets.QCheckBox(self.widget)
        self.chk_folds.setChecked(True)
        self.chk_folds.setObjectName("chk_folds")
        self.verticalLayout_2.addWidget(self.chk_folds)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.lbl_folds = QtWidgets.QLabel(self.widget)
        self.lbl_folds.setObjectName("lbl_folds")
        self.verticalLayout_2.addWidget(self.lbl_folds)
        self.spn_folds = QtWidgets.QSpinBox(self.widget)
        self.spn_folds.setMinimum(1)
        self.spn_folds.setMaximum(1000)
        self.spn_folds.setObjectName("spn_folds")
        self.verticalLayout_2.addWidget(self.spn_folds)
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.lbl_testing = QtWidgets.QLabel(self.widget)
        self.lbl_testing.setEnabled(False)
        self.lbl_testing.setObjectName("lbl_testing")
        self.verticalLayout_2.addWidget(self.lbl_testing)
        self.txt_test_set = QtWidgets.QLineEdit(self.widget)
        self.txt_test_set.setEnabled(False)
        self.txt_test_set.setReadOnly(True)
        self.txt_test_set.setObjectName("txt_test_set")
        self.verticalLayout_2.addWidget(self.txt_test_set)
        self.btn_test_set = QtWidgets.QPushButton(self.widget)
        self.btn_test_set.setEnabled(False)
        self.btn_test_set.setObjectName("btn_test_set")
        self.verticalLayout_2.addWidget(self.btn_test_set)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.txt_labels = QtWidgets.QLineEdit(self.widget)
        self.txt_labels.setReadOnly(True)
        self.txt_labels.setObjectName("txt_labels")
        self.verticalLayout_2.addWidget(self.txt_labels)
        self.btn_labels = QtWidgets.QPushButton(self.widget)
        self.btn_labels.setObjectName("btn_labels")
        self.verticalLayout_2.addWidget(self.btn_labels)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.lst_numeric = QtWidgets.QListWidget(self.widget_3)
        self.lst_numeric.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lst_numeric.setAcceptDrops(True)
        self.lst_numeric.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lst_numeric.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lst_numeric.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lst_numeric.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lst_numeric.setDragEnabled(True)
        self.lst_numeric.setDragDropOverwriteMode(True)
        self.lst_numeric.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.lst_numeric.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lst_numeric.setAlternatingRowColors(True)
        self.lst_numeric.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lst_numeric.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.lst_numeric.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.lst_numeric.setMovement(QtWidgets.QListView.Free)
        self.lst_numeric.setProperty("isWrapping", False)
        self.lst_numeric.setWordWrap(True)
        self.lst_numeric.setObjectName("lst_numeric")
        self.verticalLayout_3.addWidget(self.lst_numeric)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.btn_numeric_to_nominal = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_numeric_to_nominal.sizePolicy().hasHeightForWidth())
        self.btn_numeric_to_nominal.setSizePolicy(sizePolicy)
        self.btn_numeric_to_nominal.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_numeric_to_nominal.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_numeric_to_nominal.setFlat(False)
        self.btn_numeric_to_nominal.setObjectName("btn_numeric_to_nominal")
        self.verticalLayout_6.addWidget(self.btn_numeric_to_nominal)
        self.btn_nominal_to_numeric = QtWidgets.QPushButton(self.widget_6)
        self.btn_nominal_to_numeric.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_nominal_to_numeric.setObjectName("btn_nominal_to_numeric")
        self.verticalLayout_6.addWidget(self.btn_nominal_to_numeric)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.widget_6)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_nominal = QtWidgets.QLabel(self.widget_4)
        self.lbl_nominal.setObjectName("lbl_nominal")
        self.verticalLayout_4.addWidget(self.lbl_nominal)
        self.lst_nominal = QtWidgets.QListWidget(self.widget_4)
        self.lst_nominal.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lst_nominal.setAcceptDrops(True)
        self.lst_nominal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lst_nominal.setDragEnabled(True)
        self.lst_nominal.setDragDropOverwriteMode(True)
        self.lst_nominal.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.lst_nominal.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lst_nominal.setAlternatingRowColors(True)
        self.lst_nominal.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lst_nominal.setMovement(QtWidgets.QListView.Free)
        self.lst_nominal.setProperty("isWrapping", False)
        self.lst_nominal.setWordWrap(True)
        self.lst_nominal.setObjectName("lst_nominal")
        self.verticalLayout_4.addWidget(self.lst_nominal)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.widget_7 = QtWidgets.QWidget(self.widget_2)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.btn_nominal_to_binary = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_nominal_to_binary.sizePolicy().hasHeightForWidth())
        self.btn_nominal_to_binary.setSizePolicy(sizePolicy)
        self.btn_nominal_to_binary.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_nominal_to_binary.setObjectName("btn_nominal_to_binary")
        self.verticalLayout_7.addWidget(self.btn_nominal_to_binary)
        self.btn_binary_to_nominal = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_binary_to_nominal.sizePolicy().hasHeightForWidth())
        self.btn_binary_to_nominal.setSizePolicy(sizePolicy)
        self.btn_binary_to_nominal.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_binary_to_nominal.setObjectName("btn_binary_to_nominal")
        self.verticalLayout_7.addWidget(self.btn_binary_to_nominal)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_2.addWidget(self.widget_7)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_binary = QtWidgets.QLabel(self.widget_5)
        self.lbl_binary.setObjectName("lbl_binary")
        self.verticalLayout_5.addWidget(self.lbl_binary)
        self.lst_binary = QtWidgets.QListWidget(self.widget_5)
        self.lst_binary.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lst_binary.setAcceptDrops(True)
        self.lst_binary.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lst_binary.setDragEnabled(True)
        self.lst_binary.setDragDropOverwriteMode(True)
        self.lst_binary.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.lst_binary.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lst_binary.setAlternatingRowColors(True)
        self.lst_binary.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lst_binary.setMovement(QtWidgets.QListView.Free)
        self.lst_binary.setProperty("isWrapping", False)
        self.lst_binary.setWordWrap(True)
        self.lst_binary.setObjectName("lst_binary")
        self.verticalLayout_5.addWidget(self.lst_binary)
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.btn_train_set.clicked.connect(Dialog.btn_train_set_clicked)
        self.btn_test_set.clicked.connect(Dialog.btn_test_set_clicked)
        self.btn_labels.clicked.connect(Dialog.btn_labels_clicked)
        self.lst_numeric.customContextMenuRequested['QPoint'].connect(Dialog.show_right_click_context)
        self.lst_nominal.customContextMenuRequested['QPoint'].connect(Dialog.show_right_click_context)
        self.lst_binary.customContextMenuRequested['QPoint'].connect(Dialog.show_right_click_context)
        self.btn_numeric_to_nominal.clicked.connect(Dialog.move_label)
        self.btn_nominal_to_numeric.clicked.connect(Dialog.move_label)
        self.btn_nominal_to_binary.clicked.connect(Dialog.move_label)
        self.btn_binary_to_nominal.clicked.connect(Dialog.move_label)
        self.buttonBox.accepted.connect(Dialog.on_accept)
        self.chk_folds.toggled['bool'].connect(Dialog.chk_folds_toggled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Dataset"))
        self.label.setText(_translate("Dialog", "Training Set"))
        self.btn_train_set.setText(_translate("Dialog", "Select Training Set..."))
        self.chk_folds.setText(_translate("Dialog", "K-Fold Cross-Validation"))
        self.lbl_folds.setText(_translate("Dialog", "K-Folds"))
        self.lbl_testing.setText(_translate("Dialog", "Testing Set"))
        self.btn_test_set.setText(_translate("Dialog", "Select Testing Set..."))
        self.label_3.setText(_translate("Dialog", "Column Labels"))
        self.btn_labels.setText(_translate("Dialog", "Select Column Labels..."))
        self.label_4.setText(_translate("Dialog", "Numerical Columns"))
        self.lst_numeric.setSortingEnabled(True)
        self.btn_numeric_to_nominal.setText(_translate("Dialog", ">"))
        self.btn_nominal_to_numeric.setText(_translate("Dialog", "<"))
        self.lbl_nominal.setText(_translate("Dialog", "Nominal Columns"))
        self.lst_nominal.setSortingEnabled(True)
        self.btn_nominal_to_binary.setText(_translate("Dialog", ">"))
        self.btn_binary_to_nominal.setText(_translate("Dialog", "<"))
        self.lbl_binary.setText(_translate("Dialog", "Binary Columns"))
        self.lst_binary.setSortingEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

