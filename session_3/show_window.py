# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 619)
        MainWindow.setStyleSheet("background-color:rgb(220, 228, 236)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(50, 60, 261, 291))
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_pic")
        self.label_sex = QtWidgets.QLabel(self.centralwidget)
        self.label_sex.setGeometry(QtCore.QRect(410, 350, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_sex.setFont(font)
        self.label_sex.setAutoFillBackground(False)
        self.label_sex.setStyleSheet("color: #NH737M;")
        self.label_sex.setObjectName("label_sex")
        self.label_fio = QtWidgets.QLabel(self.centralwidget)
        self.label_fio.setGeometry(QtCore.QRect(40, 10, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_fio.setFont(font)
        self.label_fio.setStyleSheet("color: #NH737M;")
        self.label_fio.setObjectName("label_fio")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #NH737M;")
        self.label_8.setObjectName("label_8")
        self.label_zodiac = QtWidgets.QLabel(self.centralwidget)
        self.label_zodiac.setGeometry(QtCore.QRect(410, 100, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_zodiac.setFont(font)
        self.label_zodiac.setStyleSheet("color: #NH737M;")
        self.label_zodiac.setObjectName("label_zodiac")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 360, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #NH737M;")
        self.label_9.setObjectName("label_9")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(710, 531, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("QPushButton\n"
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
        self.pushButton_save.setObjectName("pushButton_save")
        self.label_age = QtWidgets.QLabel(self.centralwidget)
        self.label_age.setGeometry(QtCore.QRect(410, 50, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_age.setFont(font)
        self.label_age.setStyleSheet("color: #NH737M;")
        self.label_age.setObjectName("label_age")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 400, 731, 121))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("QTextBrowser{border: 0px;}\n"
"")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(410, 220, 301, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFillBackground(True)
        self.textBrowser.setStyleSheet("QTextBrowser{border: 0px;}")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_sex.setText(_translate("MainWindow", "Пол: Мужской"))
        self.label_fio.setText(_translate("MainWindow", "Фамилия Имя Отчество"))
        self.label_8.setText(_translate("MainWindow", "Талант:"))
        self.label_zodiac.setText(_translate("MainWindow", "Знак зодиака:"))
        self.label_9.setText(_translate("MainWindow", "О себе:"))
        self.pushButton_save.setText(_translate("MainWindow", "Закрыть"))
        self.label_age.setText(_translate("MainWindow", "Возраст: 83"))
