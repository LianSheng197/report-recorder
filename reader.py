# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reportReader.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.readDistinctButton = QtWidgets.QPushButton(self.centralwidget)
        self.readDistinctButton.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.readDistinctButton.setObjectName("readDistinctButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 621, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.readType1Button = QtWidgets.QPushButton(self.centralwidget)
        self.readType1Button.setGeometry(QtCore.QRect(280, 10, 80, 31))
        self.readType1Button.setObjectName("readType1Button")
        self.readType2Button = QtWidgets.QPushButton(self.centralwidget)
        self.readType2Button.setGeometry(QtCore.QRect(370, 10, 80, 31))
        self.readType2Button.setObjectName("readType2Button")
        self.readType3Button = QtWidgets.QPushButton(self.centralwidget)
        self.readType3Button.setGeometry(QtCore.QRect(460, 10, 80, 31))
        self.readType3Button.setObjectName("readType3Button")
        self.readAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.readAllButton.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.readAllButton.setObjectName("readAllButton")
        self.readHasShoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.readHasShoutButton.setGeometry(QtCore.QRect(190, 50, 80, 31))
        self.readHasShoutButton.setObjectName("readHasShoutButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.readType0Button = QtWidgets.QPushButton(self.centralwidget)
        self.readType0Button.setGeometry(QtCore.QRect(190, 10, 80, 31))
        self.readType0Button.setObjectName("readType0Button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.sortByBattleCountButton = QtWidgets.QPushButton(self.centralwidget)
        self.sortByBattleCountButton.setGeometry(QtCore.QRect(460, 50, 80, 31))
        self.sortByBattleCountButton.setObjectName("sortByBattleCountButton")
        self.sortByTimestampButton = QtWidgets.QPushButton(self.centralwidget)
        self.sortByTimestampButton.setGeometry(QtCore.QRect(550, 50, 80, 31))
        self.sortByTimestampButton.setObjectName("sortByTimestampButton")
        self.sortByIdButton = QtWidgets.QPushButton(self.centralwidget)
        self.sortByIdButton.setGeometry(QtCore.QRect(370, 50, 80, 31))
        self.sortByIdButton.setObjectName("sortByIdButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "歷史戰報閱讀器"))
        self.readDistinctButton.setText(_translate("MainWindow", "查詢不重複玩家"))
        self.readType1Button.setText(_translate("MainWindow", "認真決鬥"))
        self.readType2Button.setText(_translate("MainWindow", "決一死戰"))
        self.readType3Button.setText(_translate("MainWindow", "我要殺死你"))
        self.readAllButton.setText(_translate("MainWindow", "查詢所有戰報"))
        self.readHasShoutButton.setText(_translate("MainWindow", "有留言"))
        self.label_3.setText(_translate("MainWindow", "篩選屬性"))
        self.label_4.setText(_translate("MainWindow", "篩選類型"))
        self.readType0Button.setText(_translate("MainWindow", "友好切磋"))
        self.label_5.setText(_translate("MainWindow", "排序 高到低"))
        self.sortByBattleCountButton.setText(_translate("MainWindow", "依場數排序"))
        self.sortByTimestampButton.setText(_translate("MainWindow", "依時間排序"))
        self.sortByIdButton.setText(_translate("MainWindow", "預設排序"))
