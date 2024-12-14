import kelolaunit_admin as ku
import riwayat_admin as riw
import menu_acc as acc
import login as log
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 30, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton_kelolaunit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kelolaunit.setGeometry(QtCore.QRect(180, 220, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_kelolaunit.setFont(font)
        self.pushButton_kelolaunit.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_kelolaunit.setObjectName("pushButton_kelolaunit")
        self.pushButton_riwayat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_riwayat.setGeometry(QtCore.QRect(180, 280, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_riwayat.setFont(font)
        self.pushButton_riwayat.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_riwayat.setObjectName("pushButton_riwayat")

        # Menambahkan tombol Acc Pembayaran
        self.pushButton_acc_pembayaran = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_acc_pembayaran.setGeometry(QtCore.QRect(180, 340, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_acc_pembayaran.setFont(font)
        self.pushButton_acc_pembayaran.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_acc_pembayaran.setObjectName("pushButton_acc_pembayaran")

        self.pushButton_keluar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_keluar.setGeometry(QtCore.QRect(680, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_keluar.setFont(font)
        self.pushButton_keluar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 17, 30);\n"
"")
        self.pushButton_keluar.setObjectName("pushButton_keluar")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_kelolaunit.clicked.connect(self.KelolaUnit)
        self.pushButton_kelolaunit.clicked.connect(MainWindow.close)

        self.pushButton_riwayat.clicked.connect(self.Riwayat)
        self.pushButton_riwayat.clicked.connect(MainWindow.close)

        self.pushButton_keluar.clicked.connect(self.Logout)
        self.pushButton_keluar.clicked.connect(MainWindow.close)

        # Menambahkan aksi pada tombol "Acc Pembayaran"
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
