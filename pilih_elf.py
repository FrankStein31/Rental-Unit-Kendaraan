# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import menu_penyewa as mep
import sewa_elf as se
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
        
        # Left side: elf List
        self.left_widget = QtWidgets.QWidget()
        self.left_layout = QtWidgets.QVBoxLayout(self.left_widget)
        
        # Title
        self.label = QtWidgets.QLabel("Daftar elf yang Tersedia")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.left_layout.addWidget(self.label)
        
        # Table for elfs
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
        
        # elf Details
        self.details_label = QtWidgets.QLabel()
        self.details_label.setStyleSheet("color: white; font-size: 14px;")
        self.right_layout.addWidget(self.details_label)
        
        # Quantity Selection
        quantity_layout = QtWidgets.QHBoxLayout()
        self.label_quantity = QtWidgets.QLabel("Jumlah elf:")
        self.label_quantity.setStyleSheet("color: white;")
        self.spinBox_quantity = QtWidgets.QSpinBox()
        self.spinBox_quantity.setMinimum(1)
        quantity_layout.addWidget(self.label_quantity)
        quantity_layout.addWidget(self.spinBox_quantity)
        self.right_layout.addLayout(quantity_layout)
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        self.pinjam_button = QtWidgets.QPushButton("Pinjam elf")
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
        self.tableWidget.itemSelectionChanged.connect(self.display_elf_details)
        self.kembali_button.clicked.connect(self.KembaliMenu)
        self.kembali_button.clicked.connect(MainWindow.close)
        self.pinjam_button.clicked.connect(self.Pinjam)
        self.pinjam_button.clicked.connect(MainWindow.close)
        
        # Load elfs
        self.load_elfs()
        
    def load_elfs(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='uas'
            )
            cursor = conn.cursor()
            
            query = "SELECT * FROM elf WHERE stok_elf > 0"  # Only show elfs with available stock
            cursor.execute(query)
            elfs = cursor.fetchall()
            
            self.tableWidget.setRowCount(len(elfs))
            
            for row, elf in enumerate(elfs):
                for col, value in enumerate(elf[:-1]):  # Exclude last column (foto)
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, item)
            
            cursor.close()
            conn.close()
            
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Database Error", str(err))
    
    def display_elf_details(self):
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
            
            # Get full elf details
            elf_id = self.tableWidget.item(row, 0).text()
            query = """
            SELECT foto, id_elf, jenis_elf, type_elf, tahun_elf, warna_elf, stok_elf, harga_sewa_elf, driver 
            FROM elf 
            WHERE id_elf = %s
            """
            cursor.execute(query, (elf_id,))
            elf_details = cursor.fetchone()
            
            if elf_details:
                # Display image
                pixmap = QtGui.QPixmap(elf_details[0])
                scaled_pixmap = pixmap.scaled(
                    400, 400, 
                    QtCore.Qt.KeepAspectRatio, 
                    QtCore.Qt.SmoothTransformation
                )
                self.image_label.setPixmap(scaled_pixmap)
                
                # Update details label
                details_text = (
                    f"ID elf: {elf_details[1]}\n"
                    f"Jenis: {elf_details[2]}\n"
                    f"Tipe: {elf_details[3]}\n"
                    f"Tahun: {elf_details[4]}\n"
                    f"Warna: {elf_details[5]}\n"
                    f"Stok Tersedia: {elf_details[6]}\n"
                    f"Harga Sewa/Hari: Rp {elf_details[7]}\n"
                    f"Driver Tersedia: {elf_details[8]}"
                )
                self.details_label.setText(details_text)
                
                # Set max quantity for spinbox
                self.spinBox_quantity.setMaximum(elf_details[6])
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
            QtWidgets.QMessageBox.warning(None, "Peringatan", "Pilih elf terlebih dahulu")
            return
        
        row = selected_rows[0].row()
        id_elf = self.tableWidget.item(row, 0).text()
        jumlah_elf = self.spinBox_quantity.value()
        
        self.window = QtWidgets.QMainWindow()
        self.ui = se.Ui_MainWindow()
        self.ui.setupUi(self.window, id_elf, self.user_id)
        
        # Pre-set the quantity in the next window
        self.ui.spinBox_jumlah.setValue(jumlah_elf)
        
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())