import smbus2
import time
import math

# Adress microcontrolador
ADDR_MCU = 0x10

bus = smbus2.SMBus(1)

def sendRequest(sendRequest, SendServomotor, sendValue): 
  requestMessage = sendRequest+1
  servomotorMessage = SendServomotor+1

  decimalValue, integerValue = math.modf(sendValue)
  integerValueMessage = math.trunc(integerValue) + 1
  decimalValueMessage = math.trunc(round(decimalValue,2)*100)+1

  message = [requestMessage,0,servomotorMessage,0,integerValueMessage,0,decimalValueMessage]

  try:
      bus.write_i2c_block_data(ADDR_MCU,0,message)
      response = bus.read_i2c_block_data(ADDR_MCU, 0, 1)
  except Exception as e:
      print("Error: ", e)

  return response

def requestData():
    request = int(input("Escriba la peticion (1 GetSensor o 2 SetActuator): ") or 0)
    print(request)
    servomotor = int(input("Seleccione el servomotor (1 o 2): ") or 0)
    print(servomotor)
    value = float(input("Digite el valor: ") or 0.0)
    print(value)

    return [request,servomotor,value]

while True:
    [request,servomotor,value] = requestData()
    response = sendRequest(request,servomotor,value)
    time.sleep(2)
