# -*- coding: utf-8 -*-

import sys
import os
import shutil
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap

class Ui_MotorTambahWindow(object):
    def __init__(self):
        self.selected_image_path = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #2196F3;
            }
            QLabel {
                color: white;
                font-size: 12px;
            }
            QLineEdit {
                background-color: #FFD54F;
                border: 1px solid #FFA000;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #FFC107;
                color: black;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #FFA000;
            }
            QPushButton#pushButton_keluar {
                background-color: #F44336;
                color: white;
            }
            QPushButton#pushButton_keluar:hover {
                background-color: #D32F2F;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Create main layout
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # Judul
        title_label = QtWidgets.QLabel("Tambah Data Motor")
        title_label.setStyleSheet("color: white; font-size: 18px; font-weight: bold; align: center;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title_label)

        # Form Layout
        form_layout = QtWidgets.QFormLayout()
        form_layout.setVerticalSpacing(10)
        form_layout.setHorizontalSpacing(20)

        # Input Fields
        self.lineEdit_id = QtWidgets.QLineEdit()
        self.lineEdit_jenis = QtWidgets.QLineEdit()
        self.lineEdit_type = QtWidgets.QLineEdit()
        self.lineEdit_tahun = QtWidgets.QLineEdit()
        self.lineEdit_warna = QtWidgets.QLineEdit()
        self.lineEdit_stok = QtWidgets.QLineEdit()
        self.lineEdit_harga = QtWidgets.QLineEdit()
        
        # Driver Selection
        self.comboBox_driver = QtWidgets.QComboBox()
        self.comboBox_driver.addItems(['Tidak', 'Ya'])

        # Form Layout Add
        form_layout.addRow("ID Motor:", self.lineEdit_id)
        form_layout.addRow("Jenis Motor:", self.lineEdit_jenis)
        form_layout.addRow("Tipe Motor:", self.lineEdit_type)
        form_layout.addRow("Tahun:", self.lineEdit_tahun)
        form_layout.addRow("Warna:", self.lineEdit_warna)
        form_layout.addRow("Stok:", self.lineEdit_stok)
        form_layout.addRow("Harga Sewa:", self.lineEdit_harga)
        form_layout.addRow("Driver:", self.comboBox_driver)

        # Foto Section
        foto_layout = QtWidgets.QHBoxLayout()
        self.label_foto = QtWidgets.QLabel("Foto Motor")
        self.label_foto.setFixedSize(200, 200)
        self.label_foto.setStyleSheet("border: 2px dashed white;")
        self.label_foto.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButton_pilihfoto = QtWidgets.QPushButton("Pilih Foto")
        self.pushButton_pilihfoto.clicked.connect(self.choose_image)
        
        foto_layout.addWidget(self.label_foto)
        foto_layout.addWidget(self.pushButton_pilihfoto)

        # Add Layouts
        layout.addLayout(form_layout)
        layout.addLayout(foto_layout)

        # Button Layout
        button_layout = QtWidgets.QHBoxLayout()
        self.pushButton_simpan = QtWidgets.QPushButton("Simpan")
        self.pushButton_keluar = QtWidgets.QPushButton("Kembali")

        self.pushButton_simpan.clicked.connect(self.insert_motor_data)
        self.pushButton_keluar.clicked.connect(self.go_back)

        button_layout.addWidget(self.pushButton_simpan)
        button_layout.addWidget(self.pushButton_keluar)

        layout.addLayout(button_layout)

    def go_back(self):
        from unit_motor import Ui_MainWindow as T
        self.window = QtWidgets.QMainWindow()
        self.ui = T()
        self.ui.setupUi(self.window)
        QtWidgets.QApplication.activeWindow().close()
        self.window.show()

    def choose_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(None, "Pilih Foto Motor", "", 
                                                   "Gambar (*.png *.jpg *.jpeg *.bmp *.gif)", 
                                                   options=options)
        
        if file_name:
            # Simpan gambar
            self.selected_image_path = self.save_image(file_name)
            
            # Tampilkan gambar
            pixmap = QPixmap(self.selected_image_path)
            self.label_foto.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio))

    def save_image(self, file_name):
        # Buat folder jika belum ada
        image_folder = 'motor_images'
        os.makedirs(image_folder, exist_ok=True)

        import time
        base_name = os.path.basename(file_name)
        unique_name = f"{int(time.time())}_{base_name}"
        destination_path = os.path.join(image_folder, unique_name)

        # Salin file
        shutil.copy(file_name, destination_path)
        return destination_path

    def validate_input(self):
        # Validasi input
        required_fields = [
            self.lineEdit_id, self.lineEdit_jenis, 
            self.lineEdit_type, self.lineEdit_tahun, 
            self.lineEdit_warna, self.lineEdit_stok, 
            self.lineEdit_harga
        ]

        for field in required_fields:
            if not field.text().strip():
                QMessageBox.warning(None, "Error", "Semua field harus diisi!")
                return False
        
        try:
            int(self.lineEdit_tahun.text())
            int(self.lineEdit_stok.text())
            int(self.lineEdit_harga.text())
        except ValueError:
            QMessageBox.warning(None, "Error", "Tahun, Stok, dan Harga harus angka!")
            return False

        return True

    def insert_motor_data(self):
        # Validasi input
        if not self.validate_input():
            return

        try:
            # Koneksi database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="uas"
            )
            mycursor = conn.cursor()

            # Persiapkan data
            driver_status = 'ya' if self.comboBox_driver.currentText() == 'Ya' else 'tidak'
            foto_path = self.selected_image_path if self.selected_image_path else None

            # Query insert
            sql = """
            INSERT INTO motor 
            (id_mtr, jenis_mtr, type_mtr, tahun_mtr, warna_mtr, stok_mtr, harga_sewa_mtr, driver, foto)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            val = (
                self.lineEdit_id.text(), 
                self.lineEdit_jenis.text(), 
                self.lineEdit_type.text(), 
                int(self.lineEdit_tahun.text()), 
                self.lineEdit_warna.text(), 
                int(self.lineEdit_stok.text()), 
                int(self.lineEdit_harga.text()), 
                driver_status,
                foto_path
            )

            mycursor.execute(sql, val)
            conn.commit()

            # Pesan sukses
            QMessageBox.information(None, "Sukses", "Data Motor Berhasil Disimpan!")
            
            # Reset form
            self.reset_form()

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error Database", f"Gagal menyimpan data: {err}")
        finally:
            if conn.is_connected():
                mycursor.close()
                conn.close()

    def reset_form(self):
        # Reset semua input field
        for field in [
            self.lineEdit_id, self.lineEdit_jenis, 
            self.lineEdit_type, self.lineEdit_tahun, 
            self.lineEdit_warna, self.lineEdit_stok, 
            self.lineEdit_harga
        ]:
            field.clear()
        
        self.comboBox_driver.setCurrentIndex(0)
        self.label_foto.clear()
        self.label_foto.setText("Foto Motor")
        self.selected_image_path = None

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MotorTambahWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()