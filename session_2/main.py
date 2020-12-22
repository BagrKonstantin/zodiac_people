from session_2.user_interface import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPrintDialog, QPrinter
import sqlite3
from PyQt5 import Qt
from PyQt5.QtGui import QPixmap
from prettytable import PrettyTable
import os

class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, file, db):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = db

        self.file = file

        self.pushButton_female.clicked.connect(self.swap_fem)
        self.pushButton_male.clicked.connect(self.swap_man)
        self.pushButton_female.setEnabled(False)

        self.pushButton_upload.clicked.connect(self.load_photo)

        self.pixmap = QPixmap(self.file)
        self.pixmap = self.pixmap.scaledToWidth(251)
        #self.pixmap.scaled(720, 405, QtCore.Qt.KeepAspectRatio)
        self.label_pic.setPixmap(self.pixmap)



        self.pushButton_save.clicked.connect(self.save)

        self.setFixedSize(800, 600)

    def get_data(self):
        surname = self.lineEdit_surname.text()
        name = self.lineEdit_name.text()
        second_name = self.lineEdit_second_name.text()
        is_man = not self.pushButton_male.isEnabled()
        email = self.lineEdit_email.text()
        age = self.spinBox_age.text()
        zodiac = self.comboBox_zodiac.currentText()
        talant = self.textEdit_talant.toPlainText()
        about = self.textEdit_about.toPlainText()
        file_path = "../img/" + self.file.split('/')[-1]
        return surname, name, second_name, ("Мужской" if is_man else "Женский"), email, age, zodiac, talant, about, file_path

    def load_photo(self):
        fname = QFileDialog.getOpenFileName(self, 'Выберите фото', '')[0]
        #self.lineEdit_for_pic.setText(fname)
        self.file = fname
        self.pixmap = QPixmap(self.file)
        self.pixmap = self.pixmap.scaledToWidth(251)
        self.label_pic.setPixmap(self.pixmap)

    def save(self):
        try:
            data = self.get_data()
            if all(data):
                print(*data)
                self.pixmap.save("../img/{}".format(data[-1]))
                con = sqlite3.connect(self.path)
                cur = con.cursor()
                cur.execute(
                    """insert into users (surname, name, second_name, sex, email, age, zodiac, talant, about, file_path) values ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")""".format(*data))
                con.commit()
                con.close()
                self.close()
            else:
                QMessageBox.critical(self, "Ошибка", "Вы ввели не все данные", QMessageBox.Ok)
        except Exception as error:
            print(error)

    def swap_fem(self):
        self.pushButton_male.setEnabled(True)
        self.pushButton_female.setEnabled(False)

    def swap_man(self):
        self.pushButton_male.setEnabled(False)
        self.pushButton_female.setEnabled(True)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("панасенков2.jpg", "../data.db")
    mainWindow.show()
    sys.exit(app.exec())