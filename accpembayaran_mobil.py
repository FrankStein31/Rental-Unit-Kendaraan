import sys
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import menu_acc as acc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main layout
        self.main_layout = QtWidgets.QHBoxLayout(self.centralwidget)
        
        # Left side layout for search and filters
        self.left_layout = QtWidgets.QVBoxLayout()
        
        # Title
        self.label_title = QtWidgets.QLabel("Acc Pembayaran Mobil")
        self.label_title.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.label_title.setAlignment(Qt.AlignCenter)
        
        # Transaction List
        self.transaction_list = QtWidgets.QTableView()
        self.transaction_list.setStyleSheet("background-color: white;")
        self.transaction_model = QStandardItemModel()
        self.transaction_model.setHorizontalHeaderLabels([
            "ID Transaksi", 
            "Nama User", 
            "Total Pembayaran", 
            "Status"
        ])
        self.transaction_list.setModel(self.transaction_model)
        
        # Detail section
        self.detail_group = QtWidgets.QGroupBox("Detail Transaksi")
        self.detail_group.setStyleSheet("color: white;")
        self.detail_layout = QtWidgets.QFormLayout()
        
        self.detail_id = QtWidgets.QLineEdit()
        self.detail_total = QtWidgets.QLineEdit()
        self.detail_status = QtWidgets.QComboBox()
        self.detail_status.addItems([
            "Lunas", 
            "Belum Lunas", 
            "Kurang", 
            "Pending", 
            "Cancelled", 
            "Completed"
        ])
        
        self.detail_layout.addRow("ID Transaksi:", self.detail_id)
        self.detail_layout.addRow("Total Pembayaran:", self.detail_total)
        self.detail_layout.addRow("Status:", self.detail_status)
        
        self.detail_group.setLayout(self.detail_layout)
        
        # Action buttons
        self.button_layout = QtWidgets.QHBoxLayout()
        self.update_button = QtWidgets.QPushButton("Update Status")
        self.update_button.setStyleSheet("background-color: rgb(212, 17, 30); color: white;")
        self.kembali_button = QtWidgets.QPushButton("Kembali")
        self.kembali_button.setStyleSheet("background-color: rgb(212, 17, 30); color: white;")
        
        self.button_layout.addWidget(self.update_button)
        self.button_layout.addWidget(self.kembali_button)
        
        # Assembling left layout
        self.left_layout.addWidget(self.label_title)
        self.left_layout.addWidget(self.transaction_list)
        self.left_layout.addWidget(self.detail_group)
        self.left_layout.addLayout(self.button_layout)
        
        # Add left layout to main layout
        self.main_layout.addLayout(self.left_layout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Connect signals
        self.transaction_list.clicked.connect(self.show_transaction_details)
        self.update_button.clicked.connect(self.update_transaction_status)
        self.kembali_button.clicked.connect(self.back_to_menu)
        
        # Load initial data
        self.load_transactions()

    def load_transactions(self):
        try:
            connection = mysql.connector.connect(
                host="localhost", user="root", password="", database="uas"
            )
            cursor = connection.cursor()
            
            query = """
            SELECT 
                pm.id_transaksi, 
                u.nama, 
                pm.total_pembayaran, 
                pm.status 
            FROM pembayaran pm
            JOIN user u ON pm.id_user = u.id
            """
            cursor.execute(query)
            
            # Clear existing model
            self.transaction_model.removeRows(0, self.transaction_model.rowCount())
            
            for row in cursor.fetchall():
                items = [QStandardItem(str(val)) for val in row]
                self.transaction_model.appendRow(items)
                
        except mysql.connector.Error as e:
            QMessageBox.critical(None, "Error", str(e))
        finally:
            if connection:
                connection.close()

    def show_transaction_details(self, index):
        row = index.row()
        transaction_id = self.transaction_model.item(row, 0).text()
        total_payment = self.transaction_model.item(row, 2).text()
        current_status = self.transaction_model.item(row, 3).text()
        
        self.detail_id.setText(transaction_id)
        self.detail_total.setText(total_payment)
        
        # Set the status dropdown to match the current status
        status_index = self.detail_status.findText(current_status)
        if status_index >= 0:
            self.detail_status.setCurrentIndex(status_index)

    def update_transaction_status(self):
        transaction_id = self.detail_id.text()
        new_status = self.detail_status.currentText()
        
        try:
            connection = mysql.connector.connect(
                host="localhost", user="root", password="", database="uas"
            )
            cursor = connection.cursor()
            
            query = """
            UPDATE pembayaran
            SET status = %s 
            WHERE id_transaksi = %s
            """
            cursor.execute(query, (new_status, transaction_id))
            connection.commit()
            
            QMessageBox.information(None, "Sukses", "Status berhasil diperbarui")
            
            # Reload transactions
            self.load_transactions()
            
        except mysql.connector.Error as e:
            QMessageBox.critical(None, "Error", str(e))
        finally:
            if connection:
                connection.close()

    def back_to_menu(self):
        from menu_acc import Ui_MainWindow as menu

        self.window = QtWidgets.QMainWindow()
        self.ui = menu()
        self.ui.setupUi(self.window)
        QtWidgets.QApplication.activeWindow().close()
        self.window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())