from PyQt5 import QtCore, QtGui, QtWidgets
import menu_admin as mad
import unit_motor as mtr
import unit_mobil as mbl
import unit_elf as elf

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(24, 121, 202, 255), 
                    stop:1 rgba(41, 179, 250, 255));
            }
            QLabel {
                color: white;
                font-weight: bold;
            }
            QPushButton {
                background-color: rgba(255, 170, 0, 230);
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: rgba(255, 170, 0, 255);
            }
            QPushButton#pushButton_keluar {
                background-color: rgba(212, 17, 30, 230);
            }
            QPushButton#pushButton_keluar:hover {
                background-color: rgba(212, 17, 30, 255);
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main layout
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(50, 30, 50, 30)
        
        # Title
        self.label_4 = QtWidgets.QLabel("KELOLA UNIT")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_4.setFont(font)
        main_layout.addWidget(self.label_4)
        main_layout.addSpacing(20)
        
        # Content Layout
        content_layout = QtWidgets.QVBoxLayout()
        
        # First row of images and buttons
        first_row = QtWidgets.QHBoxLayout()
        
        # Motor Section
        motor_layout = QtWidgets.QVBoxLayout()
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setPixmap(QtGui.QPixmap("../../../Downloads/th (2).jpeg").scaled(250, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        motor_layout.addWidget(self.label_2)
        
        self.pushButton = QtWidgets.QPushButton("Pilih Motor")
        self.pushButton.setFixedSize(200, 50)
        motor_layout.addWidget(self.pushButton, alignment=QtCore.Qt.AlignCenter)
        first_row.addLayout(motor_layout)
        
        # Mobil Section
        mobil_layout = QtWidgets.QVBoxLayout()
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setPixmap(QtGui.QPixmap("../../../Downloads/th (3).jpeg").scaled(250, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        mobil_layout.addWidget(self.label_3)
        
        self.pushButton_2 = QtWidgets.QPushButton("Pilih Mobil")
        self.pushButton_2.setFixedSize(200, 50)
        mobil_layout.addWidget(self.pushButton_2, alignment=QtCore.Qt.AlignCenter)
        first_row.addLayout(mobil_layout)
        
        content_layout.addLayout(first_row)
        main_layout.addLayout(content_layout)
        
        # Elf Section
        elf_layout = QtWidgets.QVBoxLayout()
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setPixmap(QtGui.QPixmap("../../../Downloads/th (4).jpg").scaled(250, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        elf_layout.addWidget(self.label_5)
        
        self.pushButton_3 = QtWidgets.QPushButton("Pilih Elf")
        self.pushButton_3.setFixedSize(200, 50)
        elf_layout.addWidget(self.pushButton_3, alignment=QtCore.Qt.AlignCenter)
        
        main_layout.addLayout(elf_layout)
        main_layout.addStretch()
        
        # Bottom Buttons
        bottom_buttons = QtWidgets.QHBoxLayout()
        self.pushButton_keluar = QtWidgets.QPushButton("Kembali")
        self.pushButton_keluar.setObjectName("pushButton_keluar")
        self.pushButton_keluar.setFixedSize(150, 50)
        
        bottom_buttons.addWidget(self.pushButton_keluar)
        
        main_layout.addLayout(bottom_buttons)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons
        self.pushButton_keluar.clicked.connect(self.KembaliMenu)
        self.pushButton_keluar.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.Motor)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.Mobil)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.Elf)
        self.pushButton_3.clicked.connect(MainWindow.close)

    def Motor(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mtr.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Mobil(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mbl.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Elf(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = elf.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def KembaliMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mad.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kelola Unit - Rental Jaya"))
        self.label_4.setText(_translate("MainWindow", "KELOLA UNIT"))
        self.pushButton_3.setText(_translate("MainWindow", "Pilih Elf"))
        self.pushButton_2.setText(_translate("MainWindow", "Pilih Mobil"))
        self.pushButton.setText(_translate("MainWindow", "Pilih Motor"))
        self.pushButton_keluar.setText(_translate("MainWindow", "Kembali"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())