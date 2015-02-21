import socket

def Main():
    host='0.0.0.0'
    port=5000
    s=socket.socket()
    s.bind((host,port))
    s.listen(2)
    
    (c,(ip,port))=s.accept()

    (c2,(ip2,port2))=s.accept()
    print 'client address: '+str(c)+','+str(ip)+','+str(port)

    print 'client2 address: '+str(c2)+','+str(ip2)+','+str(port2)
    while True:
        data=c.recv(1024)
        if not data:
            break
        print "from connected user: " + str(data)
        data=str(data).upper()
        print "Sending: "+str(data)
        c.send(data)

    c.close()
if __name__=='__main__':
    Main()

