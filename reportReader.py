from readerController import Reader
from PyQt5 import QtCore, QtWidgets, QtGui
from reader import Ui_MainWindow
import sqlite3
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Reader()
    main.show()
    exit(app.exec())