import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):

    title = "COMNIA"
    containerWidget = None

    def __init__(self):
        super().__init__()
        self.initUI()

    #TODO: Refactor widgets into their own classes for neatness
    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle(self.title)
        self.containerWidget = QWidget(self)

        self.setCentralWidget(self.containerWidget)
        self.createMenuBar()
        hbox = QHBoxLayout()
        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100,200])
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        hbox.addWidget(splitter2)
        self.containerWidget.setLayout(hbox)

        self.show()

    def createMenuBar(self):
        menubar = self.menuBar()
        self.statusBar()

        fileMenu = menubar.addMenu('&File')
        newMenu = QMenu('New', self)

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        testAction = QAction('&Algorithm', self)
        testAction.setShortcut('Ctrl+Alt+N')
        testAction.setStatusTip('Create new algorithm file')
        testAction.triggered.connect(self.onTestButtonPressed)

        fileMenu.addMenu(newMenu)
        fileMenu.addAction(exitAction)

        newMenu.addAction(testAction)

    def onTestButtonPressed(self):
        print("Test button pressed!")
