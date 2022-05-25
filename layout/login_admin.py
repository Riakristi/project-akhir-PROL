# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_admin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(290, 200)
        self.verticalLayoutWidget = QtWidgets.QWidget(Admin)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 183))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelSelamatDatangAdmin = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelSelamatDatangAdmin.setFont(font)
        self.labelSelamatDatangAdmin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSelamatDatangAdmin.setObjectName("labelSelamatDatangAdmin")
        self.verticalLayout.addWidget(self.labelSelamatDatangAdmin)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.labelUsername = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelUsername.setObjectName("labelUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelUsername)
        self.lineEditUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditUsername.setText("")
        self.lineEditUsername.setClearButtonEnabled(False)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditUsername)
        self.labelPassword = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelPassword.setObjectName("labelPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditPassword.setText("")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushButtonLogin = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.verticalLayout.addWidget(self.pushButtonLogin)
        self.labelWarning = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelWarning.setObjectName("labelWarning")
        self.verticalLayout.addWidget(self.labelWarning)

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Form"))
        self.labelSelamatDatangAdmin.setText(_translate("Admin", "Selamat Datang Admin"))
        self.labelUsername.setText(_translate("Admin", "Username"))
        self.labelPassword.setText(_translate("Admin", "Password"))
        self.pushButtonLogin.setText(_translate("Admin", "Masuk"))
        self.labelWarning.setText(_translate("Admin", "Masukkan username dan password!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QWidget()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())
