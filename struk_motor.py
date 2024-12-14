from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QDialog
import menu_struk as st

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_id=None):
        self.user_id = user_id
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)  # Increased window size
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main layout
        main_layout = QVBoxLayout(self.centralwidget)
        
        # Header Section
        header_layout = QtWidgets.QHBoxLayout()
        self.kembali = QtWidgets.QPushButton("KEMBALI")
        self.kembali.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(212, 17, 30); padding: 10px;")
        header_layout.addWidget(self.kembali)
        
        header_label = QtWidgets.QLabel("Struk Transaksi Motor")
        header_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        header_label.setAlignment(QtCore.Qt.AlignCenter)
        header_layout.addWidget(header_label)
        
        # Spacer to balance the layout
        header_layout.addSpacing(100)
        
        main_layout.addLayout(header_layout)
                
        # Table for Transactions
        self.transaction_table = QTableWidget()
        self.transaction_table.setColumnCount(6)
        self.transaction_table.setHorizontalHeaderLabels(["ID", "Jenis Motor", "Tipe Motor", "Tahun", "Warna", "Total Pembayaran"])
        self.transaction_table.setStyleSheet("background-color: white;")
        self.transaction_table.horizontalHeader().setStretchLastSection(True)
        
        main_layout.addWidget(self.transaction_table)
        
        # Buttons Section
        button_layout = QtWidgets.QHBoxLayout()
        self.pushButton_detail = QtWidgets.QPushButton("Detail Transaksi")
        self.pushButton_detail.setStyleSheet("background-color: rgb(6, 131, 35); color: white; padding: 10px;")
        
        button_layout.addSpacing(50)
        button_layout.addWidget(self.pushButton_detail)
        button_layout.addSpacing(50)
        
        main_layout.addLayout(button_layout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Connect signals
        # self.cari.clicked.connect(self.search_data)
        self.pushButton_detail.clicked.connect(self.show_transaction_detail)
        self.kembali.clicked.connect(self.Struk)
        self.kembali.clicked.connect(MainWindow.close)
        
        # Connect double-click on table to show details
        self.transaction_table.doubleClicked.connect(self.show_transaction_detail)
        self.load_all_transactions()

    def Struk(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = st.Ui_MainWindow()
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()

    def load_all_transactions(self):
        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="uas"
            )
            cursor = conn.cursor()

            # Query to fetch all transactions for the specific user
            query = """
                SELECT DISTINCT m.id_mtr, m.jenis_mtr, m.type_mtr, m.tahun_mtr, m.warna_mtr, pm.total_pembayaran
                FROM motor m
                JOIN pinjam_motor p ON m.id_mtr = p.id_motor
                JOIN pembayaran_motor pm ON p.id_transaksi_motor = pm.id_transaksi_motor
                WHERE p.id_user = %s
            """
            cursor.execute(query, (self.user_id,))
            results = cursor.fetchall()

            # Clear existing table
            self.transaction_table.setRowCount(0)

            # Populate table
            for row_data in results:
                row_position = self.transaction_table.rowCount()
                self.transaction_table.insertRow(row_position)
                for i, value in enumerate(row_data):
                    self.transaction_table.setItem(row_position, i, QTableWidgetItem(str(value)))

            if not results:
                QtWidgets.QMessageBox.warning(
                    None, "Data Not Found", "Tidak ada transaksi ditemukan.")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(
                None, "Database Error", f"Terjadi kesalahan: {err}")

    def show_transaction_detail(self):
        # Get selected row
        current_row = self.transaction_table.currentRow()
        if current_row < 0:
            QtWidgets.QMessageBox.warning(None, "Peringatan", "Pilih transaksi terlebih dahulu")
            return

        # Extract data from selected row
        details = []
        for col in range(self.transaction_table.columnCount()):
            item = self.transaction_table.item(current_row, col)
            details.append(item.text() if item else "")

        # Create detailed message
        data_message = f"""
        ID Motor: {details[0]}
        Jenis Motor: {details[1]}
        Tipe Motor: {details[2]}
        Tahun Motor: {details[3]}
        Warna Motor: {details[4]}
        Total Pembayaran: Rp. {details[5]}
        """

        # Show detailed dialog
        detail_dialog = QDialog()
        detail_dialog.setWindowTitle("Detail Transaksi")
        detail_dialog.setStyleSheet("background-color: rgb(24, 121, 202); color: white;")
        
        layout = QVBoxLayout()
        
        # Detail label
        detail_label = QtWidgets.QLabel(data_message)
        detail_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(detail_label)
        
        # OK button
        ok_button = QtWidgets.QPushButton("OK")
        ok_button.setStyleSheet("background-color: rgb(6, 131, 35); color: white;")
        ok_button.clicked.connect(detail_dialog.accept)
        layout.addWidget(ok_button)
        
        detail_dialog.setLayout(layout)
        detail_dialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())