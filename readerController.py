from PyQt5 import QtCore, QtWidgets, QtGui
from reader import Ui_MainWindow
import sqlite3
import sys


class Reader(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Reader, self).__init__()
        self.setupUi(self)
        self.readAllButton.clicked.connect(self.readAll)
        self.readDistinctButton.clicked.connect(self.readDistinct)

        self.conn = sqlite3.connect('reports.sqlite3')
        self.c = self.conn.cursor()
        print("成功連接資料庫")

    def readAll(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        headerName = ["id", "對手暱稱", "對手等級", "我方等級", "戰鬥種類", "戰鬥結果", "是否留言", "戰報時間"]
        self.tableWidget.setHorizontalHeaderLabels(headerName)

        reports = self.c.execute(
            ''' SELECT * FROM reports '''
        ).fetchall()

        for report in reports:
            report = list(report)
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(report[0])))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(report[1])))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(report[3])))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(report[4])))
            self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(report[5])))
            self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(report[6])))
            self.tableWidget.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(str(report[8])))
            self.tableWidget.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(str(report[9])))

    def readDistinct(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        headerName = ["對手暱稱", "戰鬥次數"]
        self.tableWidget.setHorizontalHeaderLabels(headerName)

        reports = self.c.execute(
            ''' SELECT DISTINCT playerName FROM reports '''
        ).fetchall()

        for report in reports:
            report = list(report)
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(report[0])))