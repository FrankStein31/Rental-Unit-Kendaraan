# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from user import User
import login as log

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
        
        # Title
        title_label = QtWidgets.QLabel("REGISTRASI AKUN")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        title_label.setFont(font)
        main_layout.addWidget(title_label)
        main_layout.addSpacing(30)
        
        # Subtitle
        subtitle_label = QtWidgets.QLabel("Silahkan lengkapi data anda")
        subtitle_label.setAlignment(QtCore.Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: rgba(255,255,255,0.7);")
        main_layout.addWidget(subtitle_label)
        main_layout.addSpacing(30)
        
        # Form Layout
        form_layout = QtWidgets.QFormLayout()
        form_layout.setSpacing(15)
        form_layout.setLabelAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        # Input Fields
        self.lineEdit_nama = QtWidgets.QLineEdit()
        self.lineEdit_nama.setPlaceholderText("Masukkan nama lengkap")
        form_layout.addRow("Nama:", self.lineEdit_nama)
        
        self.lineEdit_username_3 = QtWidgets.QLineEdit()
        self.lineEdit_username_3.setPlaceholderText("Masukkan alamat")
        form_layout.addRow("Alamat:", self.lineEdit_username_3)
        
        self.lineEdit_nohp = QtWidgets.QLineEdit()
        self.lineEdit_nohp.setPlaceholderText("Masukkan nomor HP")
        form_layout.addRow("No HP:", self.lineEdit_nohp)
        
        self.lineEdit_username = QtWidgets.QLineEdit()
        self.lineEdit_username.setPlaceholderText("Pilih username")
        form_layout.addRow("Username:", self.lineEdit_username)
        
        self.lineEdit_password = QtWidgets.QLineEdit()
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText("Buat password")
        form_layout.addRow("Password:", self.lineEdit_password)
        
        main_layout.addLayout(form_layout)
        main_layout.addSpacing(30)
        
        # Button Layout
        button_layout = QtWidgets.QHBoxLayout()
        self.pushButton_kembali = QtWidgets.QPushButton("KEMBALI")
        self.pushButton_regist = QtWidgets.QPushButton("REGIST")
        
        button_layout.addWidget(self.pushButton_kembali)
        button_layout.addStretch()
        button_layout.addWidget(self.pushButton_regist)
        
        main_layout.addLayout(button_layout)
        main_layout.addStretch()
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons
        self.pushButton_regist.clicked.connect(self.BuatAkun)
        self.pushButton_kembali.clicked.connect(self.Kembali)
        self.pushButton_kembali.clicked.connect(MainWindow.close)

    def Kembali(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = log.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def BuatAkun(self):
        nama = self.lineEdit_nama.text()
        alamat = self.lineEdit_username_3.text()
        no_hp = self.lineEdit_nohp.text()
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        level = "penyewa"

        # Cek apakah ada field yang kosong
        if not (nama and alamat and no_hp and username and password):
            QtWidgets.QMessageBox.warning(None, "Peringatan", "Semua field harus diisi!")
            return

        # Cek apakah no HP hanya berisi angka
        if not no_hp.isdigit():
            QtWidgets.QMessageBox.warning(None, "Peringatan", "Nomor HP harus berupa angka!")
            return

        # Jika semua validasi lulus, lakukan insert data
        User.insert_data(nama, alamat, no_hp, username, password, level)

        # Tampilkan notifikasi sukses
        QtWidgets.QMessageBox.information(None, "Sukses", "Akun berhasil dibuat!")

        from login import Ui_MainWindow as log
        
        self.window = QtWidgets.QMainWindow()
        self.ui = log()
        self.ui.setupUi(self.window)
        QtWidgets.QApplication.activeWindow().close()
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registrasi - Rental Jaya"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())