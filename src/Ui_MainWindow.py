# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtCreator/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(150, 0))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_dataset = QtWidgets.QTextEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_dataset.sizePolicy().hasHeightForWidth())
        self.txt_dataset.setSizePolicy(sizePolicy)
        self.txt_dataset.setReadOnly(True)
        self.txt_dataset.setObjectName("txt_dataset")
        self.verticalLayout.addWidget(self.txt_dataset)
        self.btn_dataset = QtWidgets.QPushButton(self.widget_2)
        self.btn_dataset.setObjectName("btn_dataset")
        self.verticalLayout.addWidget(self.btn_dataset)
        self.line = QtWidgets.QFrame(self.widget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.txt_alg1 = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_alg1.sizePolicy().hasHeightForWidth())
        self.txt_alg1.setSizePolicy(sizePolicy)
        self.txt_alg1.setObjectName("txt_alg1")
        self.verticalLayout.addWidget(self.txt_alg1)
        self.btn_alg1 = QtWidgets.QPushButton(self.widget_2)
        self.btn_alg1.setObjectName("btn_alg1")
        self.verticalLayout.addWidget(self.btn_alg1)
        self.line_5 = QtWidgets.QFrame(self.widget_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.chk_two_stage = QtWidgets.QCheckBox(self.widget_2)
        self.chk_two_stage.setObjectName("chk_two_stage")
        self.verticalLayout.addWidget(self.chk_two_stage)
        self.line_4 = QtWidgets.QFrame(self.widget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txt_alg2 = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_alg2.sizePolicy().hasHeightForWidth())
        self.txt_alg2.setSizePolicy(sizePolicy)
        self.txt_alg2.setObjectName("txt_alg2")
        self.verticalLayout.addWidget(self.txt_alg2)
        self.btn_alg2 = QtWidgets.QPushButton(self.widget_2)
        self.btn_alg2.setObjectName("btn_alg2")
        self.verticalLayout.addWidget(self.btn_alg2)
        self.line_3 = QtWidgets.QFrame(self.widget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.btn_run = QtWidgets.QPushButton(self.widget_2)
        self.btn_run.setObjectName("btn_run")
        self.verticalLayout.addWidget(self.btn_run)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAlgorithm = QtWidgets.QAction(MainWindow)
        self.actionAlgorithm.setObjectName("actionAlgorithm")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setShortcut("")
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setShortcut("")
        self.actionExit.setObjectName("actionExit")
        self.menuNew.addAction(self.actionAlgorithm)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.btn_alg1.clicked.connect(MainWindow.btn_alg1_clicked)
        self.chk_two_stage.toggled['bool'].connect(MainWindow.chk_two_stage_toggled)
        self.btn_alg2.clicked.connect(MainWindow.btn_alg2_clicked)
        self.btn_run.clicked.connect(MainWindow.btn_run_clicked)
        self.btn_dataset.clicked.connect(MainWindow.btn_dataset_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_dataset.setText(_translate("MainWindow", "Dataset..."))
        self.label_2.setText(_translate("MainWindow", "Classifier One"))
        self.btn_alg1.setText(_translate("MainWindow", "Select Classifier...."))
        self.chk_two_stage.setText(_translate("MainWindow", "Two Stage"))
        self.label.setText(_translate("MainWindow", "Classifier Two"))
        self.btn_alg2.setText(_translate("MainWindow", "Select Classifier..."))
        self.btn_run.setText(_translate("MainWindow", "Run"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Graphs"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.actionAlgorithm.setText(_translate("MainWindow", "Algorithm"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

