from PyQt4.QtCore import  *
from PyQt4.QtGui import *
import sqlite3
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
clCampId = '0'



class myWindow(QMainWindow,server.Ui_MainWindow):
    def __init__(self,parent=None):
        super(myWindow,self).__init__(parent)

        self.setupUi(self)
	self.updateTable()
	self.threadObj = workerThread()
        self.connect(self.run,SIGNAL("clicked()"),self.settings)

	"""self.connect(self.dataOk,SIGNAL("clicked()"),self.update)

            
	self.connect(self.threadObj, SIGNAL('threadDone()'), self.update,Qt.DirectConnection)"""

    def settings(self):
        servIp = str(self.serverIp.text()) 
        servPort= int(self.serverPort.text())
	self.thread1=workerThread(self)
	self.connect(self.thread1,SIGNAL("log(QString)"),self.updateLog,Qt.DirectConnection)
        self.connect(self.thread1, SIGNAL('updateUi'), self.update,Qt.QueuedConnection)
        self.thread1.start()
    def updateLog(self,text):
	print "Log"	
	self.textEdit.append(text)
    def update(self):
	global clCampId
	global clName
        global clTemp
        global clHeart
        global clBreath
	print '\n\nIn main Thread'

        print "Name " + clName
	print "Temp " + clTemp
	print "Heart " + clHeart
	print "Breath " + clBreath
	self.campId1.setText(clCampId[0])
	self.name1.setText(clName)
	self.temp1.setText(clTemp)
	self.heart1.setText(clHeart)
	self.pressure1.setText(clBreath)
   	c.execute("INSERT INTO  table1(sNo,campId,name,heart,temp,pressure,serious,date,time) VALUES(?,?,?,?,?,?,?,?,?)",(1,clCampId[0],clName,clHeart,clTemp,clBreath,1,1,1))
	self.updateTable()
        conn.commit()
    def updateTable(self):
        #conn=sqlite3.connect("Midhun.db")
        #c=conn.cursor()
        c.execute("SELECT * FROM table1")
        allSQLRows= c.fetchall()
        
        self.table.setRowCount(len(allSQLRows)) ##set number of rows
        self.table.setColumnCount(9) ##this is fixed for myTableWidget, ensure that both of your tables, sql and qtablewidged have the same number of columns
                
        row = 0
               
                
        c.execute("SELECT * FROM table1")
        cur = c.fetchall()   
        for i,row in enumerate(cur):
            for j,val in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(val))) 
         
    


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
	self.emit(SIGNAL("log(QString)"),"Server Started\n")

	global clCampId	
	global clName
	global clTemp
        global clHeart
        global clBreath

	while True:
		clName,addr = s.recvfrom(1024)		
		clTemp,addr = s.recvfrom(1024)
		clHeart,addr = s.recvfrom(1024)
		clBreath,addr = s.recvfrom(1024)
		clCampId = addr
		print "message from:" + str(addr)
		self.emit(SIGNAL("log(QString)"),"Data received from "+ str(addr) +"\n")
		self.emit(SIGNAL("updateUi"))

	"""clName = '10'
	clTemp = '20'
        clHeart = '30'
        clBreath = '40'
	addr=10000"""

	
	"""print "name " + clName		
	print "Temp " + clTemp
	print "heart " + clHeart
	print "breath " + clBreath"""
        


if __name__ == "__main__":
    conn = sqlite3.connect("Database.db")
    c=conn.cursor()
    try:
        c.execute("CREATE TABLE table1(sNo INT,campId TEXT,name TEXT,heart TEXT,temp TEXT,pressure TEXT,serious TEXT,date TEXT,time TEXT)")
    except Exception as e:
        print e
        pass
    
    app = QApplication(sys.argv)

    window = myWindow()

    window.show()
	
    app.exec_()




