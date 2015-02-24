from PyQt4.QtCore import  *
from PyQt4.QtGui import *
#from PySide.QtCore import *
#from PySide.QtGui import *
import sys
import socket
import threading 

import server

clTemp='0'                                          #Defenition of global variable
clHeart='0'
clBreath='0'
clName = '0'

class myWindow(QMainWindow,server.Ui_MainWindow):
    def __init__(self,parent=None):
        super(myWindow,self).__init__(parent)

        self.setupUi(self)
	
	self.threadObj = workerThread()
        self.connect(self.run,SIGNAL("clicked()"),self.settings)

	"""self.connect(self.dataOk,SIGNAL("clicked()"),self.update)

            
	self.connect(self.threadObj, SIGNAL('threadDone()'), self.update,Qt.DirectConnection)"""

    def settings(self):
        servIp = str(self.serverIp.text()) 
        servPort= int(self.serverPort.text())
	self.thread1=workerThread(self)
	#self.connect(self.thread1,SIGNAL("serverStarted"),self.serverStarted,Qt.DirectConnection)
        self.connect(self.thread1, SIGNAL('updateUi'), self.update,Qt.QueuedConnection)
        self.thread1.start()
    def serverStarted(self):
		
	self.textEdit.append("Server Started . .\n")
    def update(self):
	global clName
        global clTemp
        global clHeart
        global clBreath
	print '\n\nIn main Thread'

        print "Name " + clName
	print "Temp " + clTemp
	print "Heart " + clHeart
	print "Breath " + clBreath
	self.name1.setText(clName)
	self.temp1.setText(clTemp)
	self.heart1.setText(clHeart)
	self.pressure1.setText(clBreath)
    


class workerThread(QThread):
    def __init__(self,parent=None,SA='127.0.0.1',SP=5000):
        self.yourInit(SA,SP)
	self.p = parent
        super(workerThread,self).__init__(parent)
    def yourInit(self,si,sp):
        self.servIp=si
        self.servPort=sp
    
    def run(self):
        host = self.servIp
        port = self.servPort

        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind((host,port))
	
	print "Server Started"	
	#self.emit(SIGNAL("serverStarted"))

	global clName
	global clTemp
        global clHeart
        global clBreath

	while True:
		clName,addr = s.recvfrom(1024)		
		clTemp,addr = s.recvfrom(1024)
		clHeart,addr = s.recvfrom(1024)
		clBreath,addr = s.recvfrom(1024)
		self.emit(SIGNAL("updateUi"))

	"""clName = '10'
	clTemp = '20'
        clHeart = '30'
        clBreath = '40'
	addr=10000"""

	print "message from:" + str(addr)
	print "name " + clName		
	print "Temp " + clTemp
	print "heart " + clHeart
	print "breath " + clBreath
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = myWindow()

    window.show()
	
    app.exec_()




