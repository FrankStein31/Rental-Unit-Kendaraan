# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_kelola.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import elf_edit as E
import elf_hapus as H
import elf_tambah as T
import elf_lihat as L

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 150, 531, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_tambahkendaraan = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_tambahkendaraan.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton_tambahkendaraan.setObjectName("pushButton_tambahkendaraan")
        self.gridLayout.addWidget(self.pushButton_tambahkendaraan, 0, 0, 1, 1)
        self.pushButton_hapuskendaraan = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_hapuskendaraan.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton_hapuskendaraan.setObjectName("pushButton_hapuskendaraan")
        self.gridLayout.addWidget(self.pushButton_hapuskendaraan, 2, 0, 1, 1)
        self.pushButton_perbaruikendaraan = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_perbaruikendaraan.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton_perbaruikendaraan.setObjectName("pushButton_perbaruikendaraan")
        self.gridLayout.addWidget(self.pushButton_perbaruikendaraan, 1, 0, 1, 1)
        self.pushButton_reset = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_reset.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.gridLayout.addWidget(self.pushButton_reset, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 50, 421, 41))
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
        self.pushButton_perbaruikendaraan.clicked.connect(self.Edit)
        self.pushButton_perbaruikendaraan.clicked.connect(MainWindow.close)
        self.pushButton_hapuskendaraan.clicked.connect(self.Hapusl)
        self.pushButton_hapuskendaraan.clicked.connect(MainWindow.close)
        self.pushButton_tambahkendaraan.clicked.connect(self.Tambah)
        self.pushButton_tambahkendaraan.clicked.connect(MainWindow.close)
        self.pushButton_reset.clicked.connect(self.Lihat)
        self.pushButton_reset.clicked.connect(MainWindow.close)

    def Edit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = E.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Hapusl(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = H.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Tambah(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = T.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Lihat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = L.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_tambahkendaraan.setText(_translate("MainWindow", "Tambah Kendaraan"))
        self.pushButton_hapuskendaraan.setText(_translate("MainWindow", "Hapus Kendaraan"))
        self.pushButton_perbaruikendaraan.setText(_translate("MainWindow", "Perbarui Kendaraan"))
        self.pushButton_reset.setText(_translate("MainWindow", "Lihat Kendaraan"))
        self.label.setText(_translate("MainWindow", "KELOLA UNIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
