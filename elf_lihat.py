from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, QHeaderView, QAbstractItemView
import mysql.connector
import menu_admin as mad
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)  # Increased size for better visibility
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #1479CA;
            }
            QLabel {
                color: white;
                font-size: 12px;
            }
            QTableWidget {
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
            QPushButton#pushButton_kembali {
                background-color: #F44336;
                color: white;
            }
            QPushButton#pushButton_kembali:hover {
                background-color: #D32F2F;
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Main Layout
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title_label = QtWidgets.QLabel("DAFTAR ELF")
        title_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold; align: center;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Table Widget
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        headers = ["ID Kendaraan", "Jenis", "Tipe", "Keluaran Tahun", "Warna", "Stok", "Harga Sewa", "Foto"]
        self.tableWidget.setHorizontalHeaderLabels(headers)
        
        layout.addWidget(self.tableWidget)
        
        # Button Layout
        button_layout = QtWidgets.QHBoxLayout()
        self.pushButton_refresh = QtWidgets.QPushButton("Refresh")
        self.pushButton_kembali = QtWidgets.QPushButton("Kembali")
        
        button_layout.addWidget(self.pushButton_refresh)
        button_layout.addWidget(self.pushButton_kembali)
        
        layout.addLayout(button_layout)
        
        # Connect buttons
        self.pushButton_refresh.clicked.connect(self.refreshTable)
        self.pushButton_kembali.clicked.connect(self.KembaliMenu)
        
        # Initially populate the table
        self.refreshTable()

    def KembaliMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mad.Ui_MainWindow()
        self.ui.setupUi(self.window)
        QtWidgets.QApplication.activeWindow().close()
        self.window.show()

    def refreshTable(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='uas'
            )
            cursor = connection.cursor()
            query = "SELECT * FROM elf"
            cursor.execute(query)
            result = cursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_data in result:
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                
                # Add text data
                for col in range(7):
                    item = QtWidgets.QTableWidgetItem(str(row_data[col]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(row_position, col, item)
                
                # Add photo
                photo_widget = QtWidgets.QLabel()
                photo_widget.setAlignment(QtCore.Qt.AlignCenter)
                
                if row_data[8]:  # Check if photo path exists
                    photo_path = row_data[8]
                    if os.path.exists(photo_path):
                        pixmap = QPixmap(photo_path)
                        scaled_pixmap = pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                        photo_widget.setPixmap(scaled_pixmap)
                    else:
                        photo_widget.setText("Foto Tidak Tersedia")
                else:
                    photo_widget.setText("Foto Tidak Tersedia")
                
                self.tableWidget.setCellWidget(row_position, 7, photo_widget)

        except mysql.connector.Error as e:
            QMessageBox.warning(None, "Database Error", str(e))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())