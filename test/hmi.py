import minimalmodbus
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL= True

import serial
import time

def Main():
    instrument = minimalmodbus.Instrument('/dev/ttyS0',2)
    instrument.debug = True
    instrument.serial.baudrate = 9600
    instrument.serial.bytesize = 8
    instrument.serial.parity = serial.PARITY_EVEN
    instrument.serial.stopbits = 1
    instrument.serial.timeout = 10
    instrument.mode = minimalmodbus.MODE_RTU
    print(instrument)
    time.sleep(1)
    try:
        heart = instrument.read_register(40001,functioncode=3)
        print heart
    except Exception as e:
        print e
    #heart = hmi.read()
    try:
        while(not heart):
            heart = instrument.read_register(40002)
            print heart
            time.sleep(0.5)
        print 'Heart rate in bps: ' + heart
    except:
        pass
if __name__ == '__main__':
    Main()
