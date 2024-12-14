# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accpembayaran.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import menu_acc as acc
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 170, 281, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 280, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 210, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 70, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 240, 281, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"background-color: rgb(255, 202, 111);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 350, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(620, 120, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(590, 150, 191, 401))
        self.listView.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.listView.setObjectName("listView")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 90, 131, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 420, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 380, 281, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"background-color: rgb(255, 202, 111);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(50, 450, 281, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"background-color: rgb(255, 202, 111);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 150, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 310, 281, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"background-color: rgb(255, 202, 111);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(430, 240, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 510, 93, 28))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 17, 30);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 90, 91, 41))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 17, 30);")
        self.pushButton_2.setObjectName("pushButton")
        self.kembali = QtWidgets.QPushButton(self.centralwidget)
        self.kembali.setGeometry(QtCore.QRect(50, 20, 93, 28))
        self.kembali.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 17, 30);")
        self.kembali.setObjectName("kembali")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(440, 200, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(50, 480, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 510, 281, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.comboBox.setObjectName("comboBox")
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
        self.pushButton.clicked.connect(self.update_status)
        self.pushButton_2.clicked.connect(self.search_data)

        self.kembali.clicked.connect(self.Acc)
        self.kembali.clicked.connect(MainWindow.close)



    def Acc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = acc.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()




    def search_data(self):
        try:
            # Mengambil ID motor dari lineEdit
            motor_id = self.lineEdit.text()

            # Membuka koneksi ke database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Ganti dengan password database MySQL Anda
                database="uas"
            )
            cursor = connection.cursor()

            # Query untuk mencari data berdasarkan ID motor (id_mtr)
            query = """
            SELECT mobil.jenis_mbl, mobil.type_mbl, mobil.tahun_mbl, mobil.warna_mbl, mobil.harga_sewa_mbl, pembayaran.status
            FROM mobil
            JOIN pembayaran ON mobil.id_mbl = pembayaran.id_transaksi
            WHERE mobil.id_mbl = %s

            """
            cursor.execute(query, (motor_id,))
            result = cursor.fetchone()

            if result:
                # Menampilkan data ke user dan mengisi ComboBox
                self.lineEdit_2.setText(result[0])  # jenis_mtr
                self.lineEdit_3.setText(result[1])  # type_mtr
                self.lineEdit_4.setText(str(result[2]))  # tahun_mtr
                self.lineEdit_5.setText(result[3])  # warna_mtr
                self.lineEdit_6.setText(str(result[4]))  # harga_sewa_mtr
                
                # Mengisi ComboBox dengan status saat ini dan opsi lain
                self.comboBox.clear()
                self.comboBox.addItem(result[5])  # Menambahkan status saat ini
                
                # Ambil semua pilihan status dari kolom enum
                cursor.execute("SHOW COLUMNS FROM pembayaran LIKE 'status'")
                enum_values = cursor.fetchone()[1]  # Kolom 1 adalah definisi enum

                # Extract pilihan enum dari definisi
                enum_choices = enum_values.split('(')[1].split(')')[0].replace("'", "").split(",")
                
                # Menambahkan pilihan enum ke ComboBox
                self.comboBox.addItems(enum_choices)  # Menambahkan opsi lain

            else:
                QMessageBox.warning(None, "Tidak Ditemukan", "Data tidak ditemukan dalam database.")

        except mysql.connector.Error as e:
            QMessageBox.critical(None, "Error", f"Terjadi kesalahan: {str(e)}")

        finally:
            if connection:
                connection.close()


    def update_status(self):
        try:
            # Mengambil ID motor dari lineEdit
            motor_id = self.lineEdit.text()

            # Mengambil status baru dari ComboBox
            new_status = self.comboBox.currentText()

            # Membuka koneksi ke database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Ganti dengan password database MySQL Anda
                database="uas"
            )
            cursor = connection.cursor()

            # Update status di database
            update_query = """
            UPDATE pembayaran
            SET status = %s
            WHERE id_transaksi = %s
            """
            cursor.execute(update_query, (new_status, motor_id))
            connection.commit()

            QMessageBox.information(None, "Sukses", "Status berhasil diperbarui.")

        except mysql.connector.Error as e:
            QMessageBox.critical(None, "Error", f"Terjadi kesalahan: {str(e)}")

        finally:
            if connection:
                connection.close()






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Pembayaran"))
        self.label_8.setText(_translate("MainWindow", "Tahun"))
        self.label_7.setText(_translate("MainWindow", "Type :"))
        self.label_5.setText(_translate("MainWindow", "Kode Sewa"))
        self.label_9.setText(_translate("MainWindow", "Warna"))
        self.label_6.setText(_translate("MainWindow", "Kode Sewa"))
        self.label_12.setText(_translate("MainWindow", "Harga"))
        self.label_10.setText(_translate("MainWindow", "Jenis"))
        self.label_13.setText(_translate("MainWindow", "image"))
        self.pushButton.setText(_translate("MainWindow", "ACC"))
        self.pushButton_2.setText(_translate("MainWindow", "Cari"))
        self.label_14.setText(_translate("MainWindow", "Unit"))
        self.label_15.setText(_translate("MainWindow", "ACC"))
        self.kembali.setText(_translate("Mainwindow","KEMBALI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
