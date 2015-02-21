import socket
import threading
class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting "+self.name
        Main()
        print "Ending "+self.name

def Main():
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

    c.close()

host='0.0.0.0'
port=5000
s=socket.socket()
s.bind((host,port))
s.listen(2)

#threadLock=threading.Lock()
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
