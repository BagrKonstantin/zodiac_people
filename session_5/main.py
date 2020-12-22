from session_5.show_data import Ui_MainWindow
from  session_5.add_line import Ui_MainWindow as Ui_Dialog
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPrintDialog, QPrinter
import sqlite3
from PyQt5 import Qt
from PyQt5.QtGui import QPixmap
from prettytable import PrettyTable
import os
import datetime

class Dialog(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        parent.setDisabled(True)
        self.parent = parent
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Dialog')

        self.dateEdit = QtWidgets.QDateEdit(self)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)  # +++
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setGeometry(QtCore.QRect(235, 50, 285, 40))

        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setStyleSheet("""border-style: outset;
        border-width: 1px;
        border-color:#3867d6;
        border-radius: 3px;""")

        self.pushButton_add.clicked.connect(self.www)
        self.setFixedSize(544, 379)

    def closeEvent(self, event):
        self.parent.setDisabled(False)
        event.accept()

    def www(self):
        try:
            time = "-".join(self.dateEdit.text().split(".")[::-1])
            category = self.comboBox.currentText()
            discription = self.lineEdit_dis.text()
            price = self.lineEdit_price.text().replace(",", ".")
            price = str(round(float(price), 2))
            print(price)
            a = [category, discription, price, time]

            if not all(a):
                raise Exception
            con = sqlite3.connect(self.parent.path)
            cur = con.cursor()
            cur.execute(
                """insert into pays (category, discription, price, time) values ("{}","{}", {},"{}")""".format(category,
                                                                                                               discription,
                                                                                                               price,
                                                                                                               time))
            con.commit()
            con.close()

            self.parent.update_data()
            self.close()
        except Exception as error:
            print(error)
            QMessageBox.critical(self, "Ошибка", "Вводите данные корректно", QMessageBox.Ok)










class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, file):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')

        self.path = file

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


        # self.data = {"Декорации": {"Декор и море": 1000.00, "Декор луг": 2000.50},
        #         "Костюмы и грим": {"Платье": 1500.00, "Макияж": 500.00, "грим кот": 700.00}}



        now = datetime.datetime.now()

        self.tableWidget.verticalHeader().sectionClicked.connect(self.update_k)

        self.dateEdit1 = QtWidgets.QDateEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit1.setFont(font)
        self.dateEdit1.setCalendarPopup(True)  # +++
        self.dateEdit1.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit1.setGeometry(QtCore.QRect(220, 65, 133, 30))
        self.dateEdit1.setStyleSheet("""border-style: outset;
border-width: 1px;
border-color:#3867d6;
border-radius: 3px;""")

        self.dateEdit1.setDate(QtCore.QDate.currentDate())

        self.dateEdit2 = QtWidgets.QDateEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit2.setFont(font)
        self.dateEdit2.setCalendarPopup(True)  # +++
        self.dateEdit2.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit2.setGeometry(QtCore.QRect(600, 65, 133, 30))

        self.dateEdit2.setDate(QtCore.QDate.currentDate())

        self.dateEdit2.setStyleSheet("""border-style: outset;
        border-width: 1px;
        border-color:#3867d6;
        border-radius: 3px;""")

        self.pushButton_add.clicked.connect(self.add_line)
        self.pushButton_create.clicked.connect(self.update_data)

        self.get_data()

        self.data_k = dict()
        for i in self.data.keys():
            self.data_k[i] = False

        self.tableWidget.setRowCount(len(self.data.keys()))
        self.tableWidget.cellClicked.connect(self.update_k)


        self.update_data()

        self.setFixedSize(800, 600)

    def get_data(self):
        a = "-".join(self.dateEdit1.text().split(".")[::-1])
        b = "-".join(self.dateEdit2.text().split(".")[::-1])
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        data = cur.execute("""SELECT * from pays WHERE strftime('%s', time) - strftime('%s', "{}") >= 0 AND strftime('%s', "{}") - strftime('%s', time) >= 0""".format(a, b)).fetchall()
        con.close()
        print(data)
        self.data = {"Декорации": {},
                     "Костюмы и грим": {},
                     "Инвентарь": {},
                     "Прочее": {}}
        for i in data:
            self.data[i[1]][i[2]] = i[3]



    def add_line(self):
        try:
            dialog = Dialog(self)
            dialog.show()
        except Exception as error:
            print(error)

    def update_k(self):
        if self.tableWidget.currentColumn() == 0:
            word = self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn()).text()
            if word in self.data.keys():
                if self.data_k[word]:
                    self.data_k[word] = False
                else:
                    self.data_k[word] = True

                self.update_data()

    def update_data(self):
        self.get_data()

        self.tableWidget.setRowCount(0)
        n = len(self.data.keys()) + sum(len(self.data[i].keys()) for i in self.data.keys() if self.data_k[i] == True)
        self.tableWidget.setRowCount(n)
        row = 0
        try:
            for i in self.data.keys():
                self.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem())
                self.tableWidget.verticalHeaderItem(row).setText(" + ")
                self.tableWidget.verticalHeaderItem(row).setFlags(QtCore.Qt.ItemIsEditable)

                self.tableWidget.setItem(row, 0, QTableWidgetItem())
                self.tableWidget.setItem(row, 1, QTableWidgetItem())

                self.tableWidget.item(row, 1).setFlags(QtCore.Qt.ItemIsEditable)

                self.tableWidget.item(row, 0).setText(i)
                row += 1
                if self.data_k[i]:
                    self.tableWidget.verticalHeaderItem(row - 1).setText(" -  ")
                    self.tableWidget.verticalHeaderItem(row - 1).setFlags(QtCore.Qt.ItemIsEditable)
                    for j in self.data[i].keys():
                        self.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem())
                        self.tableWidget.verticalHeaderItem(row).setText("")
                        self.tableWidget.verticalHeaderItem(row).setFlags(QtCore.Qt.ItemIsEditable)

                        self.tableWidget.setItem(row, 0, QTableWidgetItem())
                        self.tableWidget.setItem(row, 1, QTableWidgetItem())
                        self.tableWidget.item(row, 0).setText("            " + j)
                        self.tableWidget.item(row, 1).setText(str(self.data[i][j]))

                        self.tableWidget.item(row, 0).setFlags(QtCore.Qt.ItemIsEditable)
                        self.tableWidget.item(row, 1).setFlags(QtCore.Qt.ItemIsEditable)
                        row += 1
        except Exception as error:
            print(error)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("../data.db")
    mainWindow.show()
    sys.exit(app.exec())
