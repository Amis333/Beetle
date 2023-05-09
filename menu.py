from PyQt5 import QtWidgets, QtGui
from beetle_menu import Ui_MainWindow
import final_menu
import sys


class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Start menu')
        self.setWindowIcon(QtGui.QIcon('images/beetle.png'))

        self.setStyleSheet("background-color: black;")

        self.ui.label.adjustSize()
        self.ui.label.setGeometry(100, 30, 500, 90)

        self.ui.pushButton.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(0, 255, 255);")
        self.ui.pushButton_2.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(0, 255, 255);")

        self.ui.pushButton.setFont(QtGui.QFont('BigOldBoldy-dEjR', 25))
        self.ui.pushButton.setGeometry(100, 170, 500, 90)
        self.ui.pushButton.clicked.connect(self.btnClicked)

        self.ui.pushButton_2.setFont(QtGui.QFont('BigOldBoldy-dEjR', 25))
        self.ui.pushButton_2.setGeometry(100, 300, 500, 90)
        self.ui.pushButton_2.clicked.connect(self.btnClicked2)
        self.menu_closed = False
        self.algorithm_started = False

    def btnClicked(self):
        self.close()
        self.algorithm_started = True

    def btnClicked2(self):
        self.menu_closed = True
        self.close()


class FinalWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(FinalWindow, self).__init__()
        self.ui = final_menu.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Finish menu')
        self.setWindowIcon(QtGui.QIcon('images/beetle.png'))

        self.setStyleSheet("background-color: black;")

        self.ui.label.adjustSize()
        self.ui.label.setGeometry(100, 30, 500, 90)

        self.ui.pushButton.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(0, 255, 255);")

        self.ui.pushButton.setFont(QtGui.QFont('BigOldBoldy-dEjR', 25))
        self.ui.pushButton.setGeometry(100, 155, 500, 90)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        sys.exit()


def open_final_menu():
    app = QtWidgets.QApplication([])

    start_window = FinalWindow()
    start_window.setFixedSize(700, 350)
    start_window.show()

    app.exec()

