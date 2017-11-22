import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import sys
sys.path.append('../src/')
from Sidebar import Sidebar
from MainWindow import MainWindow

app = QApplication(sys.argv)
window = MainWindow()

class TestSidebar(unittest.TestCase):

    def test_createSidebar(self):
        self.sidebar = Sidebar(window)

    def test_btnDatabaseClicked(self):
        self.sidebar = Sidebar(window)
        QTest.mouseClick(self.sidebar.btnDataset, Qt.LeftButton)

if __name__ == '__main__':
    unittest.main()
