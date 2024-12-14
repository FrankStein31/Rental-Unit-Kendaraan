# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mobil1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import menu_penyewa as mep
import mysql.connector
import sewa_mbl as se

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_id=None):

        self.user_id = user_id
        print("Ini id user dari HALAMAN PILIH MOBIL", user_id)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 230, 281, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"background-color: rgb(255, 202, 111);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 131, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 520, 93, 28))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 17, 30);")
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 200, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 300, 93, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(6, 131, 35);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 160, 281, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"background-color: rgb(255, 202, 111);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 230, 281, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"background-color: rgb(255, 202, 111);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 140, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 160, 281, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(430, 440, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(340, 200, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 270, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 130, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 300, 151, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"background-color: rgb(255, 202, 111);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 80, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 390, 141, 121))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(340, 300, 411, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"background-color: rgb(255, 202, 111);")
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
        self.pushButton.clicked.connect(self.KembaliMenu)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.Pinjam)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.cari_mobil)
        self.pushButton_3.clicked.connect(self.cari_mobil_ke_lineEdit)
    

    def KembaliMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mep.Ui_MainWindow()
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()

    def Pinjam(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = se.Ui_MainWindow()
        self.ui.setupUi(self.window)
        id_mobil = self.lineEdit.text()  # Mendapatkan ID yang dimasukkan
        print(f"id_mobil yang dikirim: {id_mobil}")  # Debug untuk memastikan ID yang dikirim
        self.ui.setupUi(self.window, id_mobil, self.user_id)
        self.window.show()

    def cari_mobil(self):
        try:
            # Get the ID entered by the user (assumed to be in a QLineEdit widget)
            id_mbl = self.lineEdit.text()  # Replace 'id_input' with your QLineEdit widget name

            # Connect to MySQL database
            conn = mysql.connector.connect(
                host='localhost',  # Adjust with your MySQL host
                user='root',  # Adjust with your MySQL user
                password='',  # Adjust with your MySQL password
                database='uas'  # Replace with your database name
            )
            cursor = conn.cursor()

            # Query to get data based on the entered id_mbl
            query = "SELECT * FROM mobil WHERE id_mbl = %s"  # Use parameterized query to avoid SQL injection
            cursor.execute(query, (id_mbl,))
            result = cursor.fetchall()

            # Check if the table has columns and insert them into tableWidget
            if result:
                # Set the number of columns based on the data from the query
                columns = [desc[0] for desc in cursor.description]  # Get column names
                self.tableWidget.setColumnCount(len(columns))  # Set column count based on number of columns
                self.tableWidget.setHorizontalHeaderLabels(columns)  # Set header labels

                # Insert data into the tableWidget
                self.tableWidget.setRowCount(0)  # Clear existing rows
                for row in result:
                    row_position = self.tableWidget.rowCount()  # Get current row count
                    self.tableWidget.insertRow(row_position)  # Insert a new row
                    for column, data in enumerate(row):
                        self.tableWidget.setItem(row_position, column, QtWidgets.QTableWidgetItem(str(data)))
            else:
                print("No data available for the entered ID.")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def cari_mobil_ke_lineEdit(self):
        try:
            # Get the ID entered by the user
            id_mbl = self.lineEdit.text()  # Replace 'lineEdit' with the QLineEdit widget for entering the ID

            # Connect to MySQL database
            conn = mysql.connector.connect(
                host='localhost',  # Adjust with your MySQL host
                user='root',  # Adjust with your MySQL user
                password='',  # Adjust with your MySQL password
                database='uas'  # Replace with your database name
            )
            cursor = conn.cursor()

            # Query to get data based on the entered id_mbl
            query = "SELECT * FROM mobil WHERE id_mbl = %s"  # Use parameterized query to avoid SQL injection
            cursor.execute(query, (id_mbl,))
            result = cursor.fetchone()

            if result:
                # Map the result to corresponding lineEdits
                self.lineEdit_2.setText(str(result[1]))  # Replace index with the column position
                self.lineEdit_3.setText(str(result[2]))
                self.lineEdit_4.setText(str(result[3]))
                self.lineEdit_5.setText(str(result[4]))
                self.lineEdit_6.setText(str(result[5]))
                # Continue for additional columns as needed
            else:
                print("No data found for the entered ID.")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Data Mobil yang Tersedia"))
        self.pushButton.setText(_translate("MainWindow", "Kembali"))
        self.label_8.setText(_translate("MainWindow", "Tahun Mobil :"))
        self.label_10.setText(_translate("MainWindow", "Image Mobil :"))
        self.label_5.setText(_translate("MainWindow", "ID :"))
        self.pushButton_2.setText(_translate("MainWindow", "Pinjam"))
        self.label_6.setText(_translate("MainWindow", "Jenis Mobil :"))
        self.label_9.setText(_translate("MainWindow", "Warna Mobil :"))
        self.label_12.setText(_translate("MainWindow", "Stok Mobil :"))
        self.label_7.setText(_translate("MainWindow", "Type Mobil :"))
        self.pushButton_3.setText(_translate("MainWindow", "Mobil"))
        self.label_2.setText(_translate("MainWindow", "image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
