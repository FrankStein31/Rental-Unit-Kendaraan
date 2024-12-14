# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import menu_admin as mad

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 679)
        MainWindow.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                 "background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton_kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kembali.setGeometry(QtCore.QRect(338, 540, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_kembali.setFont(font)
        self.pushButton_kembali.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(212, 17, 30);")
        self.pushButton_kembali.setObjectName("pushButton_kembali")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(248, 70, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(48, 150, 701, 291))
        self.tableWidget.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        
        # Set table headers
        self.setTableHeaders()

        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(640, 460, 101, 31))
        self.pushButton_refresh.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the refresh button to the refreshTable function
        self.pushButton_refresh.clicked.connect(self.refreshTable)
        
    def setTableHeaders(self):
        headers = ["ID Kendaraan", "Jenis", "Tipe", "Keluaran Tahun", "Warna", "Stok", "Harga Sewa"]
        for col, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem(header)
            self.tableWidget.setHorizontalHeaderItem(col, item)

    def KembaliMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mad.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_kembali.setText(_translate("MainWindow", "Kembali"))
        self.label_4.setText(_translate("MainWindow", "LIHAT MOBIL"))
        self.pushButton_refresh.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_kembali.clicked.connect(self.KembaliMenu)
        self.pushButton_kembali.clicked.connect(MainWindow.close)


    def refreshTable(self):
        try:
            # Connect to MySQL database
            conn = mysql.connector.connect(
                host='localhost',       # Replace with your database host
                user='root',            # Replace with your database username
                password='',            # Replace with your database password
                database='uas'          # Replace with your database name
            )
            
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM mobil")  # Replace with your table name and fields
            rows = cursor.fetchall()
            
            # Clear existing rows before refreshing
            self.tableWidget.setRowCount(0)

            # Populate the table with fetched data
            for row in rows:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                for col, value in enumerate(row):
                    self.tableWidget.setItem(rowPosition, col, QtWidgets.QTableWidgetItem(str(value)))

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            print(f"Error fetching data from MySQL: {e}")
            QtWidgets.QMessageBox.critical(None, "Database Error", "Failed to fetch data from the database.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
