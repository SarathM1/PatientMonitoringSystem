

import minimalmodbus
import serial
import time
import logging
       
instrument = minimalmodbus.Instrument('/dev/ttyUSB0',2)   # device id changed from 1 to 2
#instrument.debug = True
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 7
instrument.serial.parity = serial.PARITY_EVEN
instrument.serial.stopbits = 1
instrument.serial.timeout = 1
instrument.mode = minimalmodbus.MODE_ASCII
while True:
    
    level1 = instrument.read_register(4105)
    level2 = instrument.read_register(4106)
    level3 = instrument.read_register(4107)
    level4 = instrument.read_register(4108)
    print level1,level2,level3,level4
    #except Exception as e:
        #print(e)
    currentTime = time.strftime('%d/%m/%Y %H:%M:%S',time.gmtime())
    #packet = 'DGD001;' + str(level) + ';' + str(currentTime)+'\x1A' 
    #print packet
    time.sleep(1)

#print (e)
#print('\nProgram aborted because there is error in opening the serial port.\n' )
    
   
        
#instrument.read_register(289, 1)
