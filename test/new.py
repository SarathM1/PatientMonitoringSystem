#!/usr/bin/env python
import minimalmodbus
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True

instrument = minimalmodbus.Instrument('/dev/ttyS0', 2) # port name, slave address (in decimal)
instrument.debug = True
instrument.serial.baudrate = 9600
print(instrument)

print( instrument.read_register(40002, numberOfDecimals=1,functioncode=3))

