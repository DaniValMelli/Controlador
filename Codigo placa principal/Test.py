from Servos import Servos
import time, math
import Controlador as PID

servos = Servos()
ListServos = servos.getListServos(range(0,13))

while True:
    servos.getServosSensor(ListServos)
  
  
