from Servos import Servos
import time, math
import Controlador as PID

servos = Servos()


# ------------  Offsets posicion bipedestacion estatica ---------------
def PosicionInicialRobot():
  servosActuator = [
    {
      "NumServo" : 1,
      "Actuator" : 85.0
    },
    {
      "NumServo" : 2,
      "Actuator" : 85.0
    },
    {
      "NumServo" : 3,
      "Actuator" : 80.0
    },
    {
      "NumServo" : 4,
      "Actuator" : 31.0
    },
    {
      "NumServo" : 5,
      "Actuator" : 75.0
    },
    {
      "NumServo" : 6,
      "Actuator" : 78.0
    },
    {
      "NumServo" : 7,
      "Actuator" : 76.0
    },
    {
      "NumServo" : 8,
      "Actuator" : 90.0
    },
    {
      "NumServo" : 9,
      "Actuator" : 90.0
    },
    {
      "NumServo" : 10,
      "Actuator" : 140.0
    },
    {
      "NumServo" : 11,
      "Actuator" : 78.0
    },
    {
      "NumServo" : 12,
      "Actuator" : 80.0
    }
  ]
  
  for servo in servosActuator:
    auxActivateServomotor = []
    auxActivateServomotor.append(servo)
    servos.activateServomotor(auxActivateServomotor)
    time.sleep(0.5)
PosicionInicialRobot()

def setAccionControl(accionControl):
  OFFSET_SERVOMOTOR_5 = 75.0
  OFFSET_SERVOMOTOR_11 = 78.0

  actuatorServomotor5 = OFFSET_SERVOMOTOR_5 + accionControl
  if actuatorServomotor5 > 165.0:
    actuatorServomotor5 = 165.0
  elif actuatorServomotor5 < 0.0:
    actuatorServomotor5 = 0.0
  
  actuatorServomotor11 = OFFSET_SERVOMOTOR_11 - accionControl
  if actuatorServomotor11 > 165.0:
    actuatorServomotor11 = 165.0
  elif actuatorServomotor11 < 0.0:
    actuatorServomotor11 = 0.0
  

  servoActuator = [
    {
      "NumServo" : 5,
      "Actuator" : actuatorServomotor5
    },
    {
      "NumServo" : 11,
      "Actuator" : actuatorServomotor11
    }
  ]

  servos.setServosActuator(servoActuator)

# ------------  Inicializacion de variables ---------------
salidaAnterior = 0
errorAcumulado = 0
errorAnterior = 0
tiempoAnterior_ns = time.time_ns()
vectorMediana = [7,7,7,7]


print("Inicializacion terminada")
time.sleep(10)
print("Controlando")

while True:

  salida, vectorMediana = servos.readMPU(vectorMediana)
  [accionControl, salidaAnterior, tiempoAnterior_ns, errorAcumulado, errorAnterior] = PID.controlador( salida, salidaAnterior, tiempoAnterior_ns, errorAcumulado, errorAnterior )
  setAccionControl(accionControl)
