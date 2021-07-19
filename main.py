import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide2.QtCore import QFile
from PySide2.QtGui import QFocusEvent
from ui import Ui_App
from siteParser import Parser

from console import console


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_App()
        self.ui.setupUi(self)
        self.ui.randomPageBtn.setDefault(True)
        self.ui.randomPageBtn.setFocus()

    def lineEditFocusIn(self, e):
        self.ui.lineEdit.setText("")
        self.ui.lineEdit.setStyleSheet(
            "QLineEdit {border: 2px solid #30D5C8; padding: 0 8px}"
        )
        QLineEdit.focusInEvent(self.ui.lineEdit, e)


if __name__ == "__main__":
    # Create application
    app = QApplication(sys.argv)

    # Create window
    window = MainWindow()
    parser = Parser()

    window.ui.quitBtn.clicked.connect(lambda: app.exit())

    window.ui.getBtn.clicked.connect(
        lambda: parser.looping(window.ui.lineEdit.text())
    )

    window.ui.randomPageBtn.clicked.connect(
        lambda: parser.looping(parser.getRandomPage())
    )

    window.ui.lineEdit.focusInEvent = window.lineEditFocusIn

    window.show()

    # Run main loop
    sys.exit(app.exec_())
