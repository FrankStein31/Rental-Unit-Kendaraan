# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import menu_penyewa as mep
import sewa_mbl as se
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_id=None):
        self.user_id = user_id
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)  # Increased window width for more details
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main layout
        self.main_layout = QtWidgets.QHBoxLayout(self.centralwidget)
        
        # Left side: mobil List
        self.left_widget = QtWidgets.QWidget()
        self.left_layout = QtWidgets.QVBoxLayout(self.left_widget)
        
        # Title
        self.label = QtWidgets.QLabel("Daftar mobil yang Tersedia")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.left_layout.addWidget(self.label)
        
        # Table for mobils
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setColumnCount(8)  # Increased columns
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Jenis", "Type", "Tahun", "Warna", "Stok", "Harga Sewa", "Driver"]
        )
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setStyleSheet("background-color: white;")
        self.left_layout.addWidget(self.tableWidget)
        
        # Right side: Detailed Information
        self.right_widget = QtWidgets.QWidget()
        self.right_layout = QtWidgets.QVBoxLayout(self.right_widget)
        
        # Large Image Label
        self.image_label = QtWidgets.QLabel()
        self.image_label.setMinimumSize(400, 400)
        self.image_label.setStyleSheet("background-color: white; border: 2px solid black;")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.right_layout.addWidget(self.image_label)
        
        # mobil Details
        self.details_label = QtWidgets.QLabel()
        self.details_label.setStyleSheet("color: white; font-size: 14px;")
        self.right_layout.addWidget(self.details_label)
        
        # Quantity Selection
        quantity_layout = QtWidgets.QHBoxLayout()
        self.label_quantity = QtWidgets.QLabel("Jumlah mobil:")
        self.label_quantity.setStyleSheet("color: white;")
        self.spinBox_quantity = QtWidgets.QSpinBox()
        self.spinBox_quantity.setMinimum(1)
        quantity_layout.addWidget(self.label_quantity)
        quantity_layout.addWidget(self.spinBox_quantity)
        self.right_layout.addLayout(quantity_layout)
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        self.pinjam_button = QtWidgets.QPushButton("Pinjam mobil")
        self.kembali_button = QtWidgets.QPushButton("Kembali")
        
        self.pinjam_button.setStyleSheet("background-color: green; color: white;")
        self.kembali_button.setStyleSheet("background-color: red; color: white;")
        
        button_layout.addWidget(self.kembali_button)
        button_layout.addWidget(self.pinjam_button)
        
        self.right_layout.addLayout(button_layout)
        
        # Add widgets to main layout
        self.main_layout.addWidget(self.left_widget, 2)
        self.main_layout.addWidget(self.right_widget, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Connections
        self.tableWidget.itemSelectionChanged.connect(self.display_mobil_details)
        self.kembali_button.clicked.connect(self.KembaliMenu)
        self.kembali_button.clicked.connect(MainWindow.close)
        self.pinjam_button.clicked.connect(self.Pinjam)
        self.pinjam_button.clicked.connect(MainWindow.close)
        
        # Load mobils
        self.load_mobils()
        
    def load_mobils(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='uas'
            )
            cursor = conn.cursor()
            
            query = "SELECT * FROM mobil WHERE stok_mbl > 0"  # Only show mobils with available stock
            cursor.execute(query)
            mobils = cursor.fetchall()
            
            self.tableWidget.setRowCount(len(mobils))
            
            for row, mobil in enumerate(mobils):
                for col, value in enumerate(mobil[:-1]):  # Exclude last column (foto)
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, item)
            
            cursor.close()
            conn.close()
            
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Database Error", str(err))
    
    def display_mobil_details(self):
        # Get selected row
        selected_rows = self.tableWidget.selectedIndexes()
        if not selected_rows:
            return
        
        row = selected_rows[0].row()
        
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='uas'
            )
            cursor = conn.cursor()
            
            # Get full mobil details
            mobil_id = self.tableWidget.item(row, 0).text()
            query = """
            SELECT foto, id_mbl, jenis_mbl, type_mbl, tahun_mbl, warna_mbl, stok_mbl, harga_sewa_mbl, driver 
            FROM mobil 
            WHERE id_mbl = %s
            """
            cursor.execute(query, (mobil_id,))
            mobil_details = cursor.fetchone()
            
            if mobil_details:
                # Display image
                pixmap = QtGui.QPixmap(mobil_details[0])
                scaled_pixmap = pixmap.scaled(
                    400, 400, 
                    QtCore.Qt.KeepAspectRatio, 
                    QtCore.Qt.SmoothTransformation
                )
                self.image_label.setPixmap(scaled_pixmap)
                
                # Update details label
                details_text = (
                    f"ID mobil: {mobil_details[1]}\n"
                    f"Jenis: {mobil_details[2]}\n"
                    f"Tipe: {mobil_details[3]}\n"
                    f"Tahun: {mobil_details[4]}\n"
                    f"Warna: {mobil_details[5]}\n"
                    f"Stok Tersedia: {mobil_details[6]}\n"
                    f"Harga Sewa/Hari: Rp {mobil_details[7]}\n"
                    f"Driver Tersedia: {mobil_details[8]}"
                )
                self.details_label.setText(details_text)
                
                # Set max quantity for spinbox
                self.spinBox_quantity.setMaximum(mobil_details[6])
                self.spinBox_quantity.setValue(1)
            
            cursor.close()
            conn.close()
            
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Database Error", str(err))
    
    def KembaliMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mep.Ui_MainWindow()
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()
    
    def Pinjam(self):
        selected_rows = self.tableWidget.selectedIndexes()
        if not selected_rows:
            QtWidgets.QMessageBox.warning(None, "Peringatan", "Pilih mobil terlebih dahulu")
            return
        
        row = selected_rows[0].row()
        id_mobil = self.tableWidget.item(row, 0).text()
        jumlah_mobil = self.spinBox_quantity.value()
        
        self.window = QtWidgets.QMainWindow()
        self.ui = se.Ui_MainWindow()
        self.ui.setupUi(self.window, id_mobil, self.user_id)
        
        # Pre-set the quantity in the next window
        self.ui.spinBox_jumlah.setValue(jumlah_mobil)
        
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())