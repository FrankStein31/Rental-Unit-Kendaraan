from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QFileDialog, QMessageBox, QTableWidgetItem, 
                             QTableWidget, QVBoxLayout, QHBoxLayout)
import mysql.connector
import os
import menu_admin as mad
import shutil
import uuid
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)  # Perbesar lebar window
        MainWindow.setStyleSheet("""
            background-color: rgb(250, 250, 250); 
            font-family: 'Segoe UI', Arial, sans-serif;
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.central_layout = QHBoxLayout(self.centralwidget)
        
        # Layout kiri untuk form input
        left_layout = QVBoxLayout()
        
        # Form Input elf
        form_layout = QVBoxLayout()
        
        # ID
        id_layout = QHBoxLayout()
        self.label_5 = QtWidgets.QLabel("ID:")
        self.label_5.setStyleSheet("color: #333; font-weight: bold;")
        self.lineEdit_id = QtWidgets.QLineEdit()
        self.lineEdit_id.setStyleSheet("""
            border: 1px solid #d1d5db;
            border-radius: 4px;
            padding: 5px;
            background-color: white;
        """)
        id_layout.addWidget(self.label_5)
        id_layout.addWidget(self.lineEdit_id)
        form_layout.addLayout(id_layout)
        
        # Jenis
        jenis_layout = QHBoxLayout()
        self.label_6 = QtWidgets.QLabel("Jenis:")
        self.label_6.setStyleSheet("color: #333; font-weight: bold;")
        self.lineEdit_jenis = QtWidgets.QLineEdit()
        self.lineEdit_jenis.setStyleSheet("""
            border: 1px solid #d1d5db;
            border-radius: 4px;
            padding: 5px;
            background-color: white;
        """)
        jenis_layout.addWidget(self.label_6)
        jenis_layout.addWidget(self.lineEdit_jenis)
        form_layout.addLayout(jenis_layout)
        
        # Type
        type_layout = QHBoxLayout()
        self.label_7 = QtWidgets.QLabel("Type:")
        self.label_7.setStyleSheet("color: #333; font-weight: bold;")
        self.lineEdit_type = QtWidgets.QLineEdit()
        self.lineEdit_type.setStyleSheet("""
            border: 1px solid #d1d5db;
            border-radius: 4px;
            padding: 5px;
            background-color: white;
        """)
        type_layout.addWidget(self.label_7)
        type_layout.addWidget(self.lineEdit_type)
        form_layout.addLayout(type_layout)
        
        # Tahun
        tahun_layout = QHBoxLayout()
        self.label_8 = QtWidgets.QLabel("Tahun:")
        self.label_8.setStyleSheet("color: #333; font-weight: bold;")
        self.lineEdit_tahun = QtWidgets.QLineEdit()
        self.lineEdit_tahun.setStyleSheet("""
            border: 1px solid #d1d5db;
            border-radius: 4px;
            padding: 5px;
            background-color: white;
        """)
        tahun_layout.addWidget(self.label_8)
        tahun_layout.addWidget(self.lineEdit_tahun)
        form_layout.addLayout(tahun_layout)
        
        # Warna
        warna_layout = QHBoxLayout()
        self.label_9 = QtWidgets.QLabel("Warna:")
        self.label_9.setStyleSheet("color: #333; font-weight: bold;")
        self.lineEdit_warna = QtWidgets.QLineEdit()
        self.lineEdit_warna.setStyleSheet("""
            border: 1px solid #d1d5db;
            border-radius: 4px;
            padding: 5px;
            background-color: white;
        """)
        warna_layout.addWidget(self.label_9)
        warna_layout.addWidget(self.lineEdit_warna)
        form_layout.addLayout(warna_layout)
        
        # Stok
        stok_layout = QHBoxLayout()
        self.label_12 = QtWidgets.QLabel("Stok:")
        self.label_12.setStyleSheet("color: #333; font-weight: bold;")
        self.lineEdit_stok = QtWidgets.QLineEdit()
        self.lineEdit_stok.setStyleSheet("""
            border: 1px solid #d1d5db;
            border-radius: 4px;
            padding: 5px;
            background-color: white;
        """)
        stok_layout.addWidget(self.label_12)
        stok_layout.addWidget(self.lineEdit_stok)
        form_layout.addLayout(stok_layout)
        
        # Harga
        harga_layout = QHBoxLayout()
        self.label_14 = QtWidgets.QLabel("Harga:")
        self.label_14.setStyleSheet("color: #333; font-weight: bold;")
        self.lineEdit_harga = QtWidgets.QLineEdit()
        self.lineEdit_harga.setStyleSheet("""
            border: 1px solid #d1d5db;
            border-radius: 4px;
            padding: 5px;
            background-color: white;
        """)
        harga_layout.addWidget(self.label_14)
        harga_layout.addWidget(self.lineEdit_harga)
        form_layout.addLayout(harga_layout)
        
        # Foto
        foto_layout = QVBoxLayout()
        self.label_13 = QtWidgets.QLabel("Foto Kendaraan:")
        self.label_13.setStyleSheet("color: #333; font-weight: bold;")
        self.label = QtWidgets.QLabel("image")
        self.pushButton_pilihfoto = QtWidgets.QPushButton("Pilih Foto")
        foto_layout.addWidget(self.label_13)
        foto_layout.addWidget(self.label)
        foto_layout.addWidget(self.pushButton_pilihfoto)
        form_layout.addLayout(foto_layout)
        
        # Tombol Aksi
        action_layout = QHBoxLayout()
        self.pushButton_cari = QtWidgets.QPushButton("Cari")
        self.pushButton_simpan = QtWidgets.QPushButton("Simpan")
        self.pushButton_keluar = QtWidgets.QPushButton("Kembali")
        
        # Styling Tombol
        self.pushButton_cari.setStyleSheet("""
            background-color: #3b82f6; 
            color: white;
            border-radius: 4px;
            padding: 8px;
            font-weight: bold;
        """)
        self.pushButton_simpan.setStyleSheet("""
            background-color: #10b981; 
            color: white;
            border-radius: 4px;
            padding: 8px;
            font-weight: bold;
        """)
        self.pushButton_keluar.setStyleSheet("""
            background-color: #ef4444; 
            color: white;
            border-radius: 4px;
            padding: 8px;
            font-weight: bold;
        """)
        
        action_layout.addWidget(self.pushButton_cari)
        action_layout.addWidget(self.pushButton_simpan)
        action_layout.addWidget(self.pushButton_keluar)
        
        # Susun layout kiri
        left_layout.addLayout(form_layout)
        left_layout.addLayout(action_layout)
        
        # Tabel untuk menampilkan daftar elf
        self.elf_table = QTableWidget()
        self.elf_table.setColumnCount(7)
        self.elf_table.setHorizontalHeaderLabels(
            ["ID", "Jenis", "Tipe", "Tahun", "Warna", "Stok", "Harga Sewa"]
        )
        
        # Styling Tabel
        self.elf_table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #d1d5db;
                border-radius: 4px;
            }
            QHeaderView::section {
                background-color: #f3f4f6;
                color: #111827;
                padding: 5px;
                border: 1px solid #d1d5db;
                font-weight: bold;
            }
        """)
        
        # Layout utama
        self.central_layout.addLayout(left_layout, 1)
        self.central_layout.addWidget(self.elf_table, 2)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Koneksi sinyal
        self.pushButton_pilihfoto.clicked.connect(self.images)
        self.pushButton_cari.clicked.connect(self.cari_elf_by_jenis)
        self.pushButton_simpan.clicked.connect(self.update_elf_data)
        self.pushButton_keluar.clicked.connect(self.KembaliMenu)
        self.pushButton_keluar.clicked.connect(MainWindow.close)
        
        # Tampilkan semua elf saat pertama kali dibuka
        self.load_all_elfs()
        
        # Double click pada tabel untuk edit
        self.elf_table.doubleClicked.connect(self.isi_form_dari_tabel)

    def load_all_elfs(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="uas"
            )
            mycursor = conn.cursor()
            
            mycursor.execute("SELECT * FROM elf")
            results = mycursor.fetchall()
            
            self.elf_table.setRowCount(0)
            for row_data in results:
                row_position = self.elf_table.rowCount()
                self.elf_table.insertRow(row_position)
                for i, value in enumerate(row_data):
                    self.elf_table.setItem(row_position, i, QTableWidgetItem(str(value)))
            
            mycursor.close()
            conn.close()
        
        except mysql.connector.Error as err:
            QMessageBox.warning(self.centralwidget, "Error", f"Terjadi kesalahan: {err}")

    def cari_elf_by_jenis(self):
        jenis_elf = self.lineEdit_jenis.text()

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="uas"
            )
            mycursor = conn.cursor()

            sql = "SELECT * FROM elf WHERE jenis_elf LIKE %s"
            val = (f"%{jenis_elf}%",)

            mycursor.execute(sql, val)
            results = mycursor.fetchall()

            self.elf_table.setRowCount(0)
            for row_data in results:
                row_position = self.elf_table.rowCount()
                self.elf_table.insertRow(row_position)
                for i, value in enumerate(row_data):
                    self.elf_table.setItem(row_position, i, QTableWidgetItem(str(value)))

            if not results:
                QMessageBox.information(self.centralwidget, "Data Tidak Ditemukan", "elf dengan jenis tersebut tidak ditemukan.")

            mycursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QMessageBox.warning(self.centralwidget, "Error", f"Terjadi kesalahan: {err}")

    def isi_form_dari_tabel(self):
        current_row = self.elf_table.currentRow()
        
        # Pastikan ada baris yang dipilih
        if current_row >= 0:
            # Ambil data dari setiap kolom
            id_elf = self.elf_table.item(current_row, 0).text()
            jenis_elf = self.elf_table.item(current_row, 1).text()
            type_elf = self.elf_table.item(current_row, 2).text()
            tahun_elf = self.elf_table.item(current_row, 3).text()
            warna_elf = self.elf_table.item(current_row, 4).text()
            stok_elf = self.elf_table.item(current_row, 5).text()
            harga_sewa_elf = self.elf_table.item(current_row, 6).text()
            
            # Isi form dengan data yang dipilih
            self.lineEdit_id.setText(id_elf)
            self.lineEdit_jenis.setText(jenis_elf)
            self.lineEdit_type.setText(type_elf)
            self.lineEdit_tahun.setText(tahun_elf)
            self.lineEdit_warna.setText(warna_elf)
            self.lineEdit_stok.setText(stok_elf)
            self.lineEdit_harga.setText(harga_sewa_elf)

            # Tambahkan pencarian foto
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="uas"
                )
                mycursor = conn.cursor()
                
                # Query untuk mengambil path foto
                mycursor.execute("SELECT foto FROM elf WHERE id_elf = %s", (id_elf,))
                result = mycursor.fetchone()
                
                # Tampilkan foto jika ada
                if result and result[0]:
                    foto_path = result[0]
                    if os.path.exists(foto_path):
                        pixmap = QPixmap(foto_path)
                        self.label.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio))
                        # Simpan path foto untuk digunakan nanti
                        self.current_image_path = foto_path
                    else:
                        self.label.setText("Foto tidak ditemukan")
                        self.current_image_path = None
                else:
                    self.label.setText("Tidak ada foto")
                    self.current_image_path = None
                
                mycursor.close()
                conn.close()
            
            except mysql.connector.Error as err:
                QMessageBox.warning(self.centralwidget, "Error", f"Terjadi kesalahan: {err}")

    def images(self):
        # Buka dialog untuk memilih gambar
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(None, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        
        if file_name:
            # Simpan path gambar asli untuk digunakan nanti
            self.current_image_path = file_name
            
            # Menyimpan gambar ke folder tertentu
            saved_image_path = self.save_image(file_name)
            print(f"Gambar disimpan di: {saved_image_path}")
            
            # Menampilkan gambar yang dipilih
            pixmap = QPixmap(saved_image_path)
            if not pixmap.isNull():  # Periksa apakah gambar berhasil dimuat
                self.label.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio))  # Menampilkan gambar
                self.label.setText("")  # Menghapus teks default
            else:
                QtWidgets.QMessageBox.warning(self.centralwidget, "Error", "Gagal memuat gambar.")

    def save_image(self, file_name):
        # Buat folder jika belum ada
        image_folder = 'elf_images'
        os.makedirs(image_folder, exist_ok=True)

        # Generate nama file unik menggunakan timestamp
        import time
        import uuid
        base_name = os.path.basename(file_name)
        unique_name = f"{uuid.uuid4()}_{int(time.time())}_{base_name}"
        destination_path = os.path.join(image_folder, unique_name)

        # Salin file
        shutil.copy(file_name, destination_path)
        return destination_path

    def update_elf_data(self):
        try:
            # Ambil input dari field yang ada di GUI
            id_elf = self.lineEdit_id.text()  
            jenis_elf = self.lineEdit_jenis.text()  
            type_elf = self.lineEdit_type.text()  
            tahun_elf = self.lineEdit_tahun.text()
            warna_elf = self.lineEdit_warna.text()  
            stok_elf = int(self.lineEdit_stok.text())  
            harga_sewa_elf = int(self.lineEdit_harga.text())  

            # Validasi input tidak boleh kosong
            if not all([id_elf, jenis_elf, type_elf, tahun_elf, warna_elf, stok_elf, harga_sewa_elf]):
                QtWidgets.QMessageBox.warning(
                    None, 
                    "Peringatan", 
                    "Semua field harus diisi!"
                )
                return

            # Koneksi ke database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="uas"  
            )
            mycursor = conn.cursor()

            # Cek apakah ada foto baru yang dipilih
            foto_path = None
            try:
                # Cek apakah label memiliki pixmap (gambar)
                if not self.label.pixmap().isNull():
                    foto_path = self.save_image(self.current_image_path) if hasattr(self, 'current_image_path') else None
            except Exception:
                foto_path = None

            # Query SQL untuk memperbarui data elf
            if foto_path:
                sql = """
                UPDATE elf
                SET jenis_elf = %s, type_elf = %s, tahun_elf = %s, 
                    warna_elf = %s, stok_elf = %s, harga_sewa_elf = %s, foto = %s
                WHERE id_elf = %s
                """
                val = (jenis_elf, type_elf, tahun_elf, warna_elf, stok_elf, harga_sewa_elf, foto_path, id_elf)
            else:
                sql = """
                UPDATE elf
                SET jenis_elf = %s, type_elf = %s, tahun_elf = %s, 
                    warna_elf = %s, stok_elf = %s, harga_sewa_elf = %s
                WHERE id_elf = %s
                """
                val = (jenis_elf, type_elf, tahun_elf, warna_elf, stok_elf, harga_sewa_elf, id_elf)
            
            mycursor.execute(sql, val)

            # Commit perubahan
            conn.commit()

            # Tampilkan popup berhasil
            QtWidgets.QMessageBox.information(
                None, 
                "Berhasil", 
                "Data elf berhasil diperbarui!"
            )

            # Load ulang data tabel
            self.load_all_elfs()

            # Clear form input
            self.clear_form()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(
                None, 
                "Error Database", 
                f"Terjadi kesalahan: {err}"
            )
        except ValueError:
            QtWidgets.QMessageBox.warning(
                None, 
                "Peringatan", 
                "Pastikan Stok dan Harga berupa angka!"
            )
        finally:
            # Pastikan koneksi ditutup
            if 'conn' in locals():
                conn.close()

    def clear_form(self):
        # Method untuk mengosongkan semua field input
        self.lineEdit_id.clear()
        self.lineEdit_jenis.clear()
        self.lineEdit_type.clear()
        self.lineEdit_tahun.clear()
        self.lineEdit_warna.clear()
        self.lineEdit_stok.clear()
        self.lineEdit_harga.clear()

        # Reset label foto jika perlu
        self.label.setText("image")

    def KembaliMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mad.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Warna :"))
        self.label_8.setText(_translate("MainWindow", "Tahun :"))
        self.label_6.setText(_translate("MainWindow", "Jenis :"))
        self.label_5.setText(_translate("MainWindow", "ID :"))
        self.label_7.setText(_translate("MainWindow", "Type :"))
        self.label_12.setText(_translate("MainWindow", "Stok :"))
        self.label_13.setText(_translate("MainWindow", "Foto Kendaraan :"))
        self.pushButton_pilihfoto.setText(_translate("MainWindow", "Pilih Foto"))
        self.label_10.setText(_translate("MainWindow", "elf"))
        self.label.setText(_translate("MainWindow", "image"))
        self.label_14.setText(_translate("MainWindow", "Harga :"))
        self.pushButton_cari.setText(_translate("MainWindow", "cari"))
        self.pushButton_simpan.setText(_translate("MainWindow", "SIMPAN"))
        self.pushButton_keluar.setText(_translate("MainWindow", "Kembali"))
        self.pushButton_cari.clicked.connect(self.cari_elf)
        self.pushButton_simpan.clicked.connect(self.update_elf_data)
        self.pushButton_keluar.clicked.connect(self.KembaliMenu)
        self.pushButton_keluar.clicked.connect(MainWindow.close)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
