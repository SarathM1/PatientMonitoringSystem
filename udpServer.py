import socket

def Server():    	
	host = '127.0.0.1'
        port = 5000

        s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind((host,port))
	
	print "Server Started"

	
	global clTemp
        global clHeart
        global clBreath

	#test = 's'
	#print "test cahr outside loop: " + test
	#while test != 'q':
	while True:
	
		name,addr = s.recvfrom(1024)		
		clTemp,addr = s.recvfrom(1024)
		clHeart,addr = s.recvfrom(1024)
		clBreath,addr = s.recvfrom(1024)

		print "message from:" + str(addr)
		print "name" + name		
		print "Temp " + clTemp
		print "heart " + clHeart
		print "breath " + clBreath
	
if __name__== '__main__':
	Server()

