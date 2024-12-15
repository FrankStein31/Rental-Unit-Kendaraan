# menu_admin.py
import kelolaunit_admin as ku
import riwayat_admin as riw
import menu_acc as acc
import login as log
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        self.label_4 = QtWidgets.QLabel("Selamat Datang Admin !")
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        layout.addWidget(self.label_4)
        
        # Menu Label
        self.label = QtWidgets.QLabel("MENU")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        layout.addWidget(self.label)
        
        # Buttons
        self.pushButton_kelolaunit = QtWidgets.QPushButton("Kelola Unit")
        self.pushButton_kelolaunit.setObjectName("pushButton_kelolaunit")
        layout.addWidget(self.pushButton_kelolaunit)
        
        self.pushButton_riwayat = QtWidgets.QPushButton("Riwayat")
        self.pushButton_riwayat.setObjectName("pushButton_riwayat")
        layout.addWidget(self.pushButton_riwayat)
        
        self.pushButton_acc_pembayaran = QtWidgets.QPushButton("Acc Pembayaran")
        self.pushButton_acc_pembayaran.setObjectName("pushButton_acc_pembayaran")
        layout.addWidget(self.pushButton_acc_pembayaran)
        
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
        self.pushButton_kelolaunit.clicked.connect(self.KelolaUnit)
        self.pushButton_kelolaunit.clicked.connect(MainWindow.close)

        self.pushButton_riwayat.clicked.connect(self.Riwayat)
        self.pushButton_riwayat.clicked.connect(MainWindow.close)

        self.pushButton_keluar.clicked.connect(self.Logout)
        self.pushButton_keluar.clicked.connect(MainWindow.close)

        self.pushButton_acc_pembayaran.clicked.connect(self.Acc)
        self.pushButton_acc_pembayaran.clicked.connect(MainWindow.close)

    def KelolaUnit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ku.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Riwayat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = riw.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Acc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = acc.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def Logout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = log.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def AccPembayaran(self):
        # Fungsi ini akan dipanggil saat tombol Acc Pembayaran diklik
        print("Acc Pembayaran ditekan")
        # Tambahkan aksi yang sesuai di sini

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Selamat Datang Admin !"))
        self.label.setText(_translate("MainWindow", "MENU"))
        self.pushButton_kelolaunit.setText(_translate("MainWindow", "1. Kelola Unit"))
        self.pushButton_riwayat.setText(_translate("MainWindow", "2. Riwayat"))
        self.pushButton_acc_pembayaran.setText(_translate("MainWindow", "3. Acc Pembayaran"))  # Menambahkan label tombol
        self.pushButton_keluar.setText(_translate("MainWindow", "Logout"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
