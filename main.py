from cmath import log
import sys
from PyQt5 import QtWidgets
from tampilan_awal import Ui_Form as tampilan_awal


class tampilanAwal(tampilan_awal):
    def __init__(self, dialog):
        tampilan_awal.__init__(self)
        self.setupUi(dialog)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tampilanAwalWindow = QtWidgets.QDialog()
    tampilanAwalUi = tampilanAwal(tampilanAwalWindow)
    tampilanAwalWindow.show()

    sys.exit(app.exec_())