# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'struk_beli.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(332, 220)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 199))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_nama = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_nama.setText("")
        self.label_nama.setObjectName("label_nama")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_nama)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_cup = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_cup.setText("")
        self.label_cup.setObjectName("label_cup")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_cup)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_rasa = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_rasa.setText("")
        self.label_rasa.setObjectName("label_rasa")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_rasa)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_topping = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_topping.setText("")
        self.label_topping.setObjectName("label_topping")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_topping)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_harga = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_harga.setText("")
        self.label_harga.setObjectName("label_harga")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_harga)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_cashback = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_cashback.setText("")
        self.label_cashback.setObjectName("label_cashback")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_cashback)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_tanggal = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_tanggal.setText("")
        self.label_tanggal.setObjectName("label_tanggal")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_tanggal)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "STRUK BELI"))
        self.label.setText(_translate("Form", "Nama                     :"))
        self.label_4.setText(_translate("Form", "Jenis Cone            :"))
        self.label_3.setText(_translate("Form", "Pilihan Rasa           :"))
        self.label_5.setText(_translate("Form", "Pilihan Topping      :"))
        self.label_12.setText(_translate("Form", "Subtotal                 :"))
        self.label_8.setText(_translate("Form", "Cashback               : "))
        self.label_9.setText(_translate("Form", "Tanggal Pembelian :"))
        self.label_6.setText(_translate("Form", " Terima Kasih"))
        self.label_7.setText(_translate("Form", "Atas kepercayaan Anda."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
