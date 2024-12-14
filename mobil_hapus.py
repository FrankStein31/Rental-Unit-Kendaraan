from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtWidgets import QMessageBox, QHeaderView
import mysql.connector
import os
import sys
import menu_admin as mad

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #1479CA;
            }
            QLabel {
                color: white;
                font-size: 12px;
            }
            QTableView {
                background-color: #F0F0F0;
                alternate-background-color: #E0E0E0;
                selection-background-color: #BDE0FE;
            }
            QHeaderView::section {
                background-color: #2196F3;
                color: white;
                padding: 5px;
                border: 1px solid #1976D2;
                font-weight: bold;
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
        
        # Main Layout
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title_label = QtWidgets.QLabel("HAPUS DATA MOBIL")
        title_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold; align: center;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Table View
        self.tableView = QtWidgets.QTableView()
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Create Model
        self.model = QStandardItemModel()
        self.model.setColumnCount(8)
        self.model.setHorizontalHeaderLabels(["ID", "Jenis", "Tipe", "Tahun", "Warna", "Stok", "Harga", "Status Driver"])
        self.tableView.setModel(self.model)
        
        layout.addWidget(self.tableView)
        
        # Detail Section
        detail_layout = QtWidgets.QHBoxLayout()
        
        # Foto Label
        self.label_foto = QtWidgets.QLabel("Foto Mobil")
        self.label_foto.setFixedSize(250, 250)
        self.label_foto.setStyleSheet("border: 2px dashed white;")
        self.label_foto.setAlignment(QtCore.Qt.AlignCenter)
        
        detail_layout.addWidget(self.label_foto)
        
        # Button Layout
        button_layout = QtWidgets.QVBoxLayout()
        self.pushButton_hapus = QtWidgets.QPushButton("Hapus Mobil")
        self.pushButton_refresh = QtWidgets.QPushButton("Refresh Data")
        self.pushButton_keluar = QtWidgets.QPushButton("Kembali")
        
        button_layout.addWidget(self.pushButton_hapus)
        button_layout.addWidget(self.pushButton_refresh)
        button_layout.addWidget(self.pushButton_keluar)
        
        detail_layout.addLayout(button_layout)
        
        layout.addLayout(detail_layout)
        
        # Connect buttons
        self.pushButton_hapus.clicked.connect(self.delete_mobil)
        self.pushButton_refresh.clicked.connect(self.load_mobil_data)
        self.pushButton_keluar.clicked.connect(self.KembaliMenu)
        
        # Connect selection changed
        self.tableView.selectionModel().selectionChanged.connect(self.show_mobil_details)
        
        # Initial data load
        self.load_mobil_data()

    def load_mobil_data(self):
        self.model.removeRows(0, self.model.rowCount())
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="uas"
            )
            mycursor = conn.cursor()

            sql = "SELECT * FROM mobil"
            mycursor.execute(sql)
            results = mycursor.fetchall()

            for result in results:
                row_data = []
                for col in range(8):
                    item = QStandardItem(str(result[col]))
                    row_data.append(item)
                self.model.appendRow(row_data)

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"Database error: {err}")
        finally:
            if conn.is_connected():
                mycursor.close()
                conn.close()

    def show_mobil_details(self):
        # Clear previous photo
        self.label_foto.clear()
        self.label_foto.setText("Foto mobil")
        
        # Get selected row
        indexes = self.tableView.selectedIndexes()
        if not indexes:
            return
        
        row = indexes[0].row()
        id_mobil = self.model.item(row, 0).text()

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="uas"
            )
            mycursor = conn.cursor()

            sql = "SELECT foto FROM mobil WHERE id_mbl = %s"
            val = (id_mobil,)
            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            if result and result[0]:
                foto_path = result[0]
                if os.path.exists(foto_path):
                    pixmap = QPixmap(foto_path)
                    scaled_pixmap = pixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                    self.label_foto.setPixmap(scaled_pixmap)
                else:
                    self.label_foto.setText("Foto Tidak Tersedia")

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"Database error: {err}")
        finally:
            if conn.is_connected():
                mycursor.close()
                conn.close()

    def delete_mobil(self):
        # Get selected row
        indexes = self.tableView.selectedIndexes()
        if not indexes:
            QMessageBox.warning(None, "Peringatan", "Pilih mobil yang akan dihapus!")
            return
        
        row = indexes[0].row()
        id_mobil = self.model.item(row, 0).text()
        
        # Konfirmasi penghapusan
        reply = QMessageBox.question(
            None, 
            'Konfirmasi Hapus', 
            f'Apakah Anda yakin ingin menghapus mobil dengan ID {id_mobil}?',
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="uas"
            )
            mycursor = conn.cursor()

            # Cari path foto sebelum menghapus
            sql_foto = "SELECT foto FROM mobil WHERE id_mbl = %s"
            mycursor.execute(sql_foto, (id_mobil,))
            foto_result = mycursor.fetchone()

            # Hapus data dari database
            sql_delete = "DELETE FROM mobil WHERE id_mbl = %s"
            mycursor.execute(sql_delete, (id_mobil,))
            conn.commit()

            # Hapus file foto jika ada
            if foto_result and foto_result[0]:
                foto_path = foto_result[0]
                if os.path.exists(foto_path):
                    try:
                        os.remove(foto_path)
                    except Exception as e:
                        QMessageBox.warning(None, "Peringatan", f"Gagal menghapus foto: {e}")

            # Tampilkan pesan sukses
            QMessageBox.information(None, "Sukses", f"mobil dengan ID {id_mobil} berhasil dihapus!")

            # Refresh data tabel
            self.load_mobil_data()

            # Reset foto label
            self.label_foto.clear()
            self.label_foto.setText("Foto mobil")

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error", f"Gagal menghapus data: {err}")
        finally:
            if conn.is_connected():
                mycursor.close()
                conn.close()

    def KembaliMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mad.Ui_MainWindow()
        self.ui.setupUi(self.window)
        QtWidgets.QApplication.activeWindow().close()
        self.window.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()