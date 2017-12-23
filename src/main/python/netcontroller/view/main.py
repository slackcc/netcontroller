import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 240
        self.initUI()

    def initUI(self):  #NOSONAR
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 80)
        self.textbox2.resize(280,40)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,160)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textbox_value = self.textbox.text()
        textbox_value_2 = self.textbox2.text()

        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textbox_value + " " + textbox_value_2,
                             QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        self.textbox2.setText("")
        self.textbox.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
