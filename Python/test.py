import RobotServices as robot
import time 

while True:
  tiempoInicial = time.time_ns()
  robot.readMPU()
  tiempoFinal = time.time_ns()
  print("Tiempo: " , tiempoFinal - tiempoInicial)
  time.sleep(0.1)