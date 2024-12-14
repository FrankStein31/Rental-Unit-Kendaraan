from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import pilih_elf as mbl
import pembayaran_elf as bayar
import mysql.connector

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,elf_id=None, user_id=None):

        self.user_id = user_id
        print("Ini id user dari HALAMAN SEWA ELF", user_id)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 602)
        MainWindow.setStyleSheet("background-color: rgb(24, 121, 202);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 150, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 290, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_sewaperhari = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sewaperhari.setGeometry(QtCore.QRect(120, 190, 561, 31))
        self.lineEdit_sewaperhari.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.lineEdit_sewaperhari.setObjectName("lineEdit_sewaperhari")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 370, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kembali.setGeometry(QtCore.QRect(70, 490, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_kembali.setFont(font)
        self.pushButton_kembali.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(212, 17, 30);")
        self.pushButton_kembali.setObjectName("pushButton_kembali")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 220, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 260, 561, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 100, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_pinjam = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pinjam.setGeometry(QtCore.QRect(400, 100, 101, 41))
        self.pushButton_pinjam.setObjectName("pushButton_3")
        self.pushButton_pinjam.setStyleSheet("background-color: rgb(6, 131, 35);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(120, 100, 131, 41))
        self.lineEdit_id.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 80, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.dateEdit_pinjam = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_pinjam.setGeometry(QtCore.QRect(120, 330, 561, 31))
        self.dateEdit_pinjam.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.dateEdit_pinjam.setObjectName("dateEdit_pinjam")
        self.dateEdit_kembali = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_kembali.setGeometry(QtCore.QRect(120, 410, 561, 31))
        self.dateEdit_kembali.setStyleSheet("background-color: rgb(255, 202, 111);")
        self.dateEdit_kembali.setObjectName("dateEdit_kembali")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        if elf_id is not None:
            self.set_elf_id(elf_id)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_pinjam.clicked.connect(self.Bayar)
        self.pushButton_pinjam.clicked.connect(self.simpan_data)
        self.pushButton_pinjam.clicked.connect(MainWindow.close)
        self.pushButton_kembali.clicked.connect(self.Kembali)
        self.pushButton_kembali.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.cari_elf)

        self.comboBox.addItems(['ya', 'tidak'])



    def set_elf_id(self, elf_id):
        """Menerima ID elf dari window sebelumnya dan mengisinya ke lineEdit_id"""
        print(f"elf ID diterima: {elf_id}")  # Menampilkan ID yang diterima untuk debugging
        self.lineEdit_id.setText(elf_id)  


    def Kembali(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mbl.Ui_MainWindow()
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()

    def Bayar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = bayar.Ui_MainWindow()
        self.ui.setupUi(self.window, self.user_id)
        self.window.show()


    def cari_elf(self):
        try:
            # Get the id_mbl entered by the user
            id_mbl = int(self.lineEdit_id.text())  # Input dari user (pastikan tipe data sesuai)

            # Connect to MySQL database
            conn = mysql.connector.connect(
                host='localhost',  # Adjust with your MySQL host
                user='root',  # Adjust with your MySQL user
                password='',  # Adjust with your MySQL password
                database='uas'  # Replace with your database name
            )
            cursor = conn.cursor()

            # Query to get harga_sewa_mbl and driver based on the entered id_mbl
            query = "SELECT harga_sewa_elf, driver FROM elf WHERE id_elf = %s"  # Query dengan 2 kolom
            cursor.execute(query, (id_mbl,))
            result = cursor.fetchone()

            if result:
                # Map the result to corresponding QLineEdit widgets
                self.lineEdit_sewaperhari.setText(str(result[0]))  # harga_sewa_mbl
                self.comboBox.setCurrentText(result[1])  # driver (ya/tidak)
            else:
                # Display a message if no data is found
                print("No data found for the entered id_mbl.")

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print(f"Database error: {err}")
        except ValueError:
            print("Invalid input: id_elf should be a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def simpan_data(self):
        try:
            # Ambil nilai yang dimasukkan oleh pengguna
            id_user = self.user_id
            tanggal_pinjam = self.dateEdit_pinjam.date().toString("yyyy-MM-dd")  # Tanggal pinjam
            tanggal_kembali = self.dateEdit_kembali.date().toString("yyyy-MM-dd")  # Tanggal kembali
            driver = self.comboBox.currentText()  # Pilihan driver (ya/tidak)

            print(f"ID User: {id_user}")
            print(f"Tanggal Pinjam: {tanggal_pinjam}")
            print(f"Tanggal Kembali: {tanggal_kembali}")
            print(f"Driver: {driver}")

            # Connect to MySQL database
            conn = mysql.connector.connect(
                host='localhost',  # Host MySQL
                user='root',  # Username MySQL
                password='',  # Password MySQL
                database='uas'  # Nama database
            )
            cursor = conn.cursor()

            query_elf = """
            SELECT m.id_elf, m.harga_sewa_elf, m.driver, m.stok_elf
            FROM elf m
            WHERE m.stok_elf > 0
            LIMIT 1
            """
            cursor.execute(query_elf)
            elf_result = cursor.fetchone()

            if elf_result:
                id_elf = elf_result[0]  # id_elf
                harga_sewa = elf_result[1]  # harga_sewa_mbl
                driver = elf_result[2]  # driver (ya/tidak)
                stok = elf_result[3]  # stok kendaraan

                if stok > 0:
                    # Query untuk menyimpan data ke dalam tabel pinjam
                    query_insert = """
                    INSERT INTO pinjam_elf (id_elf, id_user, harga_sewa_elf, tanggal_pinjam, tanggal_kembali, driver)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(query_insert, (id_elf, id_user, harga_sewa, tanggal_pinjam, tanggal_kembali, driver))

                    # Update stok kendaraan di tabel elf
                    query_update_stok = """
                    UPDATE elf
                    SET stok_elf = stok_elf - 1
                    WHERE id_elf = %s
                    """
                    cursor.execute(query_update_stok, (id_elf,))

                    conn.commit()  # Commit untuk menyimpan perubahan ke database

                    print("Data berhasil disimpan dan stok kendaraan berhasil dikurangi!")
                else:
                    print("Stok kendaraan tidak mencukupi!")
            else:
                print("Data tidak ditemukan!")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print(f"Database error: {err}")
        except ValueError:
            print("Invalid input: Please check the input values.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Harga Sewa per Hari : "))
        self.label_3.setText(_translate("MainWindow", "Pilih tanggal Pinjam :"))
        self.label_4.setText(_translate("MainWindow", "Pinjam Unit"))
        self.label_5.setText(_translate("MainWindow", "Pilih tanggal Kembali :"))
        self.pushButton_kembali.setText(_translate("MainWindow", "Kembali"))
        self.label_7.setText(_translate("MainWindow", "Tambahan Driver atau Tidak : "))
        self.pushButton_3.setText(_translate("MainWindow", "cari"))
        self.label_8.setText(_translate("MainWindow", "ID :"))
        self.pushButton_pinjam.setText(_translate("MainWindow", "PINJAM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
