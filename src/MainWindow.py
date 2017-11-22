import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_sidebar import ui_sidebar

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

        #Define Main Layout
        hbox = QHBoxLayout()
        topleft = ui_sidebar(self)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        textedit = QTextEdit()
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(textedit)
        splitter2.addWidget(bottom)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.setSizes([100,200])
        splitter1.addWidget(splitter2)
        hbox.addWidget(splitter1)

        self.containerWidget.setLayout(hbox)
        self.show()

    # Creates the menu bar at the top of the window and all contained actions
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

        settingsAction = QAction('&Settings', self)
        settingsAction.setShortcut('Ctrl+Alt+S')
        settingsAction.setStatusTip('Edit Program Settings')
        settingsAction.triggered.connect(self.onTestButtonPressed)

        fileMenu.addMenu(newMenu)
        fileMenu.addAction(exitAction)
        fileMenu.addAction(settingsAction)

        newMenu.addAction(testAction)

    def onTestButtonPressed(self):
        print("Test button pressed!")
