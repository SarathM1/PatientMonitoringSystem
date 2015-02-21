#!/usr/bin/python3

#import minimalmodbus

"""
Possible errors:
    1) For putty : Fix serial port permission denied error  (refer http://jesin.tk/fix-serial-port-permission-denied-errors-linux/)
    2) This code runs only on python3
    3) Check port : ttyS0/ttyUSB0
    4) Add current user to dialout (refer http://jesin.tk/fix-serial-port-permission-denied-errors-linux/)
    5) If you get a unicode error, check baud rate

"""
import serial
import time
import logging


class Sim900(object):
    def __init__ (self,port,baud=9600,bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stop=serial.STOPBITS_ONE, timeout=1):
        self.serialPort = serial.Serial(port,baud,bytesize,parity,stop,timeout)
    
    def sendAtCommand(self,command):
        self.serialPort.write(bytes(command+'\r\n',encoding='ascii'))
        self.status =  self.readCommandResponse()
        return self.status

    def readCommandResponse(self):
        time.sleep(1)
        while True:
            msg = self.serialPort.read(100).decode('ascii').strip()
            if msg:
                return msg
    
    def __del__(self):
        self.serialPort.close()
        
                

if __name__ == '__main__':
    try:
        """instrument = minimalmodbus.Instrument('/dev/ttyUSB1',1)
        instrument.serial.baudrate = 9600
        instrument.serial.bytesize = 7
        instrument.serial.parity = serial.PARITY_EVEN
        instrument.serial.stopbits = 1
        instrument.serial.timeout = 0.1
        instrument.mode = minimalmodbus.MODE_ASCII"""

        modem = Sim900('/dev/ttyS0')
        modem.sendAtCommand('AT')
        print (modem.status)
        modem.sendAtCommand('AT+CREG?')
        print (modem.status)
        modem.sendAtCommand('AT+CGATT=1')
        print (modem.status)
        modem.sendAtCommand('AT+CSTT="CMNET"')
        print (modem.status)
        modem.sendAtCommand('AT+CIICR')
        print (modem.status)
        modem.sendAtCommand('AT+CIFSR')
        print (modem.status)

        while True:
            modem.sendAtCommand('AT+CIPSTART="UDP","127.0.0.1","5000"')
            print (modem.status)
            modem.sendAtCommand('AT+CIPSEND')
            """level = instrument.read_register(4106)"""
            level= 30
            currentTime = time.strftime('%d/%m/%Y %H:%M:%S',time.gmtime())
            packet = 'DGD001;' + str(level) + ';' + str(currentTime)+'\x1A' 
            modem.sendAtCommand(packet)
            print (modem.status)
            modem.sendAtCommand('AT+CIPCLOSE')
            time.sleep(15)

    except serial.SerialException :
        print('\nProgram aborted because there is error in opening the serial port.\n' )
    
   
        
