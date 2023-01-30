# exec(open("i2cscan.py").read())

from machine import I2C 
print("I2C scanning...")
i2c = I2C(I2C.MASTER, pins = ('P9','P10') , baudrate = 400000 )
slaves = i2c.scan()
for slave in slaves : 
    print('slave address :{}'.format(hex(slave)))
    



