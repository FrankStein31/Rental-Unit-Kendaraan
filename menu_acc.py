from PyQt5 import QtCore, QtGui, QtWidgets
import accpembayaran_motor as mtr
import accpembayaran_mobil as mbl
import accpembayaran_elf as elf
import menu_admin as mad

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #2C3E50, 
                    stop:1 #34495E
                );
            }
            QPushButton {
                background-color: #3498DB;
                color: white;
                border-radius: 10px;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
                transition: all 0.3s ease;
            }
            QPushButton:hover {
                background-color: #2980B9;
                transform: scale(1.05);
            }
            QPushButton:pressed {
                background-color: #21618C;
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create a vertical layout for the central widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout.setSpacing(20)
        
        # Title Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setWeight(75)
        font.setFamily("Segoe UI")
        self.label.setFont(font)
        self.label.setStyleSheet("""
            color: white;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 15px;
        """)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        
        # Buttons Container
        self.buttonsWidget = QtWidgets.QWidget(self.centralwidget)
        self.buttonsLayout = QtWidgets.QVBoxLayout(self.buttonsWidget)
        self.buttonsLayout.setSpacing(15)
        
        # Vehicle Type Buttons
        self.pushButton_motor = self.createStyledButton("Motor")
        self.pushButton_mobil = self.createStyledButton("Mobil")
        self.pushButton_elf = self.createStyledButton("Elf")
        
        self.buttonsLayout.addWidget(self.pushButton_motor)
        self.buttonsLayout.addWidget(self.pushButton_mobil)
        self.buttonsLayout.addWidget(self.pushButton_elf)
        
        self.verticalLayout.addWidget(self.buttonsWidget)
        
        # Exit Button
        self.pushButton_keluar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_keluar.setStyleSheet("""
            background-color: #E74C3C;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 12px;
        """)
        self.pushButton_keluar.setObjectName("pushButton_keluar")
        self.verticalLayout.addWidget(self.pushButton_keluar)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Connect signals
        self.pushButton_motor.clicked.connect(self.AccMtr)
        self.pushButton_motor.clicked.connect(MainWindow.close)
        self.pushButton_mobil.clicked.connect(self.AccMbl)
        self.pushButton_mobil.clicked.connect(MainWindow.close)
        self.pushButton_elf.clicked.connect(self.AccElf)
        self.pushButton_elf.clicked.connect(MainWindow.close)
        self.pushButton_keluar.clicked.connect(self.Kembali)
        self.pushButton_keluar.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def createStyledButton(self, text):
        button = QtWidgets.QPushButton()
        button.setText(text)
        button.setMinimumHeight(50)
        return button

    def AccMtr(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mtr.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def AccMbl(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mbl.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def AccElf(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = elf.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Kembali(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mad.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ACC Pembayaran Kendaraan"))
        self.pushButton_mobil.setText(_translate("MainWindow", "Mobil"))
        self.pushButton_elf.setText(_translate("MainWindow", "Elf"))
        self.pushButton_motor.setText(_translate("MainWindow", "Motor"))
        self.label.setText(_translate("MainWindow", "ACC PEMBAYARAN KENDARAAN"))
        self.pushButton_keluar.setText(_translate("MainWindow", "Kembali"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())