# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from decimal import Decimal
from PyQt5.QtCore import QDate
import kelolaunit_penyewa as kel
import menu_penyewa as menu

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_id=None):
        self.user_id = user_id
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: rgb(24, 121, 202);
            }
            QLabel {
                color: white;
                font-size: 14pt;
            }
            QLineEdit, QDateEdit {
                background-color: rgb(255, 202, 111);
                padding: 8px;
                border-radius: 5px;
                font-size: 12pt;
            }
            QPushButton {
                color: white;
                font-size: 12pt;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton#pushButton_bayar {
                background-color: rgb(6, 131, 35);
            }
            QPushButton#pushButton_kembali {
                background-color: rgb(212, 17, 30);
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        # Title
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(200, 20, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("Pembayaran elf")
        
        # Transaction Details Section
        self.label_transaksi = QtWidgets.QLabel(self.centralwidget)
        self.label_transaksi.setGeometry(QtCore.QRect(50, 100, 300, 30))
        self.label_transaksi.setText("Detail Transaksi Terakhir:")
        
        # Rental Details Labels
        self.label_tanggal_pinjam = QtWidgets.QLabel(self.centralwidget)
        self.label_tanggal_pinjam.setGeometry(QtCore.QRect(50, 150, 300, 30))
        self.label_tanggal_pinjam.setText("Tanggal Pinjam:")
        
        self.label_tanggal_kembali = QtWidgets.QLabel(self.centralwidget)
        self.label_tanggal_kembali.setGeometry(QtCore.QRect(50, 200, 300, 30))
        self.label_tanggal_kembali.setText("Tanggal Kembali:")
        
        self.label_total_sewa = QtWidgets.QLabel(self.centralwidget)
        self.label_total_sewa.setGeometry(QtCore.QRect(50, 250, 300, 30))
        self.label_total_sewa.setText("Total Biaya Sewa:")
        
        self.label_denda = QtWidgets.QLabel(self.centralwidget)
        self.label_denda.setGeometry(QtCore.QRect(50, 300, 300, 30))
        self.label_denda.setText("Denda:")
        
        self.label_total_pembayaran = QtWidgets.QLabel(self.centralwidget)
        self.label_total_pembayaran.setGeometry(QtCore.QRect(50, 350, 300, 30))
        self.label_total_pembayaran.setText("Total Pembayaran:")
        
        # Payment Input
        self.label_bayar = QtWidgets.QLabel(self.centralwidget)
        self.label_bayar.setGeometry(QtCore.QRect(400, 300, 300, 30))
        self.label_bayar.setText("Masukkan Jumlah Bayar:")
        
        self.lineEdit_bayar = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_bayar.setGeometry(QtCore.QRect(400, 350, 350, 50))
        self.lineEdit_bayar.setPlaceholderText("Masukkan nominal pembayaran")
        
        # Buttons
        self.pushButton_bayar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bayar.setGeometry(QtCore.QRect(400, 450, 350, 50))
        self.pushButton_bayar.setText("BAYAR")
        self.pushButton_bayar.clicked.connect(self.bayar_transaksi)
        
        self.pushButton_kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kembali.setGeometry(QtCore.QRect(50, 450, 300, 50))
        self.pushButton_kembali.setText("Kembali")
        self.pushButton_kembali.clicked.connect(self.KelolaUnit)
        self.pushButton_kembali.clicked.connect(MainWindow.close)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Automatically load latest transaction
        self.load_latest_transaction()

    def load_latest_transaction(self):
        try:
            # Connect to database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='uas'
            )
            cursor = conn.cursor(dictionary=True)

            # Find the latest transaction for this user
            query = """
            SELECT p.*, m.harga_sewa_elf 
            FROM pinjam_elf p
            JOIN elf m ON p.id_elf = m.id_elf
            WHERE p.id_user = %s 
            ORDER BY p.id_transaksi_elf DESC 
            LIMIT 1
            """
            cursor.execute(query, (self.user_id,))
            transaction = cursor.fetchone()

            if transaction:
                # Calculate total rental cost and late fees
                tanggal_pinjam = transaction['tanggal_pinjam']
                tanggal_kembali = transaction['tanggal_kembali']
                harga_sewa_per_hari = transaction['harga_sewa_elf']
                jumlah_disewa = transaction['jumlah_disewa']
                driver = transaction['driver']

                # Calculate rental period 
                rental_period = (tanggal_kembali - tanggal_pinjam).days

                # Calculate base rental cost
                total_sewa = harga_sewa_per_hari * jumlah_disewa * rental_period

                # Driver cost calculation
                biaya_driver = 0
                if driver == 'ya':
                    # Add 100,000 IDR per car per day for driver
                    biaya_driver = 100000 * jumlah_disewa * rental_period
                    total_sewa += biaya_driver

                # Late fee calculation
                current_date = QDate.currentDate()
                planned_return_date = QDate.fromString(str(tanggal_kembali), 'yyyy-MM-dd')
                late_days = max(current_date.daysTo(planned_return_date) * -1, 0)
                denda = late_days * 5000  # 5000 IDR per day late

                total_pembayaran = total_sewa + denda

                # Update UI
                self.label_tanggal_pinjam.setText(f"Tanggal Pinjam: {tanggal_pinjam}")
                self.label_tanggal_kembali.setText(f"Tanggal Kembali: {tanggal_kembali}")
                self.label_total_sewa.setText(f"Total Biaya Sewa: Rp {total_sewa - biaya_driver:,.2f}")
                
                # Add a new label for driver cost if driver is selected
                if driver == 'ya':
                    self.label_biaya_driver = QtWidgets.QLabel(self.centralwidget)
                    self.label_biaya_driver.setGeometry(QtCore.QRect(50, 330, 300, 30))
                    self.label_biaya_driver.setText(f"Biaya Driver: Rp {biaya_driver:,.2f}")
                    self.label_biaya_driver.setStyleSheet("color: white; font-size: 14pt;")
                    self.label_biaya_driver.show()
                    
                    # Adjust subsequent labels' positions
                    self.label_denda.setGeometry(QtCore.QRect(50, 380, 300, 30))
                    self.label_total_pembayaran.setGeometry(QtCore.QRect(50, 430, 300, 30))
                    
                    # Move payment input and buttons down
                    self.label_bayar.setGeometry(QtCore.QRect(400, 380, 300, 30))
                    self.lineEdit_bayar.setGeometry(QtCore.QRect(400, 430, 350, 50))
                    self.pushButton_bayar.setGeometry(QtCore.QRect(400, 530, 350, 50))
                    self.pushButton_kembali.setGeometry(QtCore.QRect(50, 530, 300, 50))
                else:
                    # Remove the driver cost label if it exists
                    if hasattr(self, 'label_biaya_driver'):
                        self.label_biaya_driver.deleteLater()
                    
                    # Reset label positions to original
                    self.label_denda.setGeometry(QtCore.QRect(50, 300, 300, 30))
                    self.label_total_pembayaran.setGeometry(QtCore.QRect(50, 350, 300, 30))
                    
                    # Reset payment input and buttons to original positions
                    self.label_bayar.setGeometry(QtCore.QRect(400, 300, 300, 30))
                    self.lineEdit_bayar.setGeometry(QtCore.QRect(400, 350, 350, 50))
                    self.pushButton_bayar.setGeometry(QtCore.QRect(400, 450, 350, 50))
                    self.pushButton_kembali.setGeometry(QtCore.QRect(50, 450, 300, 50))
                
                self.label_denda.setText(f"Denda: Rp {denda:,.2f}")
                self.label_total_pembayaran.setText(f"Total Pembayaran: Rp {total_pembayaran:,.2f}")

                # Store transaction id for payment
                self.current_transaction_id = transaction['id_transaksi_elf']
            else:
                QtWidgets.QMessageBox.warning(None, "Peringatan", "Tidak ada transaksi terakhir ditemukan.")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Database Error", str(err))
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", str(e))

    def bayar_transaksi(self):
        try:
            # Validasi input pembayaran
            jumlah_dibayarkan_str = self.lineEdit_bayar.text().strip()
            
            if not jumlah_dibayarkan_str:
                QtWidgets.QMessageBox.warning(None, "Peringatan", "Masukkan jumlah pembayaran!")
                return

            try:
                jumlah_dibayarkan = Decimal(jumlah_dibayarkan_str)
            except ValueError:
                QtWidgets.QMessageBox.warning(None, "Peringatan", "Masukkan angka yang valid!")
                return

            # Connect ke database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='uas'
            )
            cursor = conn.cursor(dictionary=True)

            # Cari detail transaksi terakhir untuk menghitung total pembayaran
            query_transaksi = """
            SELECT p.*, m.harga_sewa_elf 
            FROM pinjam_elf p
            JOIN elf m ON p.id_elf = m.id_elf
            WHERE p.id_transaksi_elf = %s
            """
            cursor.execute(query_transaksi, (self.current_transaction_id,))
            transaksi = cursor.fetchone()

            if not transaksi:
                QtWidgets.QMessageBox.warning(None, "Peringatan", "Transaksi tidak ditemukan!")
                cursor.close()
                conn.close()
                return

            # Hitung total pembayaran
            tanggal_pinjam = transaksi['tanggal_pinjam']
            tanggal_kembali = transaksi['tanggal_kembali']
            harga_sewa_per_hari = transaksi['harga_sewa_elf']
            jumlah_disewa = transaksi['jumlah_disewa']

            # Hitung total sewa
            rental_period = (tanggal_kembali - tanggal_pinjam).days
            total_sewa = harga_sewa_per_hari * jumlah_disewa * rental_period

            # Add driver cost if driver is selected
            if transaksi['driver'] == 'ya':
                biaya_driver = 100000 * jumlah_disewa * rental_period
                total_sewa += biaya_driver

            # Hitung denda
            current_date = QDate.currentDate()
            planned_return_date = QDate.fromString(str(tanggal_kembali), 'yyyy-MM-dd')
            late_days = max(current_date.daysTo(planned_return_date) * -1, 0)
            denda = late_days * 5000  # 5000 IDR per day late

            total_pembayaran = total_sewa + denda

            # Hitung sisa pembayaran
            sisa_pembayaran = total_pembayaran - jumlah_dibayarkan

            # Query untuk insert pembayaran baru
            query_insert = """
            INSERT INTO pembayaran_elf
            (id_transaksi_elf, id_user, tanggal_dikembalikan, 
            total_pembayaran, denda, dibayarkan, 
            status, sisa_pembayaran_amount) 
            VALUES (%s, %s, %s, %s, %s, %s, 'Pending', %s)
            """
            cursor.execute(query_insert, (
                self.current_transaction_id, 
                self.user_id, 
                tanggal_kembali,
                total_pembayaran, 
                denda, 
                jumlah_dibayarkan, 
                sisa_pembayaran
            ))
            conn.commit()

            QtWidgets.QMessageBox.information(None, "Sukses", "Pembayaran berhasil diajukan dan menunggu konfirmasi admin!")
            
            # Kembali ke menu penyewa
            self.window = QtWidgets.QMainWindow()
            self.ui = menu.Ui_MainWindow()
            self.ui.setupUi(self.window, self.user_id)
            QtWidgets.QApplication.activeWindow().close()
            self.window.show()

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Database Error", str(err))
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", str(e))

    def KelolaUnit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = kel.Ui_MainWindow()
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())