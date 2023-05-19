import sys
from main import Smart
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
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


# Подкласс QMainWindow для настройки основного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto_predpriyatie")
        self.widget_main = QWidget()
        self.page1 = QGridLayout(self.widget_main)
        self.label = QLabel()

        self.back_button_one = QPushButton("Назад")
        self.back_button_one.clicked.connect(self.the_back_button_one_was_clicked)

        self.button_accounts = QPushButton("Посмотреть аккаунты сети")
        self.button_accounts.clicked.connect(self.the_button_accounts_was_clicked)

        self.button_users = QPushButton("Данные о пользователях")
        self.button_users.clicked.connect(self.the_button_users_was_clicked)

        self.button_auto = QPushButton("Данные о автопарке")
        self.button_auto.clicked.connect(self.the_button_auto_was_clicked)

        self.button_trip = QPushButton("Данные о поездках")
        self.button_trip.clicked.connect(self.the_button_trip_was_clicked)

        self.button_balance = QPushButton("Данные о балансе")
        self.button_balance.clicked.connect(self.the_button_balance_was_clicked)

        self.button_adm = QPushButton("Функции администратора")
        self.button_adm.clicked.connect(self.the_button_adm_was_clicked)

        self.page1.addWidget(self.button_accounts, 0, 0)
        self.page1.addWidget(self.label, 1, 0)
        self.page1.addWidget(self.button_users, 2, 0)
        self.page1.addWidget(self.button_auto, 3, 0)
        self.page1.addWidget(self.button_trip, 4, 0)
        self.page1.addWidget(self.button_balance, 5, 0)
        self.page1.addWidget(self.button_adm, 6, 0)



#------------------------------------------------------------------

        self.widget_users = QWidget()
        self.page_users = QGridLayout(self.widget_users)

        self.button_setSimpleUser = QPushButton("Задать своё имя")
        self.input_setSimpleUser = QLineEdit(self)
        self.button_setSimpleUser.clicked.connect(self.the_button_setSimpleUser_was_clicked)

        self.button_getUser = QPushButton("Получить данные о пользователе")
        self.button_getUser.clicked.connect(self.the_button_getUser_was_clicked)
        self.input_getUser = QLineEdit(self)
        self.getUser_out = QLabel()

        self.button_getUserRole = QPushButton("Получить данные о роли пользователя")
        self.button_getUserRole.clicked.connect(self.the_button_getUserRole_was_clicked)
        self.input_getUserRole = QLineEdit(self)
        self.getUserRole_out = QLabel()

        self.page_users.addWidget(self.input_setSimpleUser, 0, 0)
        self.page_users.addWidget(self.button_setSimpleUser, 1, 0)
        self.page_users.addWidget(self.input_getUser, 2, 0)
        self.page_users.addWidget(self.button_getUser, 3, 0)
        self.page_users.addWidget(self.getUser_out, 4, 0)
        self.page_users.addWidget(self.input_getUserRole, 5, 0)
        self.page_users.addWidget(self.button_getUserRole, 6, 0)
        self.page_users.addWidget(self.getUserRole_out, 7, 0)
        self.page_users.addWidget(self.back_button_one, 8, 0)

#------------------------------------------------------------------
        self.widget_auto = QWidget()
        self.page_auto = QGridLayout(self.widget_auto)

        self.button_setSostBus = QPushButton("Изменить состояние автобуса")
        self.button_setSostBus.clicked.connect(self.the_button_setSostBus_was_clicked)
        self.input_setSostBus = QLineEdit(self)

        self.button_getSostBus = QPushButton("Получить данные о состоянии автобуса")
        self.button_getSostBus.clicked.connect(self.the_button_getSostBus_was_clicked)
        self.input_getSostBus = QLineEdit(self)
        self.getSostBus_out = QLabel()

        self.page_auto.addWidget(self.input_setSostBus, 0, 0)
        self.page_auto.addWidget(self.button_setSostBus, 1, 0)
        self.page_auto.addWidget(self.input_getSostBus, 2, 0)
        self.page_auto.addWidget(self.button_getSostBus, 3, 0)
        self.page_auto.addWidget(self.getSostBus_out, 4, 0)

#------------------------------------------------------------------
        self.widget_trip = QWidget()
        self.page_trip = QGridLayout(self.widget_trip)

        self.button_getInfoOfTrip = QPushButton("Получить данные о маршруте")
        self.button_getInfoOfTrip.clicked.connect(self.the_button_getInfoOfTrip_was_clicked)
        self.input_getInfoOfTrip = QLineEdit(self)
        self.getInfoOfTrip_out = QLabel()

        self.button_getTripPrise = QPushButton("Получить данные о цене поездки")
        self.button_getTripPrise.clicked.connect(self.the_button_getTripPrise_was_clicked)
        self.input_getTripPrise = QLineEdit(self)
        self.getTripPrise_out = QLabel()

        self.button_getPeopleInTrip = QPushButton("Получить данные о пассажирах")
        self.button_getPeopleInTrip.clicked.connect(self.the_button_getPeopleInTrip_was_clicked)
        self.input_getPeopleInTrip = QLineEdit(self)
        self.getPeopleInTrip_out = QLabel()

        self.page_trip.addWidget(self.input_getInfoOfTrip, 0, 0)
        self.page_trip.addWidget(self.button_getInfoOfTrip, 1, 0)
        self.page_trip.addWidget(self.getInfoOfTrip_out, 2, 0)
        self.page_trip.addWidget(self.input_getTripPrise, 3, 0)
        self.page_trip.addWidget(self.button_getTripPrise, 4, 0)
        self.page_trip.addWidget(self.getTripPrise_out, 5, 0)
        self.page_trip.addWidget(self.input_getPeopleInTrip, 6, 0)
        self.page_trip.addWidget(self.button_getPeopleInTrip, 7, 0)
        self.page_trip.addWidget(self.getPeopleInTrip_out, 8, 0)


#------------------------------------------------------------------
        self.widget_balance = QWidget()
        self.page_balance = QGridLayout(self.widget_balance)

        self.button_addUserInTrip = QPushButton("Купить билет")
        self.button_addUserInTrip.clicked.connect(self.the_button_addUserInTrip_was_clicked)
        self.input_addUserInTrip = QLineEdit(self)

        self.button_pay = QPushButton("Пополнить баланс")
        self.button_pay.clicked.connect(self.the_button_pay_was_clicked)
        self.input_pay = QLineEdit(self)

        self.button_getBalance = QPushButton("Просмотреть баланс")
        self.button_getBalance.clicked.connect(self.the_button_getBalance_was_clicked)
        self.input_getBalance = QLineEdit(self)
        self.out_getBalance = QLabel()

        self.page_balance.addWidget(self.input_addUserInTrip, 0, 0)
        self.page_balance.addWidget(self.button_addUserInTrip, 1, 0)
        self.page_balance.addWidget(self.input_pay, 2, 0)
        self.page_balance.addWidget(self.button_pay, 3, 0)
        self.page_balance.addWidget(self.input_getBalance, 4, 0)
        self.page_balance.addWidget(self.button_getBalance, 5, 0)
        self.page_balance.addWidget(self.out_getBalance, 6, 0)
#------------------------------------------------------------------
        self.widget_adm = QWidget()
        self.page_adm = QGridLayout(self.widget_adm)

        self.button_moneyHome = QPushButton("Вывести деньги с контракта")
        self.button_moneyHome.clicked.connect(self.the_button_moneyHome_was_clicked)
        self.input_moneyHome = QLineEdit(self)

        self.button_setTrip = QPushButton("Добавить маршрут")
        self.button_setTrip.clicked.connect(self.the_button_setTrip_was_clicked)
        self.input_setTrip = QLineEdit(self)

        self.button_setBus = QPushButton("Добавить автобус")
        self.button_setBus.clicked.connect(self.the_button_setBus_was_clicked)
        self.input_setBus = QLineEdit(self)

        self.button_setPersonUser = QPushButton("Добавить персонал")
        self.button_setPersonUser.clicked.connect(self.the_button_setPersonUser_was_clicked)
        self.input_setPersonUser = QLineEdit(self)

        self.page_adm.addWidget(self.input_setPersonUser, 0, 0)
        self.page_adm.addWidget(self.button_setPersonUser, 1, 0)
        self.page_adm.addWidget(self.input_setBus, 2, 0)
        self.page_adm.addWidget(self.button_setBus, 3, 0)
        self.page_adm.addWidget(self.input_setTrip, 4, 0)
        self.page_adm.addWidget(self.button_setTrip, 5, 0)
        self.page_adm.addWidget(self.input_moneyHome, 6, 0)
        self.page_adm.addWidget(self.button_moneyHome, 7, 0)

#------------------------------------------------------------------
#------------------------------------------------------------------
        self.widget_first = QWidget()
        self.page_first = QGridLayout(self.widget_first)

        self.input_login = QLineEdit(self)
        self.input_login_password = QLineEdit(self)
        self.button_login = QPushButton("Вход")
        self.button_login.clicked.connect(self.the_button_login_was_clicked)

        self.button_signin = QPushButton("Регистрация")
        self.button_signin.clicked.connect(self.the_button_signin_was_clicked)

        self.button_signin_final = QPushButton("Зарегистрироваться")
        self.button_signin_final.clicked.connect(self.the_button_signin_final_was_clicked)


        self.widget_signin = QWidget()
        self.page_signin = QGridLayout(self.widget_signin)

        self.input_signin = QLineEdit(self)
        self.input_signin_password = QLineEdit(self)

        self.page_first.addWidget(self.input_login, 0, 0)
        self.page_first.addWidget(self.input_login_password, 1, 0)
        self.page_first.addWidget(self.button_login, 2, 0)
        self.page_first.addWidget(self.button_signin, 3, 0)

        self.page_signin.addWidget(self.input_signin, 0, 0)
        self.page_signin.addWidget(self.input_signin_password, 1, 0)
        self.page_signin.addWidget(self.button_signin_final, 2, 0)

#------------------------------------------------------------------
        # Устанавливаем центральный виджет Window.
        #self.setCentralWidget(self.widget_main)
        layout = QStackedLayout()

        layout.addWidget(self.widget_main)
        layout.addWidget(self.widget_users)

        layout.setCurrentIndex(0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
#------------------------------------------------------------------
#------------------------------------------------------------------

    def the_button_signin_was_clicked(self):
        self.setCentralWidget(self.widget_signin)

    def the_button_login_was_clicked(self):
        ob = Smart()
        if(ob.LogIn(self.input_login.text(), self.input_login_password.text())):
            self.setCentralWidget(self.widget_main)
        else:
            self.setCentralWidget(self.widget_first)

    def the_button_signin_final_was_clicked(self):
        ob = Smart()
        print(self.input_signin.text(), self.input_signin_password.text())#ob.SignIn
#----------------------------------------------------------------
#------------------------------------------------------------------
    def the_button_accounts_was_clicked(self):
        ob = Smart()
        a = ob.accounts()
        s = ''
        for i in a:
            s += str(i) + '\n'
        self.label.setText(s)

    def the_button_users_was_clicked(self):
        self.setCentralWidget(self.widget_users)

    def the_button_auto_was_clicked(self):
        self.setCentralWidget(self.widget_auto)

    def the_button_trip_was_clicked(self):
        self.setCentralWidget(self.widget_trip)

    def the_button_balance_was_clicked(self):
        self.setCentralWidget(self.widget_balance)

    def the_back_button_one_was_clicked(self):#не работает
        self.setCentralWidget(self.widget_main)

    def the_button_adm_was_clicked(self):
        self.setCentralWidget(self.widget_adm)

#------------------------------------------------------------------
#------------------------------------------------------------------

    def the_button_setSimpleUser_was_clicked(self):
        mass = self.input_setSimpleUser.text().split()
        ob = Smart()
        ob.setSimpleUser(mass[0], mass[1])


    def the_button_getUser_was_clicked(self):
        mass = self.input_getUser.text().split()
        ob = Smart()
        a = ob.getUser(mass[0])
        self.getUser_out.setText(a)
    def the_button_getUserRole_was_clicked(self):
        mass = self.input_getUserRole.text().split()
        ob = Smart()
        a = ob.getUserRole(mass[0])
        if(a == 0):
            a = "Пассажир"
        elif (a == 1):
            a = "Инженер-технолог"
        elif (a == 2):
            a = "Водитель"
        elif (a == 3):
            a = "Кондуктор"
        elif (a == 4):
            a = "Администратор"
        self.getUserRole_out.setText(str(a))

#------------------------------------------------------------------
#------------------------------------------------------------------
    def the_button_setSostBus_was_clicked(self):
        mass = self.input_setSostBus.text().split()
        ob = Smart()
        a = ob.setSostBus(int(mass[0]),bool(mass[1]),mass[2])

    def the_button_getSostBus_was_clicked(self):
        mass = self.input_getSostBus.text().split()
        a = Smart().getSostBus(int(mass[0]),mass[1])

        if(a):
            self.getSostBus_out.setText("Исправен")
        else:
            self.getSostBus_out.setText("Сломан")
#------------------------------------------------------------------
#------------------------------------------------------------------
    def the_button_getInfoOfTrip_was_clicked(self):
        mass = self.input_getInfoOfTrip.text().split()
        ob = Smart()
        a = ob.getInfoOfTrip(int(mass[0]))
        self.getInfoOfTrip_out.setText(str(a))

    def the_button_getTripPrise_was_clicked(self):
        mass = self.input_getTripPrise.text().split()
        ob = Smart()
        a = ob.getTripPrise(int(mass[0]))
        self.getTripPrise_out.setText(str(a))

    def the_button_getPeopleInTrip_was_clicked(self):
        mass = self.input_getPeopleInTrip.text().split()
        ob = Smart()
        a = ob.getPeopleInTrip(int(mass[0]),mass[1])
        s = ''
        for i in a:
            s += str(i) + '\n'

        self.getTripPrise_out.setText(s)

#------------------------------------------------------------------
#------------------------------------------------------------------
    def the_button_addUserInTrip_was_clicked(self):
        mass = self.input_addUserInTrip.text().split()
        ob = Smart()
        a = ob.addUserInTrip(int(mass[0]),mass[1])

    def the_button_pay_was_clicked(self):
        mass = self.input_pay.text().split()
        ob = Smart()
        a = ob.pay(mass[0],mass[1])

    def the_button_getBalance_was_clicked(self):
        mass = self.input_getBalance.text().split()
        ob = Smart()
        a = ob.getBalance(mass[0])
        self.out_getBalance.setText(str(a))
#------------------------------------------------------------------
#------------------------------------------------------------------

    def the_button_moneyHome_was_clicked(self):
        mass = self.input_moneyHome.text().split()
        ob = Smart()
        a = ob.moneyHome(mass[0])

    def the_button_setTrip_was_clicked(self):
        mass = self.input_setTrip.text().split()
        ob = Smart()
        a = ob.setTrip(int(mass[0]),mass[1],mass[2],int(mass[3]),int(mass[4]),mass[5])

    def the_button_setBus_was_clicked(self):
        mass = self.input_setBus.text().split()
        ob = Smart()
        a = ob.setBus(int(mass[0]),bool(mass[1]),int(mass[2]),mass[3])

    def the_button_setPersonUser_was_clicked(self):
        mass = self.input_setPersonUser.text().split()
        ob = Smart()
        a = ob.setPersonUser(mass[0],mass[1],int(mass[2]),mass[3])

    def the_button_accounts_was_clicked(self):
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
