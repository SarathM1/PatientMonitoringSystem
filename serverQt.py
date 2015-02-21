from PyQt4.QtCore import  *
from PyQt4.QtGui import *
import sys
import socket
from PyQt4 import uic

import socket
import threading

import gui 

h='0.0.0.0'
p=5000

class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting "+self.name
       
        ############################
       """ s=socket.socket()
        s.bind(('0.0.0.0',5000))
        s.listen(2)
        
        (c,(ip,port))=s.accept()

        print 'client address: '+str(c)+','+str(ip)+','+str(port)

        while True:
            data=c.recv(1024)
            if not data:
                break
            print "from connected user: " + str(data)
            data=str(data).upper()
            print "Sending: "+str(data)
            c.send(data)

        c.close()"""

        ##################################

        print "Ending "+self.name



class myWindow(QMainWindow,gui.Ui_MainWindow):
    def __init__(self):
        super(myWindow,self).__init__()
        uic.loadUi('main.ui',self)
        self.setupUi(self)

        self.connect(self.socketOk,SIGNAL("clicked()"),self.threadInit)
        
    def serverInit(self):
        global h
        global p
        h='0.0.0.0'
        p=5000
        print str(type(h)) + ',' + h + ',' + str(type(p)) + ',' + str(p)
        self.threadInit()
    def threadInit(self):
        threads=[]

        thread1=myThread(1,'Client1',1)
        thread2=myThread(2,'Client2',2)
        thread1.start()
        thread2.start()

        threads.append(thread1)
        threads.append(thread2)

        for t in threads:
            t.join()

        print 'Exiting main thread'

                 


app = QApplication(sys.argv)
window = myWindow()
window.show()
sys.exit(app.exec_())


