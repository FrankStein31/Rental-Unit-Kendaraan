
import mysql.connector
import menu_admin as mep
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Main Window Setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #F4F7F6;
            }
            QLabel {
                color: #2C3E50;
                font-weight: bold;
            }
            QPushButton {
                background-color: #3498DB;
                color: white;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton#backButton {
                background-color: #E74C3C;
            }
            QPushButton#backButton:hover {
                background-color: #C0392B;
            }
            QTableWidget {
                background-color: white;
                border-radius: 10px;
                gridline-color: #BDC3C7;
            }
            QHeaderView::section {
                background-color: #2980B9;
                color: white;
                padding: 5px;
                border: none;
                font-weight: bold;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Main Layout
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Title
        title_label = QtWidgets.QLabel("Riwayat Rental Admin")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        title_font = QtGui.QFont()
        title_font.setPointSize(22)
        title_font.setBold(True)
        title_label.setFont(title_font)
        main_layout.addWidget(title_label)

        # Table Widget
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        main_layout.addWidget(self.tableWidget)

        # Button Layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(15)

        # Back Button
        self.pushButton_2 = QtWidgets.QPushButton("Kembali")
        self.pushButton_2.setObjectName("backButton")
        
        # Refresh Button
        self.pushButton_3 = QtWidgets.QPushButton("Refresh")
        
        button_layout.addStretch(1)
        button_layout.addWidget(self.pushButton_2)
        button_layout.addWidget(self.pushButton_3)
        button_layout.addStretch(1)

        main_layout.addLayout(button_layout)

        # Connect Signals
        self.pushButton_2.clicked.connect(self.KembaliMenu)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.refreshData)

        # Initial data refresh
        QtCore.QTimer.singleShot(100, self.refreshData)

    def KembaliMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mep.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "RIWAYAT RENTAL"))
        self.pushButton_2.setText(_translate("MainWindow", "Kembali"))
        self.pushButton_3.setText(_translate("MainWindow", "Refresh"))

    def refreshData(self):
        # Database Connection
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="uas"
        )
        cursor = db_connection.cursor()

        # Clear existing table rows
        self.tableWidget.setRowCount(0)

        # Enhanced SQL Query with exact column names
        cursor.execute("""
            SELECT 
                p.id_transaksi, 
                m.jenis_mbl AS jenis_unit, 
                p.harga_sewa_mobil AS harga_sewa, 
                p.tanggal_pinjam, 
                p.tanggal_kembali, 
                p.driver, 
                pmobil.status AS status_pembayaran,
                u.nama AS nama_penyewa
            FROM pinjam p
            LEFT JOIN pembayaran pmobil ON p.id_transaksi = pmobil.id_transaksi
            LEFT JOIN mobil m ON p.id_mobil = m.id_mbl
            LEFT JOIN user u ON p.id_user = u.id
            
            UNION
            
            SELECT 
                pm.id_transaksi_motor, 
                mo.jenis_mtr AS jenis_unit, 
                pm.harga_sewa_motor AS harga_sewa, 
                pm.tanggal_pinjam, 
                pm.tanggal_kembali, 
                pm.driver, 
                pmotor.status AS status_pembayaran,
                u.nama AS nama_penyewa
            FROM pinjam_motor pm
            LEFT JOIN pembayaran_motor pmotor ON pm.id_transaksi_motor = pmotor.id_transaksi_motor
            LEFT JOIN motor mo ON pm.id_motor = mo.id_mtr
            LEFT JOIN user u ON pm.id_user = u.id
            
            UNION
            
            SELECT 
                pe.id_transaksi_elf, 
                e.jenis_elf AS jenis_unit, 
                pe.harga_sewa_elf AS harga_sewa, 
                pe.tanggal_pinjam, 
                pe.tanggal_kembali, 
                pe.driver, 
                pelf.status AS status_pembayaran,
                u.nama AS nama_penyewa
            FROM pinjam_elf pe
            LEFT JOIN pembayaran_elf pelf ON pe.id_transaksi_elf = pelf.id_transaksi_elf
            LEFT JOIN elf e ON pe.id_elf = e.id_elf
            LEFT JOIN user u ON pe.id_user = u.id
            ORDER BY tanggal_pinjam DESC
        """)

        rows = cursor.fetchall()

        # Set table properties
        self.tableWidget.setColumnCount(8)
        headers = [
            "ID Transaksi", "Jenis Unit", "Harga Sewa", 
            "Tanggal Pinjam", "Tanggal Kembali", "Driver", 
            "Status Pembayaran", "Nama Penyewa"
        ]
        self.tableWidget.setHorizontalHeaderLabels(headers)
        
        # Populate table with color-coded status
        for row in rows:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            
            for col, data in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(data) if data is not None else "")
                
                # Color-code payment status
                if col == 6:  # Status column
                    status = str(data).lower() if data is not None else ""
                    if status == 'lunas':
                        item.setBackground(QtGui.QColor(200, 255, 200))  # Light Green
                    elif status == 'belum lunas':
                        item.setBackground(QtGui.QColor(255, 200, 200))  # Light Red
                    elif status == 'pending':
                        item.setBackground(QtGui.QColor(255, 255, 200))  # Light Yellow
                
                self.tableWidget.setItem(rowPosition, col, item)

        # Adjust column widths
        self.tableWidget.resizeColumnsToContents()

        # Close database connection
        cursor.close()
        db_connection.close()

if __name__ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())