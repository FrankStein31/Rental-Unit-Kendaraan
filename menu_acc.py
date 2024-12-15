from PyQt5 import QtCore, QtGui, QtWidgets
import accpembayaran_motor as mtr
import accpembayaran_mobil as mbl
import accpembayaran_elf as elf
import menu_admin as mad

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 140, 531, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_mobil = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mobil.setFont(font)
        self.pushButton_mobil.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton_mobil.setObjectName("pushButton_mobil")
        self.gridLayout.addWidget(self.pushButton_mobil, 1, 0, 1, 1)
        self.pushButton_elf = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_elf.setFont(font)
        self.pushButton_elf.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton_elf.setObjectName("pushButton_elf")
        self.gridLayout.addWidget(self.pushButton_elf, 2, 0, 1, 1)
        self.pushButton_motor = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_motor.setFont(font)
        self.pushButton_motor.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton_motor.setObjectName("pushButton_motor")
        self.gridLayout.addWidget(self.pushButton_motor, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 50, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushButton_keluar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_keluar.setGeometry(QtCore.QRect(350, 420, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
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

        self.pushButton_motor.clicked.connect(self.AccMtr)
        self.pushButton_motor.clicked.connect(MainWindow.close)
        self.pushButton_mobil.clicked.connect(self.AccMbl)
        self.pushButton_mobil.clicked.connect(MainWindow.close)
        self.pushButton_elf.clicked.connect(self.AccElf)
        self.pushButton_elf.clicked.connect(MainWindow.close)
        self.pushButton_keluar.clicked.connect(self.Kembali)
        self.pushButton_keluar.clicked.connect(MainWindow.close)

    def AccMtr(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mtr.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def AccMbl(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mbl.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def AccElf(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = elf.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Kembali(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mad.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_mobil.setText(_translate("MainWindow", "Mobil"))
        self.pushButton_elf.setText(_translate("MainWindow", "Elf"))
        self.pushButton_motor.setText(_translate("MainWindow", "Motor"))
        self.label.setText(_translate("MainWindow", "ACC PEMBAYARAN KENDARAAN"))
        self.pushButton_keluar.setText(_translate("MainWindow", "Kembali"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
