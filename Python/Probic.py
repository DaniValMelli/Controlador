from Servos import Servos
import time

servos = Servos()
allListServos = servos.getListServos(range(1,13))

listServos = servos.getListServos([1,2,3,7,8,9])
servosSensors = servos.getServosSensor(listServos)
servosActuator = []
for servo in servosSensors:
  servosActuator.append({ "NumServo": servo["NumServo"], "Actuator": servo["Sensor"] })

servos.activateServomotor(servosActuator)
servos.setServerServosActuator(servosActuator)

while True:
  ServosSensors = servos.getServosSensor(allListServos)
  servos.setServerServosSensors(ServosSensors)
  listServos = servos.getServerServosActuator(listServos)
  servos.setServosActuator(listServos)
  time.sleep(0.1)