# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mobil_edit as E
import mobil_hapus as H
import mobil_tambah as T
import mobil_lihat as L

# Color Palette
BACKGROUND_COLOR = "rgb(55, 71, 79)"    # Dark Blue-Grey
BUTTON_COLOR = "rgb(84, 110, 122)"      # Muted Blue-Grey
ACCENT_COLOR = "rgb(120, 144, 156)"     # Soft Blue-Grey
TEXT_COLOR = "rgb(224, 224, 224)"       # Light Grey
HOVER_COLOR = "rgb(69, 90, 100)"        # Darker Blue-Grey

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(f"""
            QMainWindow {{
                background-color: {BACKGROUND_COLOR};
            }}
            QPushButton {{
                background-color: {BUTTON_COLOR};
                color: {TEXT_COLOR};
                border: none;
                padding: 12px;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                margin: 10px 0;
                transition: all 0.3s ease;
            }}
            QPushButton:hover {{
                background-color: {ACCENT_COLOR};
                transform: scale(1.05);
            }}
            QPushButton:pressed {{
                background-color: {HOVER_COLOR};
                transform: scale(0.95);
            }}
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main Vertical Layout
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(60, 40, 60, 40)
        main_layout.setSpacing(30)
        
        # Elegant Title
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 2)
        self.label.setFont(font)
        self.label.setStyleSheet(f"color: {TEXT_COLOR}; letter-spacing: 2px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.label)
        
        # Button Container
        button_container = QtWidgets.QVBoxLayout()
        button_container.setSpacing(20)
        
        # Buttons Configuration
        buttons_info = [
            ("pushButton_tambahkendaraan", "Tambah Kendaraan Mobil", self.Tambah),
            ("pushButton_perbaruikendaraan", "Perbarui Kendaraan Mobil", self.Edit),
            ("pushButton_hapuskendaraan", "Hapus Kendaraan Mobil", self.Hapusl),
            ("pushButton_reset", "Lihat Kendaraan Mobil", self.Lihat)
        ]
        
        for name, text, connection in buttons_info:
            button = QtWidgets.QPushButton(self.centralwidget)
            button.setObjectName(name)
            button.setText(text)
            button.clicked.connect(connection)
            button.clicked.connect(MainWindow.close)
            button_container.addWidget(button)
        
        main_layout.addLayout(button_container)
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Minimal Menu and Status Bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Edit(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = E.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Hapusl(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = H.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Tambah(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = T.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Lihat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = L.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manajemen Kendaraan Mobil"))
        self.label.setText(_translate("MainWindow", "KELOLA MOBIL"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())