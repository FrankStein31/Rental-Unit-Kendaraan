# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu1.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import kelolaunit_penyewa as kup
import riwayat_penyewa as rep
import menu_struk as st
import login as log

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 210, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 280, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 350, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 30, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_keluar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_keluar.setGeometry(QtCore.QRect(660, 10, 101, 31))
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

        self.pushButton.clicked.connect(self.Unit)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.Riwayat)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_keluar.clicked.connect(self.Logout)
        self.pushButton_keluar.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.Struk)
        self.pushButton_3.clicked.connect(MainWindow.close)

    def Unit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = kup.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Riwayat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = rep.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Struk(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = st.Ui_MainWindow()
        self.ui.setupUi(self.window)
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