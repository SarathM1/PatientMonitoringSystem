from PyQt4.QtCore import  *
from PyQt4.QtGui import *
import sys
import socket
import threading 

from PyQt4 import uic


import guiServer 

clTemp=0                                          #Defenition of global variable
clHeart=0
clBreath=0
serverData=0
event = threading.Event()
event2 = threading.Event()

class myWindow(QMainWindow,guiServer.Ui_MainWindow):
    def __init__(self):
        super(myWindow,self).__init__()
        uic.loadUi('main.ui',self)
        self.setupUi(self)
        self.connect(self.settingsOk,SIGNAL("clicked()"),self.settings)
        self.connect(self.cmdOk,SIGNAL("clicked()"),self.readData)
    def settings(self):
        servIp = str(self.serverIp.text()) 
        servPort= int(self.serverPort.text())
        self.thread1=workerThread(self,servIp,servPort)
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
    def run(self):
        host = self.servIp
        port = self.servPort

        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind((host,port))

        print "Server Started"

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

