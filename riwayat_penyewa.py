from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import menu_penyewa as mep

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 100, 701, 291))
        self.tableWidget.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)  # Update the column count
        self.tableWidget.setRowCount(0)
        
        # Set column headers
        self.tableWidget.setHorizontalHeaderLabels([
            "ID Transaksi", "ID Kendaraan", "Harga Sewa", "Tgl Pinjam", "Tgl Kembali", "Driver"
        ])

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 490, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 17, 30);")
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 400, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.KembaliMenu)
        self.pushButton_2.clicked.connect(MainWindow.close)

        # Connect refresh button to fetch data
        self.pushButton_3.clicked.connect(self.refreshData)

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
        # Connect to MySQL Database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="uas"  # Replace with your database name
        )
        cursor = db_connection.cursor()

        # Clear the table before refreshing
        self.tableWidget.setRowCount(0)

        # Fetch data from pinjam, pinjam_motor, and pinjam_elf tables with status from pembayaran tables
        cursor.execute("""
            SELECT 
                p.id_transaksi, 
                m.jenis_mbl AS jenis_unit, 
                p.harga_sewa_mobil AS harga_sewa, 
                p.tanggal_pinjam, 
                p.tanggal_kembali, 
                p.driver, 
                pmobil.status AS status_pembayaran
            FROM pinjam p
            LEFT JOIN pembayaran pmobil ON p.id_transaksi = pmobil.id_transaksi
            LEFT JOIN mobil m ON p.id_transaksi = m.id_mbl
            UNION
            SELECT 
                pm.id_transaksi_motor, 
                mo.jenis_mtr AS jenis_unit, 
                pm.harga_sewa_motor AS harga_sewa, 
                pm.tanggal_pinjam, 
                pm.tanggal_kembali, 
                pm.driver, 
                pmotor.status AS status_pembayaran
            FROM pinjam_motor pm
            LEFT JOIN pembayaran_motor pmotor ON pm.id_transaksi_motor = pmotor.id_transaksi_motor
            LEFT JOIN motor mo ON pm.id_transaksi_motor = mo.id_mtr
            UNION
            SELECT 
                pe.id_transaksi_elf, 
                e.jenis_elf AS jenis_unit, 
                pe.harga_sewa_elf AS harga_sewa, 
                pe.tanggal_pinjam, 
                pe.tanggal_kembali, 
                pe.driver, 
                pelf.status AS status_pembayaran
            FROM pinjam_elf pe
            LEFT JOIN pembayaran_elf pelf ON pe.id_transaksi_elf = pelf.id_transaksi_elf
            LEFT JOIN elf e ON pe.id_transaksi_elf = e.id_elf
        """)

        # Fetch data and print for debugging
        rows = cursor.fetchall()
        print(f"Rows fetched: {rows}")

        # Check if rows exist
        if not rows:
            print("No data found!")
            return

        # Set table column count and headers
        self.tableWidget.setColumnCount(7)  # Ensure this matches the number of columns in your SQL query
        self.tableWidget.setHorizontalHeaderLabels([
            "ID Transaksi", "Merk Unit", "Harga Sewa", 
            "Tanggal Pinjam", "Tanggal Kembali", "Driver", "Status Pembayaran"
        ])

        # Populate the table with fetched data
        for row in rows:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            for col, data in enumerate(row):
                self.tableWidget.setItem(rowPosition, col, QtWidgets.QTableWidgetItem(str(data) if data is not None else ""))

        # Close the database connection
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