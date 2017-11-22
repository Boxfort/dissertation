from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Sidebar import Sidebar

class Ui_MainWindow(object):

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("COMNIA")
        self.containerWidget = QWidget(self)
        self.setCentralWidget(self.containerWidget)
        self.createMenuBar()

        #Define Main Layout
        hbox = QHBoxLayout()
        topleft = Sidebar(self)
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

        self.fileMenu = menubar.addMenu('&File')
        self.newMenu = QMenu('New', self)

        self.exitAction = QAction('&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')

        self.newAlgorithmAction = QAction('&Algorithm', self)
        self.newAlgorithmAction.setShortcut('Ctrl+Alt+N')
        self.newAlgorithmAction.setStatusTip('Create new algorithm file')

        self.settingsAction = QAction('&Settings', self)
        self.settingsAction.setShortcut('Ctrl+Alt+S')
        self.settingsAction.setStatusTip('Edit Program Settings')

        self.fileMenu.addMenu(self.newMenu)
        self.fileMenu.addAction(self.settingsAction)
        self.fileMenu.addAction(self.exitAction)

        self.newMenu.addAction(self.newAlgorithmAction)

