from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import mysql.connector
import os
import menu_admin as mad
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 679)
        MainWindow.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kembali.setGeometry(QtCore.QRect(338, 540, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_kembali.setFont(font)
        self.pushButton_kembali.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 17, 30);")
        self.pushButton_kembali.setObjectName("pushButton_kembali")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(248, 70, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(48, 150, 701, 291))
        self.tableWidget.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(640, 460, 101, 31))
        self.pushButton_refresh.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the refresh button to the function
        self.pushButton_refresh.clicked.connect(self.lihat_data_elf)

    def KembaliMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mad.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def lihat_data_elf(self):
        # Clear the existing data in the table
        self.tableWidget.setRowCount(0)
        
        try:
            # Koneksi ke database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="uas"  # Ganti nama database sesuai kebutuhan
            )
            mycursor = conn.cursor()

            # Query SQL untuk mengambil semua data dari tabel elf
            sql = "SELECT * FROM elf"
            mycursor.execute(sql)

            # Ambil semua hasil query
            results = mycursor.fetchall()

            # Menambahkan data ke dalam tableWidget
            for row_num, row_data in enumerate(results):
                self.tableWidget.insertRow(row_num)  # Menambahkan baris baru
                for col_num, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_num, col_num, item)

            # Tutup koneksi
            mycursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Error", f"Terjadi kesalahan: {err}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_kembali.setText(_translate("MainWindow", "Kembali"))
        self.label_4.setText(_translate("MainWindow", "LIHAT ELF"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Kendaraan"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Jenis"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipe"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Keluaran Tahun"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Warna"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Stok"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Harga sewa"))
        self.pushButton_refresh.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_kembali.clicked.connect(self.KembaliMenu)
        self.pushButton_kembali.clicked.connect(MainWindow.close)
        self.lihat_data_elf()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
