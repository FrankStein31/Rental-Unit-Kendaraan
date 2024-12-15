from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import menu_penyewa as mep

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_id=None):

        self.user_id = user_id

        print("Ini id user dari HALAMAN RIWAYAT PENYEWA", user_id)


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 100, 701, 291))
        self.tableWidget.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)  # Update the column count
        self.tableWidget.setRowCount(0)
        
        # Set column headers
        self.tableWidget.setHorizontalHeaderLabels([
            "ID Transaksi", "ID Kendaraan", "Harga Sewa", "Tgl Pinjam", "Tgl Kembali", "Driver"
        ])

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 490, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 17, 30);")
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 400, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        
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

        self.pushButton_2.clicked.connect(self.KembaliMenu)
        self.pushButton_2.clicked.connect(MainWindow.close)

        # Connect refresh button to fetch data
        self.pushButton_3.clicked.connect(self.refreshData)

    def KembaliMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mep.Ui_MainWindow()
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "RIWAYAT RENTAL"))
        self.pushButton_2.setText(_translate("MainWindow", "Kembali"))
        self.pushButton_3.setText(_translate("MainWindow", "Refresh"))

    def refreshData(self):
        try:
            # Connect to MySQL Database
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="uas"
            )
            cursor = db_connection.cursor(dictionary=True)

            # Clear the table before refreshing
            self.tableWidget.setRowCount(0)

            # Gabungkan data dari semua tabel rental
            cursor.execute("""
                SELECT 
                    'Mobil' AS jenis_kendaraan,
                    p.id_transaksi, 
                    m.jenis_mbl AS merk_unit, 
                    p.harga_sewa_mobil AS harga_sewa, 
                    p.tanggal_pinjam, 
                    p.tanggal_kembali, 
                    p.driver, 
                    COALESCE(pmobil.status, 'Pending') AS status_pembayaran
                FROM pinjam p
                LEFT JOIN pembayaran pmobil ON p.id_transaksi = pmobil.id_transaksi
                LEFT JOIN mobil m ON p.id_mobil = m.id_mbl
                WHERE p.id_user = %s

                UNION

                SELECT 
                    'Motor' AS jenis_kendaraan,
                    pm.id_transaksi_motor AS id_transaksi, 
                    mo.jenis_mtr AS merk_unit, 
                    pm.harga_sewa_motor AS harga_sewa, 
                    pm.tanggal_pinjam, 
                    pm.tanggal_kembali, 
                    pm.driver, 
                    COALESCE(pmotor.status, 'Pending') AS status_pembayaran
                FROM pinjam_motor pm
                LEFT JOIN pembayaran_motor pmotor ON pm.id_transaksi_motor = pmotor.id_transaksi_motor
                LEFT JOIN motor mo ON pm.id_motor = mo.id_mtr
                WHERE pm.id_user = %s

                UNION

                SELECT 
                    'Elf' AS jenis_kendaraan,
                    pe.id_transaksi_elf AS id_transaksi, 
                    e.jenis_elf AS merk_unit, 
                    pe.harga_sewa_elf AS harga_sewa, 
                    pe.tanggal_pinjam, 
                    pe.tanggal_kembali, 
                    pe.driver, 
                    COALESCE(pelf.status, 'Pending') AS status_pembayaran
                FROM pinjam_elf pe
                LEFT JOIN pembayaran_elf pelf ON pe.id_transaksi_elf = pelf.id_transaksi_elf
                LEFT JOIN elf e ON pe.id_elf = e.id_elf
                WHERE pe.id_user = %s
                ORDER BY tanggal_pinjam DESC
            """, (self.user_id, self.user_id, self.user_id))

            rows = cursor.fetchall()

            if not rows:
                QtWidgets.QMessageBox.information(None, "Informasi", "Tidak ada riwayat rental.")
                return

            # Set column count and headers
            self.tableWidget.setColumnCount(8)
            headers = [
                "Jenis Kendaraan", "ID Transaksi", "Merk Unit", 
                "Harga Sewa", "Tanggal Pinjam", "Tanggal Kembali", 
                "Driver", "Status Pembayaran"
            ]
            self.tableWidget.setHorizontalHeaderLabels(headers)

            # Atur lebar kolom agar sesuai
            for i in range(len(headers)):
                self.tableWidget.setColumnWidth(i, 100)

            # Populate the table
            for row in rows:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                
                # Tambahkan data ke baris
                for col, (key, value) in enumerate(row.items()):
                    item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "-")
                    
                    # Beri warna berbeda untuk status pembayaran
                    if key == 'status_pembayaran':
                        if value == 'Lunas':
                            item.setBackground(QtGui.QColor(200, 255, 200))  # Hijau muda
                        elif value == 'Belum Lunas':
                            item.setBackground(QtGui.QColor(255, 200, 200))  # Merah muda
                    
                    self.tableWidget.setItem(rowPosition, col, item)

            # Resize rows agar konten terlihat penuh
            self.tableWidget.resizeRowsToContents()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Error Database", f"Terjadi kesalahan: {err}")
        
        finally:
            # Pastikan koneksi ditutup
            if 'cursor' in locals():
                cursor.close()
            if 'db_connection' in locals():
                db_connection.close()

if __name__ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())