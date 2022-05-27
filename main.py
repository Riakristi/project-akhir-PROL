from distutils.log import error
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from layout.tampilan_awal import Ui_Form as tampilan_awal
from layout.login_admin import Ui_Admin as login_admin
from layout.menu_admin import Ui_Form as menu_admin
from layout.edit_rasa_topping import Ui_UpdateStok as update_admin
from layout.list_cup import Ui_Form as list_cup
from layout.pilihan import Ui_Form as pilihan_menu
import model

class tampilanAwal(tampilan_awal):
    def __init__(self, dialog):
        tampilan_awal.__init__(self)
        self.setupUi(dialog)
        self.pushButtonLogin.setIcon(QtGui.QIcon('img/user.png'))

        self.pushButtonLogin.clicked.connect(self.admin)
        self.pushButtonPesan.clicked.connect(self.inputNama)

    def welcomeScreen(self):
        self.welcomeWindow = QtWidgets.QWidget()
        self.welcomeUi = tampilan_awal()
        self.updateApp = tampilanAwal(self.welcomeWindow)
        self.menuAdminWindow.close()
        self.welcomeWindow.show()

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
            self.loginAdminUi.labelWarning.show()
            
            self.menuAdminWindow = QtWidgets.QWidget()
            self.menuAdminUi = menu_admin()
            self.menuAdminUi.setupUi(self.menuAdminWindow)
            self.loginAdminWindow.close()
            self.menuAdminWindow.show()

            self.menuAdminUi.pushButtonUpdateStok.clicked.connect(self.menuAdmin)
            self.menuAdminUi.pushButtonKembali.clicked.connect(self.welcomeScreen)
        
        else:
            self.loginAdminUi.labelWarning.setText("Login gagal. Coba lagi!")
            self.loginAdminUi.labelWarning.show()

    def menuAdmin(self):
        self.menuAdminUi.updateWindow = QtWidgets.QWidget()
        self.menuAdminUi.updateUi = update_admin()
        self.menuAdminUi.updateApp = updateStok(self.menuAdminUi.updateWindow)
        self.menuAdminUi.updateWindow.show()

    def inputNama(self):
        nama = self.lineEditNama.text()

        self.listcup = QtWidgets.QWidget()
        self.listcupUi = list_cup()
        self.listcupUi.setupUi(self.listcup)
        tampilanAwalWindow.hide()
        self.listcup.show()

        self.listcupUi.label_smallcup.setPixmap(QtGui.QPixmap('img/small.png'))
        self.listcupUi.label_mediumcup.setPixmap(QtGui.QPixmap('img/medium.png'))
        self.listcupUi.label_largecup.setPixmap(QtGui.QPixmap('img/large.png'))

        self.listcupUi.pushButtonNext.clicked.connect(self.pilihan)

    def pilihan(self):
        self.pilihanmenu = QtWidgets.QWidget()
        self.pilihanmenuUi = pilihan_menu()
        self.pilihanmenuUi.setupUi(self.pilihanmenu)
        self.listcup.hide()
        self.pilihanmenu.show()

class updateStok(update_admin):
    def __init__(self, dialog):
        update_admin.__init__(self)
        self.setupUi(dialog)
        self.showMenu()
        self.comboBoxJenis.currentIndexChanged['QString'].connect(self.showMenu)

        self.pushButtonGanti.clicked.connect(self.updateMenu)
        self.labelWarning.setText("Klik tombol ganti untuk mengganti nama")

    def showMenu(self):
        getJenis = self.comboBoxJenis.currentText()
        self.comboBox.clear()
        getMenu = model.getMenu(getJenis)
        for menu in getMenu:
            self.comboBox.addItem(menu[1])
        
    def updateMenu(self):
        namaAwal = self.comboBox.currentText()
        namaGanti = self.lineEditInput.text()

        msg = QtWidgets.QMessageBox()

        model.updateMenu(namaAwal, namaGanti)
        msg.setText("Data berhasil diganti")
        msg.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tampilanAwalWindow = QtWidgets.QWidget()
    tampilanAwalUi = tampilanAwal(tampilanAwalWindow)
    tampilanAwalWindow.show()

    sys.exit(app.exec_())