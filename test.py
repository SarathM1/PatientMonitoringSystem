from PyQt4.QtCore import  *
from PyQt4.QtGui import *
import sys
from PyQt4 import uic

class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow,self).__init__()
        uic.loadUi('test.ui',self)
        self.show()
        
        self.connect(self.button,SIGNAL("clicked()"),self.showMessage)
    def showMessage(self):
        QMessageBox.information(self,"Hello","Hello there"+self.lineEdit.text())
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = myWindow()
    sys.exit(app.exec_())
