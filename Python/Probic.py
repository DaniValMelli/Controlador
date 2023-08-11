from Servos import Servos
import time

servos = Servos()
AllListServos = servos.getListServos()

while True:
  ServosSensors = servos.getServosSensor(AllListServos)
  servos.setServerServosSensors(ServosSensors)
  time.sleep(1)