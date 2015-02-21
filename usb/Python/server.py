import socket

def Main():
    host='0.0.0.0'
    port=5000
    print '1'
    s=socket.socket()#--object created
    s.bind((host,port))#--to bind host addr n port
    print '2'
    s.listen(2)#--can serve 2 clients
    print '3'
    
    c,addr=s.accept()#--accept conncn from client
    print '4'

    print 'client address: '+str(addr)

    while True:
        data=c.recv(1024)#--receive data
        if not data:
        	print str(data) +'data after closing'            
		break
        print "from connected user: " + str(data)
        data=str(data).upper()#--to convert to upper case
        print "Sending: "+str(data)
        c.send(data)#--to send data to client
    c.close()#--close the conncn
if __name__=='__main__':
    Main()

