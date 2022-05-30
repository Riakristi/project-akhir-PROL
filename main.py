import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from layout.tampilan_awal import Ui_Form as tampilan_awal
from layout.login_admin import Ui_MainWindow as login_admin
from layout.menu_admin import Ui_MainWindow as menu_admin
from layout.edit_rasa_topping import Ui_MainWindow as update_admin
from layout.list_cup import Ui_Form as list_cup
from layout.pilihan import Ui_Form as pilihan_menu
from layout.history import Ui_Form as riwayat_pembelian
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

        self.loginAdminWindow = QtWidgets.QMainWindow()
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
            
            self.menuAdminWindow = QtWidgets.QMainWindow()
            self.menuAdminUi = menu_admin()
            self.menuAdminUi.setupUi(self.menuAdminWindow)
            self.loginAdminWindow.close()
            self.menuAdminWindow.show()

            self.menuAdminUi.pushButtonUpdateStok.clicked.connect(self.menuAdmin)
            self.menuAdminUi.pushButtonRiwayatPembelian.clicked.connect(self.riwayatPembelianAdmin)
            self.menuAdminUi.pushButtonKembali.clicked.connect(self.welcomeScreen)
        
        else:
            self.loginAdminUi.labelWarning.setText("Login gagal. Coba lagi!")
            self.loginAdminUi.labelWarning.show()

    def menuAdmin(self):
        self.menuAdminUi.updateWindow = QtWidgets.QMainWindow()
        self.menuAdminUi.updateUi = update_admin()
        self.menuAdminUi.updateApp = updateStok(self.menuAdminUi.updateWindow)
        self.menuAdminUi.updateWindow.show()

    def riwayatPembelianAdmin(self):
        self.menuAdminUi.riwayatPembelianWindow = QtWidgets.QWidget()
        self.menuAdminUi.riwayatPembelianUi = riwayat_pembelian()
        self.menuAdminUi.riwayatPembelianApp = riwayatPembelian(self.menuAdminUi.riwayatPembelianWindow)
        self.menuAdminUi.riwayatPembelianWindow.show()

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
        
        self.pilihanmenuUi.checkBox_4.setText(model.getNama(1))
        self.pilihanmenuUi.checkBox_5.setText(model.getNama(2))
        self.pilihanmenuUi.checkBox_6.setText(model.getNama(3))
        self.pilihanmenuUi.checkBox_7.setText(model.getNama(4))
        
        self.pilihanmenuUi.checkBox_8.setText(model.getNama(5))
        self.pilihanmenuUi.checkBox_12.setText(model.getNama(9))
        self.pilihanmenuUi.checkBox_9.setText(model.getNama(6))
        self.pilihanmenuUi.checkBox_10.setText(model.getNama(7))
        self.pilihanmenuUi.checkBox_11.setText(model.getNama(8))

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

class riwayatPembelian(riwayat_pembelian):
    def __init__(self, dialog):
        riwayat_pembelian.__init__(self)
        self.setupUi(dialog)

        # self.pushButtonRiwayatPembelian.clicked.connect()

# class HistoryPenjualan(history):
#     def _init_(self, dialog):
#         history._init_(self)
#         self.setupUi(dialog)
#         self.mainHistory = QtWidgets.QDialog()
#         self.mainUI = history()
#         self.mainUI.setupUi(self.mainHistory)
#         menu_admin.hide()
#         self.mainHistory.show()
#         self.viewData()
#         model2.createDatabase()

#     def viewData(self):
#         data = model2.viewDataFromDB()

#         for penjualan in data:
#             rowPosition = self.mainUI.tableWidgetHistory.rowCount()
#             self.mainUI.tableWidgetHistory.insertRow(rowPosition)
#             self.mainUI.tableWidgetHistory.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(penjualan[0]))
#             self.mainUI.tableWidgetHistory.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(penjualan[1]))
#             self.mainUI.tableWidgetHistory.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(penjualan[2]))
#             self.mainUI.tableWidgetHistory.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(penjualan[3]))
#             self.mainUI.tableWidgetHistory.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(penjualan[4]))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tampilanAwalWindow = QtWidgets.QWidget()
    tampilanAwalUi = tampilanAwal(tampilanAwalWindow)
    tampilanAwalWindow.show()

    sys.exit(app.exec_())