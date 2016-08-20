import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget)
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Button', self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Hello World Application')
        self.resize(250, 150)
        self.center()

        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.button_alert)
        self.show()

    def button_alert(self):
        QMessageBox.information(self.parentWidget(),
                                'Message', "Hello World!",
                                QMessageBox.Ok)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
