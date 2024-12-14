from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from decimal import Decimal
from PyQt5.QtCore import QDate
import kelolaunit_penyewa as kel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_id=None):

        self.user_id = user_id
        print("Ini id user dari HALAMAN PEMBAYARAN ELF", user_id)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 568)
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 0, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 240, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 290, 321, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 340, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 390, 321, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_bayar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bayar.setGeometry(QtCore.QRect(280, 460, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_bayar.setFont(font)
        self.pushButton_bayar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(6, 131, 35);")
        self.pushButton_bayar.setObjectName("pushButton_bayar")
        self.dateEdit_kembali = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_kembali.setGeometry(QtCore.QRect(50, 190, 321, 41))
        self.dateEdit_kembali.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.dateEdit_kembali.setObjectName("dateEdit_kembali")
        self.datepinjam = QtWidgets.QLabel(self.centralwidget)
        self.datepinjam.setGeometry(QtCore.QRect(400, 190, 321, 41))
        self.datepinjam.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.datepinjam.setObjectName("dateEdit_kembali")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 340, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 390, 321, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_cari = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cari.setGeometry(QtCore.QRect(270, 90, 101, 41))
        self.pushButton_cari.setObjectName("pushButton_cari")
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(50, 90, 161, 41))
        self.lineEdit_id.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 60, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.pushButton_kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kembali.setGeometry(QtCore.QRect(50, 460, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_kembali.setFont(font)
        self.pushButton_kembali.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 17, 30);")
        self.pushButton_kembali.setObjectName("pushButton_kembali")
        self.pushButton_hitung = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hitung.setGeometry(QtCore.QRect(380, 290, 101, 41))
        self.pushButton_hitung.setObjectName("pushButton_hitung")
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
        self.pushButton_cari.clicked.connect(self.cari_data_peminjaman)
        self.pushButton_hitung.clicked.connect(self.hitung_denda)
        self.pushButton_bayar.clicked.connect(self.bayar_transaksi)
        self.pushButton_kembali.clicked.connect(self.KelolaUnit)
        self.pushButton_kembali.clicked.connect(MainWindow.close)


    def KelolaUnit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = kel.Ui_MainWindow()
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()

    def cari_data_peminjaman(self):
        try:
            # Ambil nilai id_transaksi dari QLineEdit
            id_transaksi = self.lineEdit_id.text()  
            
            # Pastikan id_transaksi valid
            if not id_transaksi or not id_transaksi.isdigit():
                print("ID Transaksi tidak valid!")
                return  # Hentikan jika ID tidak valid

            id_transaksi = int(id_transaksi)  # Konversi ke integer jika valid
            print(f"ID Transaksi yang dicari: {id_transaksi}")  # Debugging

            # Connect ke database MySQL
            conn = mysql.connector.connect(
                host='localhost',  # Host MySQL
                user='root',  # Username MySQL
                password='',  # Password MySQL
                database='uas'  # Nama database
            )
            cursor = conn.cursor()

            # Query untuk mencari tanggal pinjam berdasarkan id_transaksi
            query_pinjam = """
            SELECT tanggal_pinjam 
            FROM pinjam_elf
            WHERE id_transaksi_elf = %s
            """
            cursor.execute(query_pinjam, (id_transaksi,))
            pinjam_result = cursor.fetchone()

            if pinjam_result:
                # Ambil tanggal pinjam dari hasil query
                tanggal_pinjam = pinjam_result[0]

                # Tampilkan hasil data peminjaman pada QLabel
                print(f"{tanggal_pinjam}")

                # Update QLabel dengan tanggal pinjam
                self.datepinjam.setText(f" {tanggal_pinjam}")
            else:
                print("Data peminjaman tidak ditemukan.")
                self.datepinjam.setText("Data peminjaman tidak ditemukan.")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print(f"Database error: {err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def hitung_denda(self):
        try:
            # Ambil nilai dari QLineEdit dan QDateEdit
            id_transaksi = self.lineEdit_id.text()
            id_user = self.user_id
            tanggal_dikembalikan = self.dateEdit_kembali.date()

            # Validasi ID transaksi
            if not id_transaksi or not id_transaksi.isdigit():
                print("ID Transaksi tidak valid!")
                return

            id_transaksi = int(id_transaksi)
            print(f"ID Transaksi: {id_transaksi}")
            print(f"Tanggal Dikembalikan: {tanggal_dikembalikan.toString('yyyy-MM-dd')}")

            # Connect ke database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='uas'
            )
            cursor = conn.cursor()

            # Ambil tanggal pinjam dan harga sewa dari tabel pinjam
            query_pinjam = """
            SELECT p.tanggal_pinjam, m.harga_sewa_elf
            FROM pinjam_elf p
            JOIN elf m ON p.id_elf = m.id_elf
            WHERE p.id_transaksi_elf = %s
            """
            cursor.execute(query_pinjam, (id_transaksi,))
            pinjam_result = cursor.fetchone()

            if pinjam_result:
                tanggal_pinjam = pinjam_result[0]
                harga_sewa = pinjam_result[1]

                # Hitung selisih hari antara tanggal pinjam dan tanggal dikembalikan
                tanggal_pinjam_qdate = QDate.fromString(tanggal_pinjam.strftime('%Y-%m-%d'), 'yyyy-MM-dd')
                selisih_hari = tanggal_pinjam_qdate.daysTo(tanggal_dikembalikan)

                # Tentukan denda (misalnya 5000 IDR per hari keterlambatan)
                denda_per_hari = 5000
                if selisih_hari > 0:
                    denda = selisih_hari * denda_per_hari
                else:
                    denda = 0

                # Hitung total pembayaran
                total_pembayaran = harga_sewa + denda

                print(f"Tanggal Pinjam: {tanggal_pinjam}")
                print(f"Harga Sewa: {harga_sewa}")
                print(f"Selisih Hari: {selisih_hari}")
                print(f"Denda: {denda}")
                print(f"Total Pembayaran: {total_pembayaran}")

                # Simpan hasil ke tabel pembayaran menggunakan INSERT
                query_insert = """
                INSERT INTO pembayaran_elf (id_transaksi_elf, id_user, tanggal_dikembalikan, denda, total_pembayaran)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query_insert, (id_transaksi, id_user, tanggal_dikembalikan.toString('yyyy-MM-dd'), denda, total_pembayaran))
                conn.commit()

                # Tampilkan hasil ke QLabel
                self.lineEdit_2.setText(f"Denda: {denda}")
                self.lineEdit.setText(f"Total Pembayaran: {total_pembayaran}")

                print("Denda dan total pembayaran berhasil dihitung dan disimpan.")
            else:
                print("Data transaksi tidak ditemukan.")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print(f"Database error: {err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")






    def bayar_transaksi(self):
        try:
            # Ambil nilai dari input pengguna
            id_transaksi_elf = self.lineEdit_id.text().strip()  # ID transaksi dari QLineEdit
            jumlah_dibayarkan_str = self.lineEdit_3.text().strip()  # Jumlah uang yang dibayarkan

            if not id_transaksi_elf:
                print("ID Transaksi tidak boleh kosong!")
                return

            if not jumlah_dibayarkan_str:
                print("Jumlah dibayarkan tidak boleh kosong!")
                return

            # Validasi input jumlah dibayarkan
            try:
                jumlah_dibayarkan = Decimal(jumlah_dibayarkan_str)  # Konversi ke Decimal
            except ValueError:
                print("Invalid input: Pastikan jumlah dibayarkan adalah angka valid.")
                return

            if jumlah_dibayarkan <= 0:
                print("Jumlah dibayarkan harus lebih dari 0.")
                return

            print(f"ID Transaksi: {id_transaksi_elf}")
            print(f"Jumlah Dibayarkan: {jumlah_dibayarkan}")

            # Connect ke MySQL database
            conn = mysql.connector.connect(
                host='localhost',  # Host MySQL
                user='root',  # Username MySQL
                password='',  # Password MySQL
                database='uas'  # Nama database
            )
            cursor = conn.cursor()

            # Ambil total pembayaran dari tabel pembayaran berdasarkan id_transaksi
            query_pembayaran = """
            SELECT total_pembayaran, dibayarkan
            FROM pembayaran_elf
            WHERE id_transaksi_elf = %s
            """
            cursor.execute(query_pembayaran, (id_transaksi_elf,))
            pembayaran_result = cursor.fetchone()

            if pembayaran_result:
                total_pembayaran = Decimal(pembayaran_result[0])  # Konversi ke Decimal
                sebelumnya_dibayarkan = Decimal(pembayaran_result[1] or 0)  # Default ke 0 jika None, dan konversi ke Decimal
                print(f"Total Pembayaran: {total_pembayaran}")
                print(f"Sebelumnya Dibayarkan: {sebelumnya_dibayarkan}")

                # Hitung total pembayaran setelah ditambahkan pembayaran baru
                total_dibayarkan = sebelumnya_dibayarkan + jumlah_dibayarkan
                sisa_pembayaran = total_pembayaran - total_dibayarkan

                if sisa_pembayaran <= 0:
                    status = "Lunas"  # Status menjadi "Lunas" jika tidak ada sisa pembayaran
                    print("Pembayaran Lunas!")
                else:
                    status = "Kurang"  # Status menjadi "Kurang" jika ada sisa pembayaran
                    print(f"Pembayaran Kurang: {sisa_pembayaran}")

                # Update data pembayaran di tabel pembayaran
                query_update = """
                UPDATE pembayaran_elf
                SET dibayarkan = %s, status = %s, sisa_pembayaran_amount = %s
                WHERE id_transaksi_elf = %s
                """
                cursor.execute(query_update, (total_dibayarkan, status, sisa_pembayaran, id_transaksi_elf))
                conn.commit()  # Simpan perubahan

                print("Data pembayaran berhasil disimpan!")
                from menu_penyewa import Ui_MainWindow as menu
                self.window = QtWidgets.QMainWindow()
                self.ui = menu()
                self.ui.setupUi(self.window, self.user_id)
                QtWidgets.QApplication.activeWindow().close()
                self.window.show()

            else:
                print("Data pembayaran tidak ditemukan!")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print(f"Database error: {err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Pembayaran"))
        self.label.setText(_translate("MainWindow", "Total Pembayaran"))
        self.label_2.setText(_translate("MainWindow", "Denda"))
        self.pushButton_bayar.setText(_translate("MainWindow", "BAYAR"))
        self.label_3.setText(_translate("MainWindow", "Tanggal dikembalikan"))
        self.label_5.setText(_translate("MainWindow", "Masukkan Uang"))
        self.pushButton_cari.setText(_translate("MainWindow", "cari"))
        self.label_8.setText(_translate("MainWindow", "ID Transaksi:"))
        self.pushButton_kembali.setText(_translate("MainWindow", "Kembali"))
        self.pushButton_hitung.setText(_translate("MainWindow", "Hitung"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
