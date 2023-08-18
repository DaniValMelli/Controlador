import time
import RobotServices as robot

Servomotor = 1
ADDR_MCU = 11

timepoAnterior = time.time_ns()
Value = robot.getSensor(Servomotor,ADDR_MCU)
tiempo = time.time_ns()

diferenciaTiempo = tiempo - timepoAnterior
print("ADDR_MCU: ", ADDR_MCU, " - ", "Value: ", Value, "time: ", diferenciaTiempo)
