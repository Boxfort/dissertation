import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import sys
sys.path.append('../src/')
from MainWindow import MainWindow

app = QApplication(sys.argv)

class TestMainWindow(unittest.TestCase):

    def test_createMainWindow(self):
        self.window = MainWindow()

if __name__ == '__main__':
    unittest.main()
