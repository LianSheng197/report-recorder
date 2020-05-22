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
        MainWindow.resize(631, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.readDistinctButton = QtWidgets.QPushButton(self.centralwidget)
        self.readDistinctButton.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.readDistinctButton.setObjectName("readDistinctButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 611, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.readType1Button = QtWidgets.QPushButton(self.centralwidget)
        self.readType1Button.setGeometry(QtCore.QRect(360, 50, 80, 31))
        self.readType1Button.setObjectName("readType1Button")
        self.readType2Button = QtWidgets.QPushButton(self.centralwidget)
        self.readType2Button.setGeometry(QtCore.QRect(450, 50, 80, 31))
        self.readType2Button.setObjectName("readType2Button")
        self.readType3Button = QtWidgets.QPushButton(self.centralwidget)
        self.readType3Button.setGeometry(QtCore.QRect(540, 50, 80, 31))
        self.readType3Button.setObjectName("readType3Button")
        self.readAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.readAllButton.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.readAllButton.setObjectName("readAllButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "歷史戰報閱讀器"))
        self.readDistinctButton.setText(_translate("MainWindow", "查詢不重複玩家"))
        self.readType1Button.setText(_translate("MainWindow", "認真對決"))
        self.readType2Button.setText(_translate("MainWindow", "決一死戰"))
        self.readType3Button.setText(_translate("MainWindow", "我要殺死你"))
        self.readAllButton.setText(_translate("MainWindow", "查詢所有戰報"))
        self.label.setText(_translate("MainWindow", "篩選類型"))
