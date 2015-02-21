from PyQt4.QtCore import  *
from PyQt4.QtGui import *
import sys
import socket
import threading 

from PyQt4 import uic


import gui 

clTemp=0                                          #Defenition of global variable
clHeart=0
clBreath=0
serverData=0
event = threading.Event()
event2 = threading.Event()

class myWindow(QMainWindow,gui.Ui_MainWindow):
    def __init__(self):
        super(myWindow,self).__init__()
        uic.loadUi('main.ui',self)
        self.setupUi(self)
        self.connect(self.settingsOk,SIGNAL("clicked()"),self.settings)
        self.connect(self.cmdOk,SIGNAL("clicked()"),self.readData)
    def settings(self):
        servIp = str(self.serverIp.text()) 
        servPort= int(self.serverPort.text())
        clIp = str(self.clientIp.text()) 
        clPort= int(self.clientPort.text())
        self.thread1=workerThread(self,servIp,servPort,clIp,clPort)
        self.thread1.start()
    def readData(self):
        global clientTemp
        global clientHeart
        global clientBreath

        clientTemp = self.temp.text()                         # clientData is global variable
        clientHeart = self.heart.text() 
        clientBreath = self.breath.text()
        event.set()
        #thread2=workerThread2(self,data)



class workerThread(QThread):
    def __init__(self,parent=None,SA=0,SP=0,CA=0,CP=0):
        self.yourInit(SA,SP,CA,CP)
        super(workerThread,self).__init__(parent)
    def yourInit(self,si,sp,ci,cp):
        self.servIp=si
        self.servPort=sp
        self.clIp=ci
        self.clPort=cp
    def run(self):
        host = self.clIp
        port = self.clPort

        server = (self.servIp,self.servPort)

        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind((host,port))

        event.wait()
        global clientTemp
        global clientHeart
        global clientBreath
        s.send(clientTemp)
        s.send(clientHeart)
        s.send(clientBreath)
        s.close()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window = myWindow()
    window.show()
    app.exec_()

