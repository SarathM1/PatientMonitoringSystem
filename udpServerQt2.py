from PyQt4.QtCore import  *
from PyQt4.QtGui import *
import sqlite3
#from PySide.QtCore import *
#from PySide.QtGui import *
import sys
import socket
import threading 

import server

clName = '0'                                          #Defenition of global variable
clTemp = '0'
clPulse = '0'
clBpd = '0'
clBps = '0'
clCampId = '0'


class myWindow(QMainWindow,server.Ui_MainWindow):
    def __init__(self,parent=None):
        super(myWindow,self).__init__(parent)

        self.setupUi(self)
	self.updateTable()
        self.connect(self.run,SIGNAL("clicked()"),self.settings)
        #self.process_column()

    def settings(self):
        servIp = str(self.serverIp.text()) 
        servPort= int(self.serverPort.text())
	self.thread1=workerThread(self,servIp,servPort)
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
        global clPulse
        global clBpd
        global clBps
	print '\n\nIn main Thread'

        print "Name " + clName
	print "Temp " + clTemp
	print "Pulse " + clPulse
	print "BPD " + clBpd
	print "BPS " + clBps
	self.campId.setText(clCampId[0])
	self.name.setText(clName)
	self.temp.setText(clTemp)
	self.pulse.setText(clPulse)
	self.bpd.setText(clBpd)
	self.bps.setText(clBps)
   	c.execute("INSERT INTO  table1(sNo,campId,name,temp,pulse,bpd,bps,date,time) VALUES(?,?,?,?,?,?,?,?,?)",(1,clCampId[0],clName,clTemp,clPulse,clBpd,clBps,1,1))
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
	try:        
	    self.process_column()
	except Exception as e:
	    QMessageBox.warning(None,QString("Error!!"),QString(str(e)))
	    pass 
    def process_column(self, processCol=4):
        print 'In process_column()'
        print 'row_count = ' + str(self.table.rowCount())
        data=self.table.item(1,3).text()
        #print 'element(1,3) = ' + str(data)
        #if (int(data) >= 20):
           # self.table.item(1,3).setBackground(QBrush(Qt.yellow))
        for row in xrange(self.table.rowCount()):
            #print row
            item = self.table.item(row, 3)
            text = str(item.text())
            #print 'item [' + str(row) + ',' + '3] = ' + text
            if (int(text) >= 20):
                item.setBackground(QBrush(Qt.yellow))
    


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

	global clTemp	
	global clName
	global clBpd
        global clBps
        global clPulse

	while True:
		clName,addr = s.recvfrom(1024)		
		clTemp,addr = s.recvfrom(1024)
		clPulse,addr = s.recvfrom(1024)
		clBpd,addr = s.recvfrom(1024)
		clBps,addr = s.recvfrom(1024)
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
        c.execute("CREATE TABLE table1(sNo INT,campId TEXT,name TEXT,temp TEXT,pulse TEXT,bpd TEXT,bps TEXT,date TEXT,time TEXT)")
    except Exception as e:
        print e
        pass
    
    app = QApplication(sys.argv)

    window = myWindow()

    window.show()
	
    app.exec_()




