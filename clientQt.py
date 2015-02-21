from PyQt4.QtCore import  *
from PyQt4.QtGui import *
import sys
import socket
import threading 

from PyQt4 import uic


import gui 

clientData=0                                          #Defenition of global variable
serverData=0
event = threading.Event()
event2 = threading.Event()

class myWindow(QMainWindow,gui.Ui_MainWindow):
    def __init__(self):
        super(myWindow,self).__init__()
        uic.loadUi('main.ui',self)
        self.setupUi(self)
        self.connect(self.socketOk,SIGNAL("clicked()"),self.client)
        self.connect(self.cmdOk,SIGNAL("clicked()"),self.readData)
    def client(self):
        host = str(self.ip.text()) 
        port= int(self.port.text())
        self.thread1=workerThread(self,host,port)
        self.thread1.start()
    def readData(self):
        global clientData
        clientData = self.cmd.text()                         # clientData is global variable
        event.set()
        #thread2=workerThread2(self,data)


"""class workerThread2(QThread):
    def __init__(self,parent=None,h=0,p=0):
        self.yourInit(h,p)
        super(workerThread,self).__init__(parent)
    def yourInit(self,x,y):
        self.host=x
        self.port=y
 """

class workerThread(QThread):
    def __init__(self,parent=None,h=0,p=0):
        self.yourInit(h,p)
        super(workerThread,self).__init__(parent)
    def yourInit(self,x,y):
        self.host=x
        self.port=y
    def run(self):
        #print self.h1 + ',' + str(self.p1)
        s=socket.socket()
        s.connect((self.host,self.port))
        event.wait()
        global clientData
        global serverData
        message = clientData
        while message!='q':
            s.send(message)
            serverData =s.recv(1024)
            print 'Received data from server: ' + str(serverData)
            #message = chr(ord(message) + 1) 
            event.clear()
            event.wait()
            message = clientData
        #data=s.recv(1024)
        #print 'Received data from server: '+str(data)
        s.close()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window = myWindow()
    window.show()
    app.exec_()

