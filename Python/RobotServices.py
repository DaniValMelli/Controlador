import smbus2
import math

bus = smbus2.SMBus(1)

# Type of request
GET_SENSOR = 1
SET_ACTUATOR = 2
ACTIVATE_SERVOMOTOR = 3
DEACTIVATE_SERVOMOTOR = 4

# Type of response
SUCCESSFUL = 1
ERROR = 2
  
def sendRequestRobot(Request, Servomotor, Value, ADDR_MCU):

  decimalValue, integerValue = math.modf(Value)
  integerValue = math.trunc(integerValue)
  decimalValue = math.trunc(round(decimalValue,2)*100)

  message = [Request,Servomotor,integerValue,decimalValue]

  response = 0
  value = 0.0

  try:
    bus.write_i2c_block_data(ADDR_MCU,0,message)
    auxResponse = bus.read_i2c_block_data(ADDR_MCU, 0, 3)
    response = auxResponse[0]
    integerValue = auxResponse[1]
    decimalValue = (auxResponse[2])/100
    value = integerValue + decimalValue
  except Exception as e:
    print("Servomotor: ", Servomotor ,"Error: ",e)

  return [response, value]


def getSensor(Servomotor, ADDR_MCU):
  [response, value] = sendRequestRobot(GET_SENSOR, Servomotor, 0.0, ADDR_MCU)
  return value

def setActuator(Servomotor, Value, ADDR_MCU):
  [response, value] = sendRequestRobot(SET_ACTUATOR, Servomotor, Value, ADDR_MCU)
  
def activateActuator(Servomotor, Value, ADDR_MCU):
  [response, value] = sendRequestRobot(ACTIVATE_SERVOMOTOR, Servomotor, Value, ADDR_MCU)

def deactivateActuator(Servomotor, ADDR_MCU):
  [response, value] = sendRequestRobot(DEACTIVATE_SERVOMOTOR, Servomotor, 0.0, ADDR_MCU)

  