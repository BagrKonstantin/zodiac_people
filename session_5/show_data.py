# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_data.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(220, 228, 236)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 100, 661, 431))
        self.tableWidget.setStyleSheet("background-color:white;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #NH737M;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 70, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #NH737M;")
        self.label_2.setObjectName("label_2")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(70, 40, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setStyleSheet("QPushButton\n"
"{\n"
"   background-color:rgb(56, 103, 214);\n"
"  color: white;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 11px;\n"
"}\n"
"  QPushButton:hover\n"
"{\n"
"  background-color:#4b7bec;\n"
"  mouse:pointer;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(50, 91, 189);\n"
"    border-width: 2px;\n"
"    border-style: rgba(0, 0, 0, 0.4);\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color:rgba(56, 103, 214, 0.6);\n"
"    border-style: inset;\n"
"}")
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(656, 40, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("QPushButton\n"
"{\n"
"   background-color:rgb(56, 103, 214);\n"
"  color: white;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 11px;\n"
"}\n"
"  QPushButton:hover\n"
"{\n"
"  background-color:#4b7bec;\n"
"  mouse:pointer;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(50, 91, 189);\n"
"    border-width: 2px;\n"
"    border-style: rgba(0, 0, 0, 0.4);\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color:rgba(56, 103, 214, 0.6);\n"
"    border-style: inset;\n"
"}")
        self.pushButton_add.setObjectName("pushButton_add")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Сумма"))
        self.label.setText(_translate("MainWindow", "Дата начала:"))
        self.label_2.setText(_translate("MainWindow", "Дата Окончания:"))
        self.pushButton_create.setText(_translate("MainWindow", "Сформировать"))
        self.pushButton_add.setText(_translate("MainWindow", "Добавить"))
