import sys
from main import Smart
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QStackedWidget,
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QGridLayout,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Auto_predpriyatie")
#         self.widget_main = QWidget()
#         self.page1 = QGridLayout(self.widget_main)
#         self.label = QLabel()
#
#         # self.back_button_one = QPushButton("Назад")
#         # self.back_button_one.clicked.connect(self.the_back_button_one_was_clicked)
#
#         self.button_accounts = QPushButton("per")
#         self.button_accounts.clicked.connect(self.the_button_accounts_was_clicked)
#
#         self.page1.addWidget(self.button_accounts, 0, 0)
#         self.page1.addWidget(self.label, 1, 0)
#         self.setCentralWidget(self.widget_main)
#     def the_button_accounts_was_clicked(self):
#         window = DoMainWindow()
#         window.show()
# class DoMainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("huita")
#         self.widget_amin = QWidget()
#         self.page2 = QGridLayout(self.widget_amin)
#         self.label2 = QLabel()
#         self.setCentralWidget(self.widget_amin)
#

        # self.back_button_one = QPushButton("Назад")
        # self.back_button_one.clicked.connect(self.the_back_button_one_was_clicked)
        #
        # self.button_accounts = QPushButton("Посмотреть аккаунты сети")
        # self.button_accounts.clicked.connect(self.the_button_accounts_was_clicked)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


    #     self.setWindowTitle("Auto_predpriyatie")
    #     self.widget_main = QWidget()
    #     self.page1 = QGridLayout(self.widget_main)
    #     self.label = QLabel()
    #
    #     self.back_button_one = QPushButton("Посмотреть аккаунты сети")
    #     self.back_button_one.clicked.connect(self.the_back_button_one_was_clicked)
    #
    #     self.page1.addWidget(self.back_button_one, 0, 0)
    #     self.page1.addWidget(self.label, 1, 0)
    #
    #     # ------------------------------------------------------------------
    #
    #     self.widget_users = QWidget()
    #     self.page_users = QGridLayout(self.widget_users)
    #
    #     self.button_setSimpleUser = QPushButton("Задать своё имя")
    #
    #     self.page_users.addWidget(self.button_setSimpleUser, 1, 0)
    #
    #     self.setWindowTitle("My App")
    #
    #     layout = QStackedWidget()
    #
    #     layout.addWidget(self.widget_main)
    #     layout.addWidget(self.widget_users)
    #
    #     layout.currentWidget()
    #
    #
    #
    #
    #     widget = QWidget()
    #     widget.setLayout(layout)
    #     self.setCentralWidget(widget)
    #
    # def the_back_button_one_was_clicked(self):
    #     self.layout.currentIndex(1)
    #     self.widget.setLayout(self.layout)
    #     self.setCentralWidget(self.widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
