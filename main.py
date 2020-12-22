from main_tab_window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog, QHBoxLayout
from PyQt5 import QtWidgets, QtGui, QtCore

from session_1.main import UI_Task1 as first_tab
from session_5.main import UI_Task1 as second_tab


class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')

        self.first_tab = first_tab(path)
        self.second_tab = second_tab(path)

        self.tabWidget.removeTab(2)
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(0)

        self.tabWidget.addTab(self.first_tab, "Участники")
        self.tabWidget.addTab(self.second_tab, "Расходы")

        self.setFixedSize(846, 668)



        # ёбаные одинэсеры, я перебью ваши семьи, друзей, собак, кошек, рыбок ваших нахуй




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("data.db")
    mainWindow.show()
    sys.exit(app.exec())