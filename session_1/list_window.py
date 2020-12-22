# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 577)
        MainWindow.setStyleSheet("background-color:rgb(220, 228, 236)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 90, 681, 431))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("QTableWidget:item {\n"
"     border-radius: 20px;\n"
"     height:40px;\n"
"     background: white;\n"
"     padding: 0 8px;\n"
"    font: 14pt \"Segoe UI\";\n"
" }\n"
"QTableWidget {\n"
"     background: white;\n"
" }\n"
"\n"
"QTableWidget:item:selected{color: rgb(112, 126, 255);}\n"
"QTableWidget{border: 0px;}\n"
"QTableWidget{color: rgb(99, 175, 208)}\n"
"QTableWidget{font: 14pt \"Segoe UI\";}\n"
"QTableWidget {padding: 0px;} \n"
"QTableWidget {} \n"
"QTableWidget:horizontalHeader { margin:0px; \n"
"                                    background-color: black;\n"
"                color: #NH737M;     }")
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(134)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(280, 50, 80, 23))
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
        self.pushButton_card = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_card.setGeometry(QtCore.QRect(613, 50, 131, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_card.setFont(font)
        self.pushButton_card.setStyleSheet("QPushButton\n"
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
        self.pushButton_card.setObjectName("pushButton_card")
        self.pushButton_print = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_print.setGeometry(QtCore.QRect(528, 50, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_print.setFont(font)
        self.pushButton_print.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_print.setMouseTracking(True)
        self.pushButton_print.setStyleSheet("QPushButton\n"
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
        self.pushButton_print.setObjectName("pushButton_print")
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(60, 50, 72, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setStyleSheet("QPushButton\n"
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
        self.pushButton_search.setObjectName("pushButton_search")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 50, 141, 23))
        self.lineEdit.setStyleSheet("background-color:white;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(663, 530, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setStyleSheet("QPushButton\n"
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
        self.pushButton_update.setObjectName("pushButton_update")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Отчество"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Возраст"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Знак зодиака"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_create.setText(_translate("MainWindow", "Создать"))
        self.pushButton_card.setText(_translate("MainWindow", "Карточка участника"))
        self.pushButton_print.setText(_translate("MainWindow", "Печать"))
        self.pushButton_search.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_update.setText(_translate("MainWindow", "Обновить"))
