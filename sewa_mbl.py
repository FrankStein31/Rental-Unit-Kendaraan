# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import pilih_mobil as mbl
import pembayaran_mobil as bayar
import mysql.connector
from datetime import datetime, timedelta

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, mobil_id=None, user_id=None):
        self.user_id = user_id
        self.mobil_id = mobil_id
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 700)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: rgb(24, 121, 202);
            }
            QLabel {
                color: white;
                font-size: 12pt;
            }
            QLineEdit, QSpinBox, QDateEdit, QComboBox {
                background-color: rgb(255, 202, 111);
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton {
                color: white;
                font-size: 10pt;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton#pushButton_sewa {
                background-color: rgb(6, 131, 35);
            }
            QPushButton#pushButton_kembali {
                background-color: rgb(212, 17, 30);
            }
            QPushButton#pushButton_pinjam {
                background-color: rgb(6, 131, 35);
            }
            QPushButton#pushButton_3 {
                background-color: rgb(150, 150, 150);
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        # Title Label
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(200, 20, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("Pinjam mobil")
        
        # mobil ID Input
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(120, 100, 200, 30))
        self.label_id.setText("Masukkan ID mobil:")
        
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(120, 130, 561, 40))
        self.lineEdit_id.setPlaceholderText("Ketik ID mobil dan tekan Enter")
        
        # Add Enter key event to lineEdit_id
        self.lineEdit_id.returnPressed.connect(self.cari_mobil_auto)
        
        # Price Per Day
        self.label_harga = QtWidgets.QLabel(self.centralwidget)
        self.label_harga.setGeometry(QtCore.QRect(120, 200, 561, 30))
        self.label_harga.setText("Harga Sewa per Hari:")
        
        self.lineEdit_sewaperhari = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sewaperhari.setGeometry(QtCore.QRect(120, 230, 561, 40))
        self.lineEdit_sewaperhari.setReadOnly(True)
        
        # Quantity
        self.label_jumlah = QtWidgets.QLabel(self.centralwidget)
        self.label_jumlah.setGeometry(QtCore.QRect(120, 280, 561, 30))
        self.label_jumlah.setText("Jumlah mobil yang Disewa:")
        
        self.spinBox_jumlah = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_jumlah.setGeometry(QtCore.QRect(120, 310, 561, 40))
        self.spinBox_jumlah.setMinimum(1)
        
        # Driver Option
        self.label_driver = QtWidgets.QLabel(self.centralwidget)
        self.label_driver.setGeometry(QtCore.QRect(120, 370, 561, 30))
        self.label_driver.setText("Tambahan Driver:")
        
        self.comboBox_driver = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_driver.setGeometry(QtCore.QRect(120, 400, 561, 40))
        self.comboBox_driver.addItems(['tidak', 'ya'])
        
        # Rental Dates
        self.label_pinjam = QtWidgets.QLabel(self.centralwidget)
        self.label_pinjam.setGeometry(QtCore.QRect(120, 460, 561, 30))
        self.label_pinjam.setText("Tanggal Pinjam:")
        
        self.dateEdit_pinjam = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_pinjam.setGeometry(QtCore.QRect(120, 490, 561, 40))
        self.dateEdit_pinjam.setDate(QtCore.QDate.currentDate())
        
        self.label_kembali = QtWidgets.QLabel(self.centralwidget)
        self.label_kembali.setGeometry(QtCore.QRect(120, 540, 561, 30))
        self.label_kembali.setText("Tanggal Kembali:")
        
        self.dateEdit_kembali = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_kembali.setGeometry(QtCore.QRect(120, 570, 561, 40))
        # Set default return date to 1 day after current date
        next_day = QtCore.QDate.currentDate().addDays(1)
        self.dateEdit_kembali.setDate(next_day)
        
        # Buttons
        self.pushButton_pinjam = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pinjam.setGeometry(QtCore.QRect(450, 630, 230, 50))
        self.pushButton_pinjam.setText("PINJAM")
        self.pushButton_pinjam.clicked.connect(self.simpan_data)
        
        self.pushButton_kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kembali.setGeometry(QtCore.QRect(120, 630, 230, 50))
        self.pushButton_kembali.setText("Kembali")
        self.pushButton_kembali.clicked.connect(self.Kembali)
        self.pushButton_kembali.clicked.connect(MainWindow.close)
        
        MainWindow.setCentralWidget(self.centralwidget)

        # If mobil_id is provided, automatically load details
        if mobil_id:
            self.lineEdit_id.setText(str(mobil_id))
            self.cari_mobil_auto()

    def cari_mobil_auto(self):
        try:
            # Get the mobil ID entered by the user
            id_mbl = int(self.lineEdit_id.text())

            # Connect to MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='uas'
            )
            cursor = conn.cursor()

            # Query to get mobil details
            query = """
            SELECT harga_sewa_mbl, driver, stok_mbl 
            FROM mobil 
            WHERE id_mbl = %s
            """
            cursor.execute(query, (id_mbl,))
            result = cursor.fetchone()

            if result:
                # Update UI with mobil details
                self.lineEdit_sewaperhari.setText(str(result[0]))
                self.comboBox_driver.setCurrentText(result[1])
                
                # Set maximum quantity based on available stock
                max_stock = result[2]
                self.spinBox_jumlah.setMaximum(max_stock)
                
                # Optional: Show stock information
                QtWidgets.QMessageBox.information(
                    None, 
                    "mobil Ditemukan", 
                    f"Stok tersedia: {max_stock}"
                )
                
                # Store mobil_id for later use
                self.mobil_id = id_mbl
            else:
                QtWidgets.QMessageBox.warning(
                    None, 
                    "Peringatan", 
                    "mobil tidak ditemukan"
                )

            cursor.close()
            conn.close()

        except ValueError:
            QtWidgets.QMessageBox.warning(
                None, 
                "Peringatan", 
                "ID mobil harus berupa angka"
            )
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(
                None, 
                "Database Error", 
                str(err)
            )

    def simpan_data(self):
        try:
            # Ambil nilai yang dimasukkan oleh pengguna
            id_user = self.user_id
            
            # Convert QDate to string using properly formatted method
            tanggal_pinjam = self.dateEdit_pinjam.date().toString(QtCore.Qt.ISODate)  
            tanggal_kembali = self.dateEdit_kembali.date().toString(QtCore.Qt.ISODate)  
            
            driver = self.comboBox_driver.currentText()  # Pilihan driver (ya/tidak)
            jumlah_disewa = self.spinBox_jumlah.value()  # Jumlah mobil yang disewa

            print(f"ID User: {id_user}")
            print(f"Tanggal Pinjam: {tanggal_pinjam}")
            print(f"Tanggal Kembali: {tanggal_kembali}")
            print(f"Driver: {driver}")
            print(f"Jumlah Disewa: {jumlah_disewa}")

            # Validasi tanggal
            if self.dateEdit_pinjam.date() >= self.dateEdit_kembali.date():
                QtWidgets.QMessageBox.warning(None, "Peringatan", "Tanggal kembali harus setelah tanggal pinjam")
                return

            # Connect to MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='uas'
            )
            cursor = conn.cursor()

            # Ambil detail mobil berdasarkan ID yang dipilih
            query_mobil = """
            SELECT m.id_mbl, m.harga_sewa_mbl, m.driver, m.stok_mbl
            FROM mobil m
            WHERE m.id_mbl = %s AND m.stok_mbl >= %s
            """
            cursor.execute(query_mobil, (self.mobil_id, jumlah_disewa))
            mobil_result = cursor.fetchone()

            if mobil_result:
                id_mobil = mobil_result[0]  # id_mobil
                harga_sewa = mobil_result[1]  # harga_sewa_mbl
                driver_tersedia = mobil_result[2]  # driver (ya/tidak)
                stok = mobil_result[3]  # stok kendaraan

                # Hitung lama sewa
                tgl_pinjam = datetime.strptime(tanggal_pinjam, "%Y-%m-%d")
                tgl_kembali = datetime.strptime(tanggal_kembali, "%Y-%m-%d")
                lama_sewa = (tgl_kembali - tgl_pinjam).days

                # Hitung total harga sewa
                total_harga = harga_sewa * jumlah_disewa * lama_sewa

                # Tambahan biaya driver jika dipilih
                if driver == 'ya':
                    total_harga += 100000 * jumlah_disewa * lama_sewa  # 100k per mobil per hari

                # Query untuk menyimpan data ke dalam tabel pinjam_mobil
                query_insert = """
                INSERT INTO pinjam (
                    id_mobil, 
                    id_user, 
                    harga_sewa_mobil, 
                    tanggal_pinjam, 
                    tanggal_kembali, 
                    jumlah_disewa,
                    driver
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_insert, (
                    id_mobil, 
                    id_user, 
                    total_harga, 
                    tanggal_pinjam, 
                    tanggal_kembali, 
                    jumlah_disewa,
                    driver
                ))

                # Update stok kendaraan di tabel mobil
                query_update_stok = """
                UPDATE mobil
                SET stok_mbl = stok_mbl - %s
                WHERE id_mbl = %s
                """
                cursor.execute(query_update_stok, (jumlah_disewa, id_mobil))

                conn.commit()  # Commit untuk menyimpan perubahan ke database

                # Tampilkan pesan sukses dengan total harga
                pesan_sukses = f"Penyewaan mobil berhasil!\nTotal Biaya: Rp {total_harga:,.2f}"
                QtWidgets.QMessageBox.information(None, "Sukses", pesan_sukses)
                
                print("Data berhasil disimpan dan stok kendaraan berhasil dikurangi!")
                
                # Call Bayar method to proceed to payment
                self.Bayar()
            else:
                QtWidgets.QMessageBox.warning(None, "Peringatan", "Stok kendaraan tidak mencukupi!")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Database Error", str(err))
            print(f"Database error: {err}")
        except ValueError:
            QtWidgets.QMessageBox.warning(None, "Peringatan", "Invalid input: Please check the input values.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Kesalahan", str(e))
            print(f"An unexpected error occurred: {e}")

    def Kembali(self):
        # Open pilih mobil window
        self.window = QtWidgets.QMainWindow()
        self.ui = mbl.Ui_MainWindow()
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()

    def Bayar(self):
        # Open pembayaran window
        self.window = QtWidgets.QMainWindow()
        self.ui = bayar.Ui_MainWindow()
        self.ui.setupUi(self.window, self.user_id)
        QtWidgets.QApplication.activeWindow().close()
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())