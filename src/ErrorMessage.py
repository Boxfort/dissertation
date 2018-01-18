from PyQt5.QtWidgets import QMessageBox

class ErrorMessage(QMessageBox):

    def __init__(self, message, info = None):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setText(message)
        if info:
            self.setDetailedText(info)
        self.setWindowTitle("Error")
        self.setStandardButtons(QMessageBox.Ok)

    def show(self):
        return self.exec_()
