import socket

def Main():
    host = '127.0.0.1'
    port = 5001

    server = ('127.0.0.1',5000)
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    
#    message = 's'
 #   s.sendto(message,server)
    #while message != 'q':
    while True:
	name = raw_input("message ->")	
	temp = raw_input("temp ->")
	heart = raw_input("heart ->")
	breath = raw_input("breath ->")
	
	s.sendto(name,server)
	s.sendto(temp,server)
	s.sendto(heart,server)
	s.sendto(breath,server)
	
	"""s.sendto('10',server)
	s.sendto('20',server)
	s.sendto('30',server)
	s.sendto('40',server)"""                   
	
    s.close()

if __name__=='__main__':
    Main()
