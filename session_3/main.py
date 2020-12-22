from session_3.show_window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPrintDialog, QPrinter
import sqlite3
from PyQt5 import Qt
from PyQt5.QtGui import QPixmap


class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, id, surname, name, second_name, sex, email, age, zodiac, talant, about, file_path):
        #
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.file = file_path

        self.pixmap = QPixmap(self.file)
        self.pixmap = self.pixmap.scaledToWidth(251)
        self.label_pic.setPixmap(self.pixmap)

        self.label_fio.setText("{} {} {}".format(name, surname, second_name))

        self.label_age.setText("Возраст: {}".format(age))
        self.label_zodiac.setText("Знак зодиака: {}".format(zodiac))
        self.textBrowser.setText(talant)
        self.label_sex.setText("Пол: {}".format(sex))
        self.textBrowser_2.setText(about)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 400, 731, 1000))

        self.pushButton_save.hide()
        self.textBrowser.setText(talant)

        self.setFixedSize(800, 600)




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1(1, "Константин", "Константинович", "Константинов и ещё 12 си", 21, "Скорпион",
                          "Сука почему мой талант должен ограничиваться 100 символами, а? Я что, какая то шутка для вас и ещё 9",
                          "Мужской",
                          "АААААААААзфпощшцыпуйрлзруейлрлоеурохзецолзхуклзщруйщшпощшпйущпкукйреощй35зщшрйщр4щшо5рощшх4цощз",
                          "../session_2/панасенков2.jpg")
    mainWindow.show()
    sys.exit(app.exec())
