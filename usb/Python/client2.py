import socket

def Main():
    host='127.0.0.1'
    port=5000

    s=socket.socket()
    s.connect((host,port))
    print '---->Server2'
    message=raw_input("->")
    while message!='q':
        s.send(message)
        data=s.recv(1024)
        print 'Received data from server: '+str(data)
        message=raw_input("->")
    s.close()

if __name__=='__main__':
    Main()
