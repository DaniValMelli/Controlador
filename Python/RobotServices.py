import smbus2
import MPU6050
import math
import time

bus = smbus2.SMBus(1)
time.sleep(2)

# Type of request
GET_SENSOR = 1
SET_ACTUATOR = 2
ACTIVATE_SERVOMOTOR = 3
DEACTIVATE_SERVOMOTOR = 4

# Type of response
SUCCESSFUL = 1
ERROR = 2

def sendWrite( Request, Servomotor, Value, ADDR_MCU ):
  decimalValue, integerValue = math.modf(Value)
  integerValue = math.trunc(integerValue)
  decimalValue = math.trunc(round(decimalValue,2)*100)

  message = [Request,Servomotor,integerValue,decimalValue]

  try:
    bus.write_i2c_block_data(ADDR_MCU,0,message)
  except Exception as e:
    print("Servomotor: ", Servomotor ,"Error: ",e)

  time.sleep(0.0001)
  
  
def sendRead( Servomotor, ADDR_MCU ):
  auxResponse = []
  value = 0.0
  try:
    auxResponse = bus.read_i2c_block_data(ADDR_MCU,Servomotor,3)
    breakpoint()
    integerValue = auxResponse[1]
    decimalValue = (auxResponse[2])/100
    value = integerValue + decimalValue
  except Exception as e:
    print("Servomotor: ", Servomotor ,"Error: ",e)

  time.sleep(0.0001)

  return value


def getSensor(Servomotor, ADDR_MCU):
  value = sendRead( Servomotor, ADDR_MCU )
  return value

def setActuator(Servomotor, Value, ADDR_MCU):
  sendWrite(SET_ACTUATOR, Servomotor, Value, ADDR_MCU)
  
def activateActuator(Servomotor, Value, ADDR_MCU):
  sendWrite(ACTIVATE_SERVOMOTOR, Servomotor, Value, ADDR_MCU)

def deactivateActuator(Servomotor, ADDR_MCU):
  sendWrite(DEACTIVATE_SERVOMOTOR, Servomotor, 0.0, ADDR_MCU)

def readMPU():
  
  acc_y,acc_z = 0
  for i in range(0,20):
    acc_y += MPU6050.readAccelerationY()
    acc_z += MPU6050.readAccelerationZ()

  acc_y /= 20
  acc_z /= 20
  angulo = math.degrees(math.atan(acc_z/acc_y))
  
  print("Angulo: ", angulo)
        
