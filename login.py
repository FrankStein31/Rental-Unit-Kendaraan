# -*- coding: utf-8 -*-

from user import User
import registrasi as reg
import menu_admin as mad
import menu_penyewa as mp
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(41, 128, 185, 255), 
                    stop:1 rgba(109, 213, 250, 255));
            }
            QLabel {
                color: white;
                font-weight: bold;
            }
            QLineEdit {
                padding: 8px;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 0.2);
                color: white;
                border: 1px solid rgba(255, 255, 255, 0.5);
            }
            QLineEdit:focus {
                border: 2px solid white;
            }
            QPushButton {
                background-color: rgba(255, 255, 255, 0.2);
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.1);
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main layout
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(50, 50, 50, 50)
        
        # Logo placeholder
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setText("RENTAL JAYA")
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.logo_label.setFont(font)
        main_layout.addWidget(self.logo_label)
        main_layout.addSpacing(50)
        
        # Login form layout
        form_layout = QtWidgets.QVBoxLayout()
        form_layout.setSpacing(15)
        
        # Username
        username_layout = QtWidgets.QHBoxLayout()
        username_label = QtWidgets.QLabel("Username")
        username_label.setFont(QtGui.QFont("Arial", 12))
        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setPlaceholderText("Masukkan username")
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        form_layout.addLayout(username_layout)
        
        # Password
        password_layout = QtWidgets.QHBoxLayout()
        password_label = QtWidgets.QLabel("Password")
        password_label.setFont(QtGui.QFont("Arial", 12))
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setPlaceholderText("Masukkan password")
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        form_layout.addLayout(password_layout)
        
        main_layout.addLayout(form_layout)
        main_layout.addSpacing(30)
        
        # Button layout
        button_layout = QtWidgets.QHBoxLayout()
        self.login_button = QtWidgets.QPushButton("LOGIN")
        self.register_button = QtWidgets.QPushButton("REGISTRASI")
        self.exit_button = QtWidgets.QPushButton("KELUAR")
        
        button_layout.addWidget(self.exit_button)
        button_layout.addStretch()
        button_layout.addWidget(self.register_button)
        button_layout.addWidget(self.login_button)
        
        main_layout.addLayout(button_layout)
        main_layout.addStretch()
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to their respective methods
        self.login_button.clicked.connect(self.login)
        self.login_button.clicked.connect(MainWindow.close)
        self.register_button.clicked.connect(self.openRegistrasi)
        self.register_button.clicked.connect(MainWindow.close)
        self.exit_button.clicked.connect(MainWindow.close)

    # Rest of the methods remain the same as the original code
    def openMenuPenyewa(self, user_id):
        print("Ini id user dari login opern menu penyewa ", user_id)
        self.window = QtWidgets.QMainWindow()
        self.ui = mp.Ui_MainWindow()
        self.ui.setupUi(self.window, user_id)
        self.window.show()

    def openMenuAdmin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mad.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def login(self):
        usernamelogin = self.username_input.text()
        passwordlogin = self.password_input.text()
        
        if usernamelogin == "" or passwordlogin == "":
            self.notif("Error", "Username dan password harus diisi!")
            self.username_input.clear()
            self.password_input.clear()
        else:
            level_login, user_id = User.login(usernamelogin, passwordlogin)
            if level_login == "admin":
                self.openMenuAdmin()
                QtWidgets.QApplication.activeWindow().close()
            elif level_login == "penyewa":
                self.openMenuPenyewa(user_id)
                QtWidgets.QApplication.activeWindow().close()
            else:
                self.notif("Error", "Username atau password salah!")
                self.username_input.clear()
                self.password_input.clear()
                self.username_input.setFocus()

    def notif(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()

    def openRegistrasi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = reg.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login - Rental Jaya"))
        self.exit_button.setText(_translate("MainWindow", "KELUAR"))
        self.login_button.setText(_translate("MainWindow", "LOGIN"))
        self.register_button.setText(_translate("MainWindow", "REGISTRASI"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())