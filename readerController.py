from PyQt5 import QtCore, QtWidgets, QtGui
from reader import Ui_MainWindow
import sqlite3
import time
import sys


class Reader(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Reader, self).__init__()
        self.setupUi(self)

        # 按鈕點擊事件註冊
        self.readAllButton.clicked.connect(self.readAll)
        self.readDistinctButton.clicked.connect(self.readDistinct)
        self.readType0Button.clicked.connect(self.readType0)
        self.readType1Button.clicked.connect(self.readType1)
        self.readType2Button.clicked.connect(self.readType2)
        self.readType3Button.clicked.connect(self.readType3)
        self.readHasShoutButton.clicked.connect(self.readHasShout)

        # 資料庫連線
        self.conn = sqlite3.connect('reports.sqlite3')
        self.c = self.conn.cursor()
        print("成功連接資料庫")

    # 查詢所有戰報
    def readAll(self):
        self.tableWidget.setSortingEnabled(False)
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
            self.tableWidget.setItem(rowPosition, 0, MyTableWidgetItem(str(report[0]), int(report[0])))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(report[1])))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(report[3])))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(report[4])))
            self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(report[5])))
            self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(report[6])))
            self.tableWidget.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(str("是" if report[8] == 1 else "否")))
            self.tableWidget.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(str(self.dateTime(report[9]))))

        self.setColumnWidth(8)
        self.tableWidget.setSortingEnabled(True)

    # 查詢不重複玩家
    def readDistinct(self):
        self.tableWidget.setSortingEnabled(False)
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

            playerName = report[0]
            battleCount = self.c.execute(
                f"select count(playerName) as counts from reports where playerName = '{playerName}'"
            ).fetchone()[0]

            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(playerName)))
            self.tableWidget.setItem(rowPosition, 1, MyTableWidgetItem(str(battleCount), int(battleCount)))

        self.setColumnWidth(2)
        self.tableWidget.setSortingEnabled(True)

    # 篩選：友好切磋
    def readType0(self):
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        headerName = ["id", "對手暱稱", "對手等級", "我方等級", "戰鬥種類", "戰鬥結果", "是否留言", "戰報時間"]
        self.tableWidget.setHorizontalHeaderLabels(headerName)

        reports = self.c.execute(
            ''' SELECT * FROM reports WHERE type = '友好切磋' '''
        ).fetchall()

        for report in reports:
            report = list(report)
            rowPosition = self.tableWidget.rowCount()

            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, MyTableWidgetItem(str(report[0]), int(report[0])))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(report[1])))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(report[3])))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(report[4])))
            self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(report[5])))
            self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(report[6])))
            self.tableWidget.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(str("是" if report[8] == 1 else "否")))
            self.tableWidget.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(str(self.dateTime(report[9]))))

        self.setColumnWidth(8)
        self.tableWidget.setSortingEnabled(True)

    # 篩選：認真決鬥
    def readType1(self):
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        headerName = ["id", "對手暱稱", "對手等級", "我方等級", "戰鬥種類", "戰鬥結果", "是否留言", "戰報時間"]
        self.tableWidget.setHorizontalHeaderLabels(headerName)

        reports = self.c.execute(
            ''' SELECT * FROM reports WHERE type = '認真決鬥' '''
        ).fetchall()

        for report in reports:
            report = list(report)
            rowPosition = self.tableWidget.rowCount()

            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, MyTableWidgetItem(str(report[0]), int(report[0])))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(report[1])))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(report[3])))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(report[4])))
            self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(report[5])))
            self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(report[6])))
            self.tableWidget.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(str("是" if report[8] == 1 else "否")))
            self.tableWidget.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(str(self.dateTime(report[9]))))

        self.setColumnWidth(8)
        self.tableWidget.setSortingEnabled(True)

    # 篩選：決一死戰
    def readType2(self):
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        headerName = ["id", "對手暱稱", "對手等級", "我方等級", "戰鬥種類", "戰鬥結果", "是否留言", "戰報時間"]
        self.tableWidget.setHorizontalHeaderLabels(headerName)

        reports = self.c.execute(
            ''' SELECT * FROM reports WHERE type = '決一死戰' '''
        ).fetchall()

        for report in reports:
            report = list(report)
            rowPosition = self.tableWidget.rowCount()

            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, MyTableWidgetItem(str(report[0]), int(report[0])))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(report[1])))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(report[3])))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(report[4])))
            self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(report[5])))
            self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(report[6])))
            self.tableWidget.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(str("是" if report[8] == 1 else "否")))
            self.tableWidget.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(str(self.dateTime(report[9]))))

        self.setColumnWidth(8)
        self.tableWidget.setSortingEnabled(True)

    # 篩選：我要殺死你
    def readType3(self):
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        headerName = ["id", "對手暱稱", "對手等級", "我方等級", "戰鬥種類", "戰鬥結果", "是否留言", "戰報時間"]
        self.tableWidget.setHorizontalHeaderLabels(headerName)

        reports = self.c.execute(
            ''' SELECT * FROM reports WHERE type = '我要殺死你' '''
        ).fetchall()

        for report in reports:
            report = list(report)
            rowPosition = self.tableWidget.rowCount()

            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, MyTableWidgetItem(str(report[0]), int(report[0])))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(report[1])))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(report[3])))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(report[4])))
            self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(report[5])))
            self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(report[6])))
            self.tableWidget.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(str("是" if report[8] == 1 else "否")))
            self.tableWidget.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(str(self.dateTime(report[9]))))

        self.setColumnWidth(8)
        self.tableWidget.setSortingEnabled(True)

    # 篩選：有留言
    def readHasShout(self):
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        headerName = ["id", "對手暱稱", "對手等級", "我方等級", "戰鬥種類", "戰鬥結果", "是否留言", "戰報時間"]
        self.tableWidget.setHorizontalHeaderLabels(headerName)

        reports = self.c.execute(
            ''' SELECT * FROM reports WHERE hasShout = 1 '''
        ).fetchall()

        for report in reports:
            report = list(report)
            rowPosition = self.tableWidget.rowCount()

            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, MyTableWidgetItem(str(report[0]), int(report[0])))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(report[1])))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(report[3])))
            self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(report[4])))
            self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(report[5])))
            self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(report[6])))
            self.tableWidget.setItem(rowPosition, 6, QtWidgets.QTableWidgetItem(str("是" if report[8] == 1 else "否")))
            self.tableWidget.setItem(rowPosition, 7, QtWidgets.QTableWidgetItem(str(self.dateTime(report[9]))))

        self.setColumnWidth(8)
        self.tableWidget.setSortingEnabled(True)

    def dateTime(self, timestamp):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timestamp / 1000))

    def setColumnWidth(self, columnCount):
        for i in range(columnCount):
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

# 自定義排序，針對數字
# 僅需要在需數字排序的資料用上即可
class MyTableWidgetItem(QtWidgets.QTableWidgetItem):
    def __init__(self, text, sortKey):
        QtWidgets.QTableWidgetItem.__init__(self, text, QtWidgets.QTableWidgetItem.UserType)
        self.sortKey = sortKey

    def __lt__(self, other):
        return self.sortKey < other.sortKey 