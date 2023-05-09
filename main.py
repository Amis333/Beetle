from graphics import Graphics
from PyQt5 import QtWidgets
from menu import StartWindow


def main():
    app = QtWidgets.QApplication([])

    start_window = StartWindow()
    start_window.setFixedSize(700, 500)
    start_window.show()

    app.exec()

    if start_window.algorithm_started:
        algorithm_graphics = Graphics()
        algorithm_graphics.algorithm_cycle()
    

if __name__ == '__main__':
    main()
