import socket
import minimalmodbus
import serial
import time

def Main():
    host = '127.0.0.1'
    port = 5001

    server = ('127.0.0.1',5000)
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    
#    message = 's'
 #   s.sendto(message,server)
    #while message != 'q':
    oldBreath=0
    while True:
	
	name = raw_input("message ->")	
	temp = raw_input("temp ->")
	heart = raw_input("heart ->")
	breath = raw_input("breath ->")
	
	#newBreath = instrument.read_register(4105)
    	#newHeart = instrument.read_register(4106)
    	#level3 = instrument.read_register(4107)
	print 'newBreath' + str(breath)
	#check = newBreath - oldBreath
	#print 'check= '+ str(check)
	#if check != 0:
        #oldBreath = newBreath
        #print 'oldBreath= ' + str(oldBreath)
        print 'newHeart= ' + str(heart)
        s.sendto(name,server)
        s.sendto(temp,server)
        s.sendto(str(heart),server)
        s.sendto(str(breath),server)

	"""s.sendto('10',server)
	s.sendto('20',server)
	s.sendto('30',server)
	s.sendto('40',server)"""                   
	
    s.close()

if __name__=='__main__':
    """instrument = minimalmodbus.Instrument('/dev/ttyUSB0',2)
    #instrument.debug = True
    instrument.serial.baudrate = 9600
    instrument.serial.bytesize = 7
    instrument.serial.parity = serial.PARITY_EVEN
    instrument.serial.stopbits = 1
    instrument.serial.timeout = 1
    instrument.mode = minimalmodbus.MODE_ASCII"""
    Main()
