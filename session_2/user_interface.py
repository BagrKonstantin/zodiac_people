# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 596)
        MainWindow.setStyleSheet("background-color:rgb(220, 228, 236)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_surname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_surname.setGeometry(QtCore.QRect(440, 29, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_surname.setFont(font)
        self.lineEdit_surname.setStyleSheet("background-color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color:#3867d6;\n"
"border-radius: 3px;")
        self.lineEdit_surname.setText("")
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(440, 69, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("background-color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color:#3867d6;\n"
"border-radius: 3px;")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_second_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_second_name.setGeometry(QtCore.QRect(440, 109, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_second_name.setFont(font)
        self.lineEdit_second_name.setStyleSheet("background-color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color:#3867d6;\n"
"border-radius: 3px;")
        self.lineEdit_second_name.setObjectName("lineEdit_second_name")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 66, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 105, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 151, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 190, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 269, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.spinBox_age = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_age.setGeometry(QtCore.QRect(440, 230, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.spinBox_age.setFont(font)
        self.spinBox_age.setStyleSheet("background-color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color:#3867d6;\n"
"border-radius: 3px;")
        self.spinBox_age.setObjectName("spinBox_age")
        self.comboBox_zodiac = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_zodiac.setGeometry(QtCore.QRect(440, 271, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.comboBox_zodiac.setFont(font)
        self.comboBox_zodiac.setStyleSheet("QComboBox {\n"
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
        self.comboBox_zodiac.setObjectName("comboBox_zodiac")
        self.comboBox_zodiac.addItem("")
        self.comboBox_zodiac.addItem("")
        self.comboBox_zodiac.addItem("")
        self.comboBox_zodiac.addItem("")
        self.comboBox_zodiac.addItem("")
        self.comboBox_zodiac.addItem("")
        self.comboBox_zodiac.addItem("")
        self.comboBox_zodiac.addItem("")
        self.comboBox_zodiac.addItem("")
        self.comboBox_zodiac.addItem("")
        self.comboBox_zodiac.addItem("")
        self.comboBox_zodiac.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 320, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(440, 190, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("background-color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color:#3867d6;\n"
"border-radius: 3px;")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.textEdit_talant = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_talant.setGeometry(QtCore.QRect(440, 320, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textEdit_talant.setFont(font)
        self.textEdit_talant.setStyleSheet("background-color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color:#3867d6;\n"
"border-radius: 3px;")
        self.textEdit_talant.setObjectName("textEdit_talant")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 380, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textEdit_about = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_about.setGeometry(QtCore.QRect(20, 410, 761, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.textEdit_about.setFont(font)
        self.textEdit_about.setStyleSheet("background-color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color:#3867d6;\n"
"border-radius: 3px;")
        self.textEdit_about.setObjectName("textEdit_about")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(440, 150, 341, 33))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_female = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_female.sizePolicy().hasHeightForWidth())
        self.pushButton_female.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_female.setFont(font)
        self.pushButton_female.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_female.setStyleSheet("QPushButton\n"
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
"    cursor: not-allowed;\n"
"}")
        self.pushButton_female.setFlat(False)
        self.pushButton_female.setObjectName("pushButton_female")
        self.horizontalLayout.addWidget(self.pushButton_female)
        self.pushButton_male = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_male.sizePolicy().hasHeightForWidth())
        self.pushButton_male.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_male.setFont(font)
        self.pushButton_male.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_male.setStyleSheet("QPushButton\n"
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
"    cursor: not-allowed;\n"
"}")
        self.pushButton_male.setFlat(False)
        self.pushButton_male.setObjectName("pushButton_male")
        self.horizontalLayout.addWidget(self.pushButton_male)
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(710, 540, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_save.setStyleSheet("QPushButton\n"
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
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_upload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_upload.setGeometry(QtCore.QRect(20, 340, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_upload.setStyleSheet("QPushButton\n"
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
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(20, 30, 251, 291))
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_pic")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Фамилия:"))
        self.label_2.setText(_translate("MainWindow", "Имя:"))
        self.label_3.setText(_translate("MainWindow", "Отчество:"))
        self.label_4.setText(_translate("MainWindow", "Пол:"))
        self.label_5.setText(_translate("MainWindow", "E-mail:"))
        self.label_6.setText(_translate("MainWindow", "Возраст:"))
        self.label_7.setText(_translate("MainWindow", "Знак зодиака:"))
        self.comboBox_zodiac.setItemText(0, _translate("MainWindow", "Овен"))
        self.comboBox_zodiac.setItemText(1, _translate("MainWindow", "Телец"))
        self.comboBox_zodiac.setItemText(2, _translate("MainWindow", "Близнецы"))
        self.comboBox_zodiac.setItemText(3, _translate("MainWindow", "Рак"))
        self.comboBox_zodiac.setItemText(4, _translate("MainWindow", "Лев"))
        self.comboBox_zodiac.setItemText(5, _translate("MainWindow", "Дева"))
        self.comboBox_zodiac.setItemText(6, _translate("MainWindow", "Весы"))
        self.comboBox_zodiac.setItemText(7, _translate("MainWindow", "Скорпион"))
        self.comboBox_zodiac.setItemText(8, _translate("MainWindow", "Стрелец"))
        self.comboBox_zodiac.setItemText(9, _translate("MainWindow", "Козерог"))
        self.comboBox_zodiac.setItemText(10, _translate("MainWindow", "Водолей"))
        self.comboBox_zodiac.setItemText(11, _translate("MainWindow", "Рыбы"))
        self.label_8.setText(_translate("MainWindow", "Талант:"))
        self.label_9.setText(_translate("MainWindow", "О себе:"))
        self.pushButton_female.setText(_translate("MainWindow", "Женский"))
        self.pushButton_male.setText(_translate("MainWindow", "Мужской"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_upload.setText(_translate("MainWindow", "Загрузить"))
