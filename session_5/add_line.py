# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_line.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 379)
        MainWindow.setStyleSheet("background-color:rgb(220, 228, 236)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 501, 281))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color:#3867d6;\n"
"border-radius: 3px;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    background-color:white;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:#3867d6;\n"
"    border-radius: 3px;\n"
"    transition: 0.8;\n"
"}\n"
"\n"
"QComboBox::item{\n"
"    background-color:white;\n"
"    transition: 0.8;\n"
"}\n"
"QComboBox:editable {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.lineEdit_dis = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_dis.setFont(font)
        self.lineEdit_dis.setStyleSheet("background-color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color:#3867d6;\n"
"border-radius: 3px;")
        self.lineEdit_dis.setObjectName("lineEdit_dis")
        self.verticalLayout_2.addWidget(self.lineEdit_dis)
        self.lineEdit_price = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_price.setFont(font)
        self.lineEdit_price.setStyleSheet("background-color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color:#3867d6;\n"
"border-radius: 3px;")
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.verticalLayout_2.addWidget(self.lineEdit_price)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(450, 330, 71, 23))
        self.pushButton_add.setStyleSheet("QPushButton\n"
"{\n"
"   background-color:rgb(56, 103, 214);\n"
"   border-radius: 4px;\n"
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
        self.label.setText(_translate("MainWindow", "Дата:"))
        self.label_2.setText(_translate("MainWindow", "Категория:"))
        self.label_3.setText(_translate("MainWindow", "Краткое описание:"))
        self.label_4.setText(_translate("MainWindow", "Сумма:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Декорации"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Костюмы и грим"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Инвентарь"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Прочее"))
        self.pushButton_add.setText(_translate("MainWindow", "Добавить"))
