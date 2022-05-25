from cmath import log
import sys
from PyQt5 import QtWidgets
from layout.tampilan_awal import Ui_Form as tampilan_awal
from layout.login_admin import Ui_Admin as login_admin
from layout.menu_admin import Ui_Form as menu_admin


class tampilanAwal(tampilan_awal):
    def __init__(self, dialog):
        tampilan_awal.__init__(self)
        self.setupUi(dialog)

        self.pushButtonAdmin.clicked.connect(self.admin)

    def admin(self):
        tampilanAwalWindow.close()

        self.loginAdminWindow = QtWidgets.QDialog()
        self.loginAdminUi = login_admin()
        self.loginAdminUi.setupUi(self.loginAdminWindow)
        self.loginAdminWindow.show()

        self.pushButtonLogin.clicked.connect(self.login)

    def login(self):
        '''fungsi buat login di menu admin'''
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()
        if(username == "admin" and password == "1234"):
            self.labelWarning.setText("Login berhasil!")

            self.loginAdminWindow.close()
            
            self.adminWindow = QtWidgets.QDialog()
            self.adminWindowUi = menu_admin()
            self.adminWindowUi.setupUi(self.adminWindow)
            self.adminWindow.show()
        
        else:
            self.labelWarning.setText("Login gagal. Coba lagi!")
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tampilanAwalWindow = QtWidgets.QDialog()
    tampilanAwalUi = tampilanAwal(tampilanAwalWindow)
    tampilanAwalWindow.show()

    sys.exit(app.exec_())