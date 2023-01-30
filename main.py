from imu import MPU6050
from time import sleep
from machine import Pin, I2C

i2c = I2C(I2C.MASTER, pins = ('P9','P10') , baudrate = 400000 )
imu = MPU6050(i2c)

while True:
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)
    tem=round(imu.temperature,2)
    #print('temperature: {} \r'.format(tem))  
    print("ax:",ax,"\t","ay:",ay,"\t","az:",az,"\t","gx",gx,"\t","gy",gy,"\t","gz",gz,"                ",end="\r")
    sleep(0.2)

    
