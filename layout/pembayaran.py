# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pembayaran.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(424, 396)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 401, 368))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.qr_frame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qr_frame.sizePolicy().hasHeightForWidth())
        self.qr_frame.setSizePolicy(sizePolicy)
        self.qr_frame.setMinimumSize(QtCore.QSize(250, 250))
        self.qr_frame.setMaximumSize(QtCore.QSize(250, 250))
        self.qr_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qr_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qr_frame.setObjectName("qr_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.qr_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.qr_label = QtWidgets.QLabel(self.qr_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qr_label.sizePolicy().hasHeightForWidth())
        self.qr_label.setSizePolicy(sizePolicy)
        self.qr_label.setText("")
        self.qr_label.setPixmap(QtGui.QPixmap("../../../Pictures/rumahsakit/Indra.png"))
        self.qr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.qr_label.setObjectName("qr_label")
        self.horizontalLayout_6.addWidget(self.qr_label)
        self.horizontalLayout_5.addWidget(self.qr_frame)
        self.verticalLayout_2.addWidget(self.frame)
        self.voucer_frame = QtWidgets.QFrame(self.layoutWidget)
        self.voucer_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.voucer_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.voucer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.voucer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.voucer_frame.setObjectName("voucer_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.voucer_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.voucer_content = QtWidgets.QFrame(self.voucer_frame)
        self.voucer_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.voucer_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.voucer_content.setObjectName("voucer_content")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.voucer_content)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.voucer_label = QtWidgets.QLabel(self.voucer_content)
        self.voucer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.voucer_label.setObjectName("voucer_label")
        self.horizontalLayout_7.addWidget(self.voucer_label)
        self.voucer_input = QtWidgets.QLineEdit(self.voucer_content)
        self.voucer_input.setText("")
        self.voucer_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.voucer_input.setObjectName("voucer_input")
        self.horizontalLayout_7.addWidget(self.voucer_input)
        self.apply_button = QtWidgets.QPushButton(self.voucer_content)
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout_7.addWidget(self.apply_button)
        self.verticalLayout_3.addWidget(self.voucer_content)
        self.voucer_info = QtWidgets.QLabel(self.voucer_frame)
        self.voucer_info.setText("")
        self.voucer_info.setAlignment(QtCore.Qt.AlignCenter)
        self.voucer_info.setObjectName("voucer_info")
        self.verticalLayout_3.addWidget(self.voucer_info)
        self.label_sukses = QtWidgets.QLabel(self.voucer_frame)
        self.label_sukses.setText("")
        self.label_sukses.setObjectName("label_sukses")
        self.verticalLayout_3.addWidget(self.label_sukses)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_cekBayar = QtWidgets.QPushButton(self.voucer_frame)
        self.pushButton_cekBayar.setObjectName("pushButton_cekBayar")
        self.horizontalLayout.addWidget(self.pushButton_cekBayar)
        self.pushButton_cetakStruk = QtWidgets.QPushButton(self.voucer_frame)
        self.pushButton_cetakStruk.setObjectName("pushButton_cetakStruk")
        self.horizontalLayout.addWidget(self.pushButton_cetakStruk)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.voucer_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.voucer_label.setText(_translate("Form", "Voucer : "))
        self.apply_button.setText(_translate("Form", "Apply"))
        self.pushButton_cekBayar.setText(_translate("Form", "Cek Bayar"))
        self.pushButton_cetakStruk.setText(_translate("Form", "Cetak Struk"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
