# import modul
import datetime
import sys
import xendit
from xendit import EWallet
import qrcode, json

# import layout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, QtGui
from layout.tampilan_awal import Ui_Form as tampilan_awal
from layout.login_admin import Ui_MainWindow as login_admin
from layout.menu_admin import Ui_MainWindow as menu_admin
from layout.edit_rasa_topping import Ui_MainWindow as update_admin
from layout.list_cup import Ui_Form as list_cup
from layout.pilihan import Ui_Form as pilihan_menu
from layout.history import Ui_Form as riwayat_pembelian
from layout.rekap_penjualan import Ui_Form as rekap_penjualan
from layout.pembayaran import Ui_pembayaran as pembayaran

""" import file model database """
# import file model database
import model
import model2

# api key dari xendit
xendit.api_key = "xnd_development_nQN91JP7PtSKjWmf9dJJRpltxiS3nF0gXRvsFsdGMF7b92VxlAy7doG1pV2tMO"

class tampilanAwal(tampilan_awal):
    """ tampilan awal dari program """
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
        """ sebuah fungsi untuk membuat ui dari login admin """
        tampilanAwalWindow.close()

        self.loginAdminWindow = QtWidgets.QMainWindow()
        self.loginAdminUi = login_admin()
        self.loginAdminUi.setupUi(self.loginAdminWindow)
        self.loginAdminWindow.show()
        self.loginAdminUi.pushButtonLogin.clicked.connect(self.login)

    def login(self):
        ''' fungsi buat login di menu admin '''
        username = self.loginAdminUi.lineEditUsername.text()
        password = self.loginAdminUi.lineEditPassword.text()
        if(username == "admin" and password == "1234"):
            """ apabila username dan password sesuai maka lanjut ke ui menu admin """
            """ ui menu admin adalah sebuah fitur untuk menampilkan pilihan mau ganti nama barang, menuju riwayat pembelian, menuju rekap penjualan, atau mau kembali ke tampilan awal """
            self.menuAdminWindow = QtWidgets.QMainWindow()
            self.menuAdminUi = menu_admin()
            self.menuAdminUi.setupUi(self.menuAdminWindow)
            self.loginAdminWindow.close()
            self.menuAdminWindow.show()

            """ reaksi ketika push button di ui menu admin diklik """
            self.menuAdminUi.pushButtonUpdateStok.clicked.connect(self.gantiNamaBarangAdmin)
            self.menuAdminUi.pushButtonRiwayatPembelian.clicked.connect(self.riwayatPembelianAdmin)
            self.menuAdminUi.pushButtonKembali.clicked.connect(self.welcomeScreen)
            self.menuAdminUi.pushButtonRekapPenjualan.clicked.connect(self.rekapPenjualanAdmin)
        
        else:
            """ apabila username atau password tidak sesuai maka akan muncul tulisan peringatan di label warning """
            self.loginAdminUi.labelWarning.setText("Login gagal. Coba lagi!")
            self.loginAdminUi.labelWarning.show()

    def gantiNamaBarangAdmin(self):
        """ sebuah fungsi untuk menampilkan ui ganti nama barang """
        self.menuAdminUi.updateWindow = QtWidgets.QMainWindow()
        self.menuAdminUi.updateUi = update_admin()
        self.menuAdminUi.updateApp = updateStok(self.menuAdminUi.updateWindow)
        self.menuAdminUi.updateWindow.show()

    def riwayatPembelianAdmin(self):
        self.menuAdminUi.riwayatPembelianWindow = QtWidgets.QWidget()
        self.menuAdminUi.riwayatPembelianUi = riwayat_pembelian()
        self.menuAdminUi.riwayatPembelianApp = riwayatPembelian(self.menuAdminUi.riwayatPembelianWindow)
        self.menuAdminUi.riwayatPembelianWindow.show()

    def rekapPenjualanAdmin(self):
        self.menuAdminUi.rekapPenjualanWindow = QtWidgets.QWidget()
        self.menuAdminUi.rekapPenualanUi = rekap_penjualan()
        self.menuAdminUi.rekapPenjualanApp = rekapPenjualan(self.menuAdminUi.rekapPenjualanWindow)
        self.menuAdminUi.rekapPenjualanWindow.show()

    def inputNama(self):
        global nama
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
        global ukuran_cup,varian_rasa,varian_toping
        self.pilihanmenu = QtWidgets.QWidget()
        self.pilihanmenuUi = pilihan_menu()
        self.pilihanmenuUi.setupUi(self.pilihanmenu)
        self.listcup.hide()
        self.pilihanmenu.show()
        
        if self.pilihanmenuUi.checkBox.isChecked():
            ukuran_cup = "SMALL"
        elif self.pilihanmenuUi.checkBox_2.isChecked():
            ukuran_cup = "MEDIUM"
        elif self.pilihanmenuUi.checkBox_3.isChecked():
            ukuran_cup = "LARGE"
        if self.pilihanmenuUi.checkBox_4.isChecked():
            varian_rasa = model.getNama(1)
        elif self.pilihanmenuUi.checkBox_5.isChecked():
            varian_rasa = model.getNama(2)
        elif self.pilihanmenuUi.checkBox_6.isChecked():
            varian_rasa = model.getNama(3)
        elif self.pilihanmenuUi.checkBox_7.isChecked():
            varian_rasa = model.getNama(4)
        if self.pilihanmenuUi.checkBox_8.isChecked():
            varian_toping = model.getNama(5)
        elif self.pilihanmenuUi.checkBox_9.isChecked():
            varian_toping = model.getNama(6)
        elif self.pilihanmenuUi.checkBox_10.isChecked():
            varian_toping = model.getNama(7)
        elif self.pilihanmenuUi.checkBox_11.isChecked():
            varian_toping = model.getNama(8)

        self.pilihanmenuUi.checkBox_4.setText(model.getNama(1))
        self.pilihanmenuUi.checkBox_5.setText(model.getNama(2))
        self.pilihanmenuUi.checkBox_6.setText(model.getNama(3))
        self.pilihanmenuUi.checkBox_7.setText(model.getNama(4))
        
        self.pilihanmenuUi.checkBox_8.setText(model.getNama(5))
        self.pilihanmenuUi.checkBox_12.setText(model.getNama(9))
        self.pilihanmenuUi.checkBox_9.setText(model.getNama(6))
        self.pilihanmenuUi.checkBox_10.setText(model.getNama(7))
        self.pilihanmenuUi.checkBox_11.setText(model.getNama(8))

        self.pilihanmenuUi.pushButton_2.clicked.connect(self.payment)

    def checkbox(self):
        global harga, varian_rasa, varian_toping
        if self.pilihanmenuUi.checkBox.isChecked():
            ukuran_cup = "SMALL"
        elif self.pilihanmenuUi.checkBox_2.isChecked():
            ukuran_cup = "MEDIUM"
        elif self.pilihanmenuUi.checkBox_3.isChecked():
            ukuran_cup = "LARGE"
        if self.pilihanmenuUi.checkBox_4.isChecked():
            varian_rasa = model.getNama(1)
        elif self.pilihanmenuUi.checkBox_5.isChecked():
            varian_rasa = model.getNama(2)
        elif self.pilihanmenuUi.checkBox_6.isChecked():
            varian_rasa = model.getNama(3)
        elif self.pilihanmenuUi.checkBox_7.isChecked():
            varian_rasa = model.getNama(4)
        if self.pilihanmenuUi.checkBox_8.isChecked():
            varian_toping = model.getNama(5)
        elif self.pilihanmenuUi.checkBox_9.isChecked():
            varian_toping = model.getNama(6)
        elif self.pilihanmenuUi.checkBox_10.isChecked():
            varian_toping = model.getNama(7)
        elif self.pilihanmenuUi.checkBox_11.isChecked():
            varian_toping = model.getNama(8)

        harga_rasa = model.getHarga(varian_rasa)
        harga_topping = model.getHarga(varian_toping)
        harga = int(harga_rasa[0][0]) + int(harga_topping[0][0])    
        

    def payment(self):
        self.pembayaran = QtWidgets.QMainWindow()
        self.pembayaranUi = pembayaran()
        self.pembayaranUi.setupUi(self.pembayaran)
        self.pilihanmenu.hide()
        self.pembayaran.show()  
        self.checkbox()
        self.qr()


        self.pembayaranUi.qr_label.setPixmap(QtGui.QPixmap('qr.png').scaled(248, 248))
        self.pembayaranUi.pushButton_cek.clicked.connect(self.cek_bayar)

    def cek_bayar(self):
        status = self.check_status(charge_id)
        if status != "SUCCESS":
            self.cek_bayar()
        else:
            print(status.status)
        
            
    def create_charge(self, product):
        basket = []
        harga = 0
        for item in product:
            basket_item = EWallet.helper_create_basket_item(
                reference_id = "basket-product-ref-id",
                name = item['name'],
                category = item['category'],
                currency = "IDR",
                price = item['harga'],
                quantity = item['quantity'],
                type = "product_type",
                sub_category = "product_sub_category",
                metadata = {
                    "meta": "data"
                }
            )
            harga = harga + (item['harga'] * item['quantity'])
            basket.append(basket_item)

        ewallet_charge = EWallet.create_ewallet_charge(
            reference_id="basket-product-ref-id",
            currency="IDR",
            amount=harga,
            checkout_method="ONE_TIME_PAYMENT",
            channel_code="ID_SHOPEEPAY",
            channel_properties={
                "success_redirect_url": "https://yourwebsite.com/order/123",
            },
            basket=basket,
        )
        qr_string = ewallet_charge.actions['mobile_deeplink_checkout_url']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
           
        )
        qr.add_data(qr_string)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qr.png')
        
        return ewallet_charge

    def check_status(self, charge_id):
        ewallet_status = EWallet.get_ewallet_charge_status(
            charge_id=charge_id,
        )
        return ewallet_status

    def qr(self):
        global charge_id
        product = [
        {
            'name': varian_rasa + ":" + varian_toping ,
            'category': 'minuman',
            'harga': harga,
            'quantity': 1
        },
        ]
        
        request = self.create_charge(product)
        charge_id = request.id
        

class updateStok(update_admin):
    """ class baru untuk fitur penggantian nama barang """
    def __init__(self, dialog):
        update_admin.__init__(self)
        self.setupUi(dialog)
        self.showMenu()
        self.comboBoxJenis.currentIndexChanged['QString'].connect(self.showMenu)

        self.pushButtonGanti.clicked.connect(self.updateMenu)
        self.labelWarning.setText("Klik tombol ganti untuk mengganti nama")

    def showMenu(self):
        """ fungsi untuk menampilkan daftar menu terbaru berdasarkan jenis menu yang tampil di combo box jenis """
        getJenis = self.comboBoxJenis.currentText()
        self.comboBox.clear()
        getMenu = model.getMenu(getJenis)
        for menu in getMenu:
            self.comboBox.addItem(menu[1])
        
    def updateMenu(self):
        """ sebuah fitur untuk mengganti nama barang berdasarkan nama yang tampil di combo box """
        namaAwal = self.comboBox.currentText()
        namaGanti = self.lineEditInput.text()

        model.updateMenu(namaAwal, namaGanti)
        self.lineEditInput.setText("")
        self.showMenu()

        """ tampilan message box ketika data berhasil diganti """
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Status data")
        msg.setText("Data berhasil diganti")
        msg.exec_()

class pilihanMenu(pilihan_menu):
    def __init__(self, dialog):
        pilihan_menu.__init__(self)
        self.setupUi(dialog)

    # def checkPilihan(self):
    #     self.button_group_cup = QtWidgets.QButtonGroup() 
    #     self.button_group_cup.addButton(self.listcupUi.pilihanMenuUi.checkBox) 
    #     self.button_group_cup.addButton(self.listcupUi.pilihanMenuUi.checkBox_2) 
    #     self.button_group_cup.addButton(self.listcupUi.pilihanMenuUi.checkBox_3)

    #     self.button_group_cup.setExclusive(False) 
    #     for cup in self.button_group_cup.buttons(): 
    #         cup.setCheckState(QtCore.Qt.Unchecked)

class riwayatPembelian(riwayat_pembelian):
    def __init__(self, dialog):
        riwayat_pembelian.__init__(self)
        self.setupUi(dialog)

    def tambahData(self):
        nama_pembeli = nama
        waktu = datetime.datetime.today()

        tanggal_pembelian = waktu.strftime("%A, %d %B, %Y, %H:%M:%S")
        
        model2.insertDatatoDB(nama_pembeli,tanggal_pembelian,ukuran_cup,varian_rasa,varian_toping)

        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(nama_pembeli))
        self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(tanggal_pembelian))
        self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(ukuran_cup))
        self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(varian_rasa))
        self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(varian_toping))

class rekapPenjualan(rekap_penjualan):
    def __init__(self, dialog):
        rekap_penjualan.__init__(self)
        self.setupUi(dialog)
    
    def viewData(self):
        cupsizeSmall = model2.viewDataFromDB("ukuran_cup","SMALL")
        cupsizeMedium = model2.viewDataFromDB("ukuran_cup","MEDIUM")
        cupsizeLarge = model2.viewDataFromDB("ukuran_cup","LARGE")

        ambilrasa = model2.ambilrasa()
        rowPosition_cupsize = self.tableWidgetCupSize.rowCount()
        self.tableWidgetCupSize.setItem(rowPosition_cupsize, 0, QtWidgets.QTableWidget(str(len(cupsizeSmall))))
        self.tableWidgetCupSize.setItem(rowPosition_cupsize, 1, QtWidgets.QTableWidget(str(len(cupsizeMedium))))
        self.tableWidgetCupSize.setItem(rowPosition_cupsize, 2, QtWidgets.QTableWidget(str(len(cupsizeLarge))))
        
        rowPosition_variantopping = self.tableWidgetVarianTopping.rowCount()
        self.tableWidgetCupSize.insertRow(rowPosition_cupsize)
        for rasa in ambilrasa:
            rowPosition_varianrasa = self.tableWidgetVarianRasa.rowCount()
            ambiljumlahrasa = model2.viewDataFromDB("varian_rasa",rasa)
            self.tableWidgetVarianRasa.setItem(rowPosition_varianrasa, 0, QtWidgets.QTableWidget(rasa))
            self.tableWidgetVarianRasa.setItem(rowPosition_varianrasa, 1, QtWidgets.QTableWidget(str(len(ambiljumlahrasa))))
        
        ambiltopping = model2.ambiltopping()
        for topping in ambiltopping:
            rowPosition_variantopping = self.tableWidgetVarianTopping.rowCount()
            ambiljumlahtopping = model2.viewDataFromDB("varian_toping",topping)
            self.tableWidgetVarianTopping.setItem(rowPosition_variantopping, 0, QtWidgets.QTableWidget(topping))
            self.tableWidgetVarianTopping.setItem(rowPosition_variantopping, 1, QtWidgets.QTableWidget(str(len(ambiljumlahtopping))))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tampilanAwalWindow = QtWidgets.QWidget()
    tampilanAwalUi = tampilanAwal(tampilanAwalWindow)
    tampilanAwalWindow.show()

    sys.exit(app.exec_())