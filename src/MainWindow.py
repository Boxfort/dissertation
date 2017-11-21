import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication

class MainWindow(QMainWindow):

    title = "COMNIA"

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle(self.title)
        self.createMenuBar()
        self.show()

    def createMenuBar(self):
        menubar = self.menuBar()
        self.statusBar()

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        testAction = QAction('&Test', self)
        testAction.setShortcut('Ctrl+T')
        testAction.setStatusTip('This is a test action')
        testAction.triggered.connect(self.onButtonPressed)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(testAction)

    def onTestButtonPressed(self):
        print("Test button pressed!")
