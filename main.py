# import modul
import datetime
import sys
from typing import final
import xendit
from xendit import EWallet
import qrcode, json

# import layout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, QtGui, QtCore
from layout.tampilan_awal import Ui_Form as tampilan_awal
from layout.login_admin import Ui_MainWindow as login_admin
from layout.menu_admin import Ui_MainWindow as menu_admin
from layout.edit_rasa_topping import Ui_MainWindow as update_admin
from layout.list_cup import Ui_Form as list_cup
from layout.pilihan import Ui_MainWindow as pilihan_menu
from layout.history import Ui_Form as riwayat_pembelian
from layout.rekap_penjualan import Ui_Form as rekap_penjualan
from layout.pembayaran import Ui_Form as pembayaran
from layout.struk_beli import Ui_Form as struk_beli

""" import file model database """
# import file model database
import model
import model2

# api key dari xendit
xendit.api_key = "xnd_development_nQN91JP7PtSKjWmf9dJJRpltxiS3nF0gXRvsFsdGMF7b92VxlAy7doG1pV2tMO"

#tanggal
waktu = datetime.datetime.today()
tanggal_pembelian = waktu.strftime("%A, %d %B, %Y, %H:%M:%S")

# default
potongan = 0
nama = "Pelanggan"



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
        self.menuAdminUi.rekapPenjualanUi = rekap_penjualan()
        self.menuAdminUi.rekapPenjualanApp = rekapPenjualan(self.menuAdminUi.rekapPenjualanWindow)
        self.menuAdminUi.rekapPenjualanWindow.show()

    def inputNama(self):
        global nama
        self.listcup = QtWidgets.QWidget()
        self.listcupUi = list_cup()
        self.listcupUi.setupUi(self.listcup)
        tampilanAwalWindow.hide()
        self.listcup.show()

        self.listcupUi.label_cone.setPixmap(QtGui.QPixmap('img/cone.jpg').scaled(490, 400))
        
        nama_pembeli = self.lineEditNama.text()
        if nama_pembeli != "":
            nama =  nama_pembeli
            
        else:
            pass

        self.listcupUi.pushButtonNext.clicked.connect(self.pilihan)

    def pilihan(self):
        global jenis_cone,varian_rasa,varian_toping
        self.pilihanmenu = QtWidgets.QMainWindow()
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

        #button grup untuk checkbox pilihan cone
        self.button_group_cone = QtWidgets.QButtonGroup() 
        self.button_group_cone.addButton(self.pilihanmenuUi.checkBox) 
        self.button_group_cone.addButton(self.pilihanmenuUi.checkBox_2) 
        self.button_group_cone.addButton(self.pilihanmenuUi.checkBox_3)


        self.button_group_cone.setExclusive(True) 
        for cone in self.button_group_cone.buttons(): 
            cone.setCheckState(QtCore.Qt.Unchecked)

        #button grup untuk checkbox pilihan rasa
        self.button_group_rasa = QtWidgets.QButtonGroup() 
        self.button_group_rasa.addButton(self.pilihanmenuUi.checkBox_4) 
        self.button_group_rasa.addButton(self.pilihanmenuUi.checkBox_5) 
        self.button_group_rasa.addButton(self.pilihanmenuUi.checkBox_6)
        self.button_group_rasa.addButton(self.pilihanmenuUi.checkBox_7)

        self.button_group_rasa.setExclusive(True) 
        for rasa in self.button_group_rasa.buttons(): 
            rasa.setCheckState(QtCore.Qt.Unchecked)

        #button grup untuk checkbox pilihan topping
        self.button_group_topping = QtWidgets.QButtonGroup() 
        self.button_group_topping.addButton(self.pilihanmenuUi.checkBox_8) 
        self.button_group_topping.addButton(self.pilihanmenuUi.checkBox_9) 
        self.button_group_topping.addButton(self.pilihanmenuUi.checkBox_10)
        self.button_group_topping.addButton(self.pilihanmenuUi.checkBox_11)
        self.button_group_topping.addButton(self.pilihanmenuUi.checkBox_12)

        self.button_group_topping.setExclusive(True) 
        for topping in self.button_group_topping.buttons(): 
            topping.setCheckState(QtCore.Qt.Unchecked)
        
        # cek button checkbox
        # checkbox cone
        for cone in self.button_group_cone.buttons(): 
            if cone.CheckState(QtCore.Qt.Unchecked):
                self.pilihanmenuUi.label_2.setText("Silahkan ceklist pada checkbox pilihan menu terlebih dahulu sebelum melanjutkan pemesanan!")
            else:
                self.pilihanmenuUi.pushButton_2.clicked.connect(self.payment)

        # checkbox rasa
        for rasa in self.button_group_rasa.buttons(): 
            if rasa.Unchecked():
                self.pilihanmenuUi.label_2.setText("Silahkan ceklist pada checkbox pilihan menu terlebih dahulu sebelum melanjutkan pemesanan!")
            else:
                self.pilihanmenuUi.pushButton_2.clicked.connect(self.payment)

        # checkbox topping
        for topping in self.button_group_topping.buttons(): 
            if topping.Unchecked():
                self.pilihanmenuUi.label_2.setText("Silahkan ceklist pada checkbox pilihan menu terlebih dahulu sebelum melanjutkan pemesanan!")
            else:
                self.pilihanmenuUi.pushButton_2.clicked.connect(self.payment)


        # if varian_rasa != "" and varian_toping != "" and jenis_cone != "":
        #     self.pilihanmenuUi.pushButton_2.clicked.connect(self.payment)
        # else:
        #     self.pilihanmenuUi.label_2.setText("Silahkan ceklist pada checkbox pilihan menu terlebih dahulu sebelum melanjutkan pemesanan!")


        # try:
        #     if varian_rasa != "" and varian_toping != "" and jenis_cone != "":
        #         self.pilihanmenuUi.pushButton_2.clicked.connect(self.payment)
 
        # except:
        #     self.pilihanmenuUi.label_2.setText("Silahkan ceklist pada checkbox pilihan menu terlebih dahulu sebelum melanjutkan pemesanan!")
        # finally:
        #     if varian_rasa and varian_toping and jenis_cone != "":


    def checkbox(self):
        global harga, varian_rasa, varian_toping, jenis_cone
        jenis_cone = ""
        varian_rasa = ""
        varian_toping = ""
        if self.pilihanmenuUi.checkBox.isChecked():
            jenis_cone = "Waffle Cone"
        elif self.pilihanmenuUi.checkBox_2.isChecked():
            jenis_cone = "Sugar Cone"
        elif self.pilihanmenuUi.checkBox_3.isChecked():
            jenis_cone = "Cake Cone"
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
        elif self.pilihanmenuUi.checkBox_12.isChecked():
            varian_toping = model.getNama(9)
            

        harga_rasa = model.getHarga(varian_rasa)
        harga_topping = model.getHarga(varian_toping)
        
        # print(harga_rasa)
        # print(harga_topping)
        print(varian_rasa)
        print(varian_toping)
        harga = int(harga_rasa[0][0]) + int(harga_topping[0][0])    
        #print(harga)

    def payment(self):
        self.pembayaran = QtWidgets.QMainWindow()
        self.pembayaranUi = pembayaran()
        self.pembayaranUi.setupUi(self.pembayaran)
        self.pilihanmenu.hide()
        self.pembayaran.show()  
        self.checkbox()
        self.qr()
      
        self.pembayaranUi.qr_label.setPixmap(QtGui.QPixmap('qr.png').scaled(248, 248))
        self.pembayaranUi.pushButton_cekBayar.clicked.connect(self.cek_bayar)
        self.pembayaranUi.apply_button.clicked.connect(self.voucher)


    def voucher(self):
        global potongan
        kode_voucer = self.pembayaranUi.voucer_input.text()
        voucher = model.getVoucher(kode_voucer)  
        
        print(voucher)
                
        if voucher != 0:
            self.pembayaranUi.voucer_info.setText("Kode voucher berhasil digunakan")
            self.pembayaranUi.voucer_input.setText("")
            potongan = int(voucher[0])
        else:
            self.pembayaranUi.voucer_info.setText("Kode voucer tidak terdaftar")
            self.pembayaranUi.voucer_input.setText("")
            
        

    def cek_bayar(self):
        global status
        status = self.check_status(charge_id)
        if status == "SUCCEEDED":
            # if status == "SUCCEEDED":
            self.pembayaranUi.pushButton_cetakStruk.clicked.connect(self.struk)

            self.pembayaranUi.voucer_info.setText("Pembayaran berhasil")
            
        else:
            self.pembayaranUi.voucer_info.setText("Silahkan scan QR pembayaran terlebih dahulu!")
          
                     
            
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

        """generate qrcode image"""
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
        status = ewallet_status.status
        return status
        
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
        
    def struk(self):
        self.struk_beli = QtWidgets.QWidget()
        self.strukbeliUi = struk_beli()
        self.strukbeliUi.setupUi(self.struk_beli)
        self.struk_beli.show()

        self.strukbeliUi.label_nama.setText(nama)
        self.strukbeliUi.label_cup.setText(jenis_cone)
        self.strukbeliUi.label_rasa.setText(varian_rasa)
        self.strukbeliUi.label_topping.setText(varian_toping)
        self.strukbeliUi.label_harga.setText(str(harga))
        self.strukbeliUi.label_cashback.setText(str(potongan))
        self.strukbeliUi.label_tanggal.setText(tanggal_pembelian)
        
        model2.insertDatatoDB(nama,tanggal_pembelian,jenis_cone,varian_rasa,varian_toping,harga)



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
    #     self.exclusive_rasa()

    # def exclusive_rasa(self):
    #     self.button_group_rasa = QtWidgets.QButtonGroup() 
    #     self.button_group_rasa.addButton(self.pilihanmenuUi.checkBox_4) 
    #     self.button_group_rasa.addButton(self.pilihanmenuUi.checkBox_5) 
    #     self.button_group_rasa.addButton(self.pilihanmenuUi.checkBox_6)
    #     self.button_group_rasa.addButton(self.pilihanmenuUi.checkBox_7)

    #     self.button_group_rasa.setExclusive(True) 
    #     for rasa in self.button_group_rasa.buttons(): 
    #         rasa.setCheckState(QtCore.Qt.Unchecked)

class riwayatPembelian(riwayat_pembelian):
    def __init__(self, dialog):
        riwayat_pembelian.__init__(self)
        self.setupUi(dialog)
        self.viewhistory()


    def viewhistory(self):
        data = model2.getHistory()
        for item in data:
            rowPosition = self.tableWidgetHistory.rowCount()
            self.tableWidgetHistory.insertRow(rowPosition)
            self.tableWidgetHistory.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(item[0]))
            self.tableWidgetHistory.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(item[1]))
            self.tableWidgetHistory.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(item[2]))
            self.tableWidgetHistory.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(item[3]))
            self.tableWidgetHistory.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(item[4]))
            self.tableWidgetHistory.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(item[5])))

class rekapPenjualan(rekap_penjualan):
    def __init__(self, dialog):
        rekap_penjualan.__init__(self)
        self.setupUi(dialog)
        self.viewrekap()

    def viewrekap(self):
        waffleCone = len(model2.count_cone("Waffle Cone"))
        sugarCone = len(model2.count_cone("Sugar Cone"))
        cakeCone = len(model2.count_cone("Cake Cone"))
        # print(waffleCone, sugarCone, cakeCone)

        ambilrasa = model2.ambilrasa()
        # print(ambilrasa)
        columnPosition_cupsize = self.tableWidgetCupSize.columnCount()
        #self.tableWidgetCupSize.insertColumn(columnPosition_cupsize)
        self.tableWidgetCupSize.setItem(0, 0, QtWidgets.QTableWidgetItem(str(waffleCone)))
        self.tableWidgetCupSize.setItem(1, 0, QtWidgets.QTableWidgetItem(str(sugarCone)))
        self.tableWidgetCupSize.setItem(2, 0, QtWidgets.QTableWidgetItem(str(cakeCone)))
        

        for rasa in ambilrasa:
            rowPosition_varianrasa = self.tableWidgetVarianRasa.rowCount()
            self.tableWidgetVarianRasa.insertRow(rowPosition_varianrasa)
            # print(rasa)
            ambiljumlahrasa = model2.count_rasa(rasa[0])
            self.tableWidgetVarianRasa.setItem(rowPosition_varianrasa, 0, QtWidgets.QTableWidgetItem(rasa[0]))
            self.tableWidgetVarianRasa.setItem(rowPosition_varianrasa, 1, QtWidgets.QTableWidgetItem(str(len(ambiljumlahrasa))))
            
        
        ambiltoping = model2.ambiltoping()
        for toping in ambiltoping:
            rowPosition_variantopping = self.tableWidgetVarianToping.rowCount()
            self.tableWidgetVarianToping.insertRow(rowPosition_variantopping)

            ambiljumlahtoping = model2.count_toping(toping[0])
            self.tableWidgetVarianToping.setItem(rowPosition_variantopping, 0, QtWidgets.QTableWidgetItem(toping[0]))
            self.tableWidgetVarianToping.setItem(rowPosition_variantopping, 1, QtWidgets.QTableWidgetItem(str(len(ambiljumlahtoping))))
            
        jumlahCone = model2.jumlahCone()
        self.labelTotalPenjualan.setText("Total Penjualan Sebanyak {} Cone".format(str(len(jumlahCone))))
        self.labelTotalPenjualan.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tampilanAwalWindow = QtWidgets.QWidget()
    tampilanAwalUi = tampilanAwal(tampilanAwalWindow)
    tampilanAwalWindow.show()

    sys.exit(app.exec_())