from PyQt5 import QtCore, QtGui, QtWidgets
import kelolaunit_penyewa as kup
import riwayat_penyewa as rep
import menu_struk as st
import login as log

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_id=None):
        self.user_id = user_id
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(36, 160, 237, 255), 
                    stop:1 rgba(90, 200, 250, 255));
            }
            QPushButton {
                background-color: white;
                color: #1E88E5;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
                border: 2px solid #1E88E5;
            }
            QPushButton:hover {
                background-color: #E3F2FD;
            }
            QPushButton:pressed {
                background-color: #BBDEFB;
            }
            QLabel {
                color: white;
                font-weight: bold;
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main Layout
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(20)
        
        # Welcome Label
        self.label_2 = QtWidgets.QLabel("Selamat Datang")
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        layout.addWidget(self.label_2)
        
        # Select Menu Label
        self.label = QtWidgets.QLabel("Pilih Menu")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        layout.addWidget(self.label)
        
        # Buttons
        self.pushButton = QtWidgets.QPushButton("Pilih Unit")
        self.pushButton.setObjectName("pushButton")
        layout.addWidget(self.pushButton)
        
        self.pushButton_2 = QtWidgets.QPushButton("Lihat Riwayat")
        self.pushButton_2.setObjectName("pushButton_2")
        layout.addWidget(self.pushButton_2)
        
        self.pushButton_3 = QtWidgets.QPushButton("Pembayaran")
        self.pushButton_3.setObjectName("pushButton_3")
        layout.addWidget(self.pushButton_3)
        
        # Logout Button
        logout_layout = QtWidgets.QHBoxLayout()
        logout_layout.addStretch()
        self.pushButton_keluar = QtWidgets.QPushButton("Logout")
        self.pushButton_keluar.setObjectName("pushButton_keluar")
        self.pushButton_keluar.setStyleSheet("""
            background-color: #D32F2F;
            color: white;
            border-radius: 5px;
            padding: 5px 10px;
        """)
        logout_layout.addWidget(self.pushButton_keluar)
        layout.addLayout(logout_layout)
        
        MainWindow.setCentralWidget(self.centralwidget)

        # Connect signals
        self.pushButton.clicked.connect(self.Unit)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.Riwayat)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_keluar.clicked.connect(self.Logout)
        self.pushButton_keluar.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.Struk)
        self.pushButton_3.clicked.connect(MainWindow.close)

    def Unit(self):
        print("Ini id user dari menu penyewa unit", self.user_id)
        self.window = QtWidgets.QMainWindow()
        self.ui = kup.Ui_MainWindow()
        # self.ui.setupUi(self.window)
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()

    def Riwayat(self):
        print("Ini id user dari menu penyewa riwayat", self.user_id)
        self.window = QtWidgets.QMainWindow()
        self.ui = rep.Ui_MainWindow()
        # self.ui.setupUi(self.window)
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()

    def Struk(self):
        print("Ini id user dari menu penyewa struk", self.user_id)
        self.window = QtWidgets.QMainWindow()
        self.ui = st.Ui_MainWindow()
        # self.ui.setupUi(self.window)
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()

    def Logout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = log.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pilih Menu"))
        self.pushButton.setText(_translate("MainWindow", "1. Pilih Unit"))
        self.pushButton_2.setText(_translate("MainWindow", "2. Lihat Riwayat Anda"))
        self.pushButton_3.setText(_translate("MainWindow", "3. Pembayaran"))
        self.label_2.setText(_translate("MainWindow", "Selamat Datang"))
        self.pushButton_keluar.setText(_translate("MainWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
