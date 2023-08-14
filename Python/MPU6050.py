import smbus2					#import SMBus module of I2C
import time

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

bus = smbus2.SMBus(1) 	# or buACCEL_ZOUT_Hs = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

def MPU_Init():

  #write to sample rate register
  bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
  time.sleep(0.0001)

  #Write to power management register
  bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
  time.sleep(0.0001)

  #Write to Configuration register
  bus.write_byte_data(Device_Address, CONFIG, 0)
  time.sleep(0.0001)

  #Write to Gyro configuration register
  bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
  time.sleep(0.0001)

  #Write to interrupt enable register
  bus.write_byte_data(Device_Address, INT_ENABLE, 1)
  time.sleep(0.0001)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
  high = bus.read_byte_data(Device_Address, addr)
  time.sleep(0.0001)
  low = bus.read_byte_data(Device_Address, addr+1)
  time.sleep(0.0001)

  #concatenate higher and lower value
  value = ((high << 8) | low)
  
  #to get signed value from mpu6050
  if(value > 32768):
    value = value - 65536
  return value

def readAccelerationX():
  return read_raw_data(ACCEL_XOUT_H)

def readAccelerationY():
  return read_raw_data(ACCEL_YOUT_H)

def readAccelerationZ():
  return read_raw_data(ACCEL_ZOUT_H)

MPU_Init()