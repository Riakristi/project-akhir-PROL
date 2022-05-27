from cmath import log
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from layout.tampilan_awal import Ui_Form as tampilan_awal
from layout.login_admin import Ui_Admin as login_admin
from layout.menu_admin import Ui_Form as menu_admin
from layout.list_cup import Ui_Form as list_cup
from layout.pilihan import Ui_Form as pilihan_menu

class tampilanAwal(tampilan_awal):
    def __init__(self, dialog):
        tampilan_awal.__init__(self)
        self.setupUi(dialog)
        self.pushButtonLogin.setIcon(QtGui.QIcon('img/user.png'))

        self.pushButtonLogin.clicked.connect(self.admin)
        self.pushButtonPesan.clicked.connect(self.input_nama)

    def admin(self):
        tampilanAwalWindow.close()

        self.loginAdminWindow = QtWidgets.QWidget()
        self.loginAdminUi = login_admin()
        self.loginAdminUi.setupUi(self.loginAdminWindow)
        self.loginAdminWindow.show()

        self.loginAdminUi.pushButtonLogin.clicked.connect(self.login)

    def login(self):
        '''fungsi buat login di menu admin'''
        username = self.loginAdminUi.lineEditUsername.text()
        password = self.loginAdminUi.lineEditPassword.text()
        if(username == "admin" and password == "1234"):
            self.loginAdminUi.labelWarning.setText("Login berhasil!")
            self.loginAdminUi.labelWarning.show()
            
            self.adminWindow = QtWidgets.QWidget()
            self.adminWindowUi = menu_admin()
            self.adminWindowUi.setupUi(self.adminWindow)
            self.loginAdminWindow.hide()
            self.adminWindow.show()
        
        else:
            self.loginAdminUi.labelWarning.setText("Login gagal. Coba lagi!")
            self.loginAdminUi.labelWarning.show()

    def input_nama(self):
        nama = self.lineEditNama.text()

        self.listcup = QtWidgets.QDialog()
        self.listcupUi = list_cup()
        self.listcupUi.setupUi(self.listcup)
        tampilanAwalWindow.hide()
        self.listcup.show()

        self.listcupUi.label_smallcup.setPixmap(QtGui.QPixmap('img/small.png'))
        self.listcupUi.label_mediumcup.setPixmap(QtGui.QPixmap('img/medium.png'))
        self.listcupUi.label_largecup.setPixmap(QtGui.QPixmap('img/large.png'))

        self.listcupUi.pushButtonNext.clicked.connect(self.pilihan)

    def pilihan(self):
        self.pilihanmenu = QtWidgets.QDialog()
        self.pilihanmenuUi = pilihan_menu()
        self.pilihanmenuUi.setupUi(self.pilihanmenu)
        self.listcup.hide()
        self.pilihanmenu.show()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tampilanAwalWindow = QtWidgets.QWidget()
    tampilanAwalUi = tampilanAwal(tampilanAwalWindow)
    tampilanAwalWindow.show()

    sys.exit(app.exec_())