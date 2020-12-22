from session_1.list_window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from session_2 import main as create_card
from session_3 import main as show_card

from PyQt5.Qt import QPrintDialog, QPrinter
import sqlite3
from PyQt5 import Qt
from PyQt5.QtGui import QPixmap
from prettytable import PrettyTable
import os

class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = path

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute("""Select * from users""").fetchall()
        con.close()

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        self.update_table()

        self.pushButton_update.clicked.connect(self.update_data)


        self.pushButton_card.clicked.connect(self.show_card)
        self.pushButton_create.clicked.connect(self.create_card)

        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_print.clicked.connect(self.print)

        self.setFixedSize(800, 600)

    def print(self):
        th = ["Фамилия", "Имя", "Отчество", "Возраст", "Знак Зодиака"]

        td = []
        for i in range(self.tableWidget.rowCount()):
            for j in range(5):
                td.append(self.tableWidget.item(i, j).text())

        columns = len(th)  # Подсчитаем кол-во столбцов на будущее.

        table = PrettyTable(th)  # Определяем таблицу.

        # Cкопируем список td, на случай если он будет использоваться в коде дальше.
        td_data = td[:]
        # Входим в цикл который заполняет нашу таблицу.
        # Цикл будет выполняться до тех пор пока у нас не кончатся данные
        # для заполнения строк таблицы (список td_data).
        while td_data:
            # Используя срез добавляем первые пять элементов в строку.
            # (columns = 5).
            table.add_row(td_data[:columns])
            # Используя срез переопределяем td_data так, чтобы он
            # больше не содержал первых 5 элементов.
            td_data = td_data[columns:]

        print(str(table))  # Печатаем таблицу

        #
        # import fpdf  # pip3 intall fpdf
        #
        # pdf = fpdf.FPDF()
        # pdf.add_page()
        # pdf.add_font('DejaVu', '', 'Roboto-Light.ttf', uni=False)
        # pdf.set_font("Arial", size=12)
        # pdf.cell(200, 10, txt=str(table), ln=1, align="C")
        # pdf.output("test.pdf")

        # Если вы, девчонки, выберетесь из учебки, если вы переживёте курс молодого бойца, вы станете оружием,
        # посланниками смерти, молящими о том, чтобы началась война! Но до этого дня вы просто блевотина! Вы низшая
        # форма жизни на земле! Вы вообще нихуя не люди! Вы всего лишь неорганизованная стая скользких
        # вонючих жаб! Я строг и поэтому я вам не понравлюсь! Но чем больше вы будете меня ненавидеть,
        # тем большему вы научитесь! Я строг, но я справедлив! У меня здесь нет расовой дискриминации,
        # мне насрать на черножопых, на жыдов, на макаронников и на латиносов! Вы все здесь одинаково никчёмны!
        # Моя задача – избавится от тех, кто неспособен служить в моей любимой морской пехоте! Вам это понятно, мрази?


        #
        doc = QtGui.QTextDocument(str(table))
        printer = QPrinter()
        dialog = QPrintDialog(printer)
        if dialog.exec_():
            with open("test.txt", "w") as doc:
                doc.write(str(table))
            os.startfile("test.txt", "print")

    def update_data(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute("""Select * from users""").fetchall()
        con.close()

        self.lineEdit.setText("")
        self.update_table()

    def search(self):
        try:
            print(self.data)
            text = self.lineEdit.text()
            if text:
                self.data = [i for i in self.data if any([True for j in i if text in str(j)])]
            else:
                con = sqlite3.connect(self.path)
                cur = con.cursor()
                self.data = cur.execute("""Select * from users""").fetchall()
                con.close()
            self.update_table()
        except Exception as error:
            print(error)


    def update_table(self):
        self.tableWidget.setRowCount(0)

        n = len(self.data)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
            self.tableWidget.setItem(i, 2, QTableWidgetItem())
            self.tableWidget.setItem(i, 3, QTableWidgetItem())
            self.tableWidget.setItem(i, 4, QTableWidgetItem())

            self.tableWidget.item(i, 0).setText(self.data[i][1])
            self.tableWidget.item(i, 1).setText(self.data[i][2])
            self.tableWidget.item(i, 2).setText(self.data[i][3])

            self.tableWidget.item(i, 3).setText(str(self.data[i][6]))
            self.tableWidget.item(i, 4).setText(self.data[i][7])



        # for n in range(3):
        #     for i in range(5):
        #         self.tableWidget.setItem(n, i, QTableWidgetItem())
        #         self.tableWidget.item(n, i).setText("{}{}".format(n, i))


    def create_card(self):
        print(self.tableWidget.verticalHeader().sortIndicatorSection())
        self.windoww = create_card.UI_Task1("", self.path)
        self.windoww.show()

    def show_card(self):
        try:
            n = self.tableWidget.currentRow()
            print(n)

            self.windoww = show_card.UI_Task1(*self.data[n])
            self.windoww.show()
        except Exception as error:
            print(error)




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("../data.db")
    mainWindow.show()
    sys.exit(app.exec())