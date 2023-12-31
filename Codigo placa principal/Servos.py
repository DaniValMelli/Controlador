import ServerServices as server
import RobotServices as robot
import numpy as np

class Servos:

  def __init__ (self):
    self.Servos = [
      {
        "NumServo" : 1,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 11
      },
      {
        "NumServo" : 2,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 11
      },
      {
        "NumServo" : 3,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 11
      },
      {
        "NumServo" : 4,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 12
      },
      {
        "NumServo" : 5,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 13
      },
      {
        "NumServo" : 6,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 13
      },
      {
        "NumServo" : 7,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 14
      },
      {
        "NumServo" : 8,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 14
      },
      {
        "NumServo" : 9,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 14
      },
      {
        "NumServo" : 10,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 15
      },
      {
        "NumServo" : 11,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 16
      },
      {
        "NumServo" : 12,
        "Sensor" : 0.0,
        "Actuator" : 0.0,
        "MicroController" : 16
      }
    ]

  # Retornar el indice del servo
  def findIndexServo(self,NumServo):
    for i, servo in enumerate(self.Servos):
      if servo["NumServo"] == NumServo:
        return i

  # """----------------- Funcion devuelve los numServos de todos los servos ------------------"""

  def getListServos(self,listServos):
    response = []
    for numServo in listServos:
      for servo in self.Servos:
        if numServo == servo["NumServo"]:
          response.append(servo)
    return response
    

  # """--------------------------- Funciones para Sensores ---------------------------------"""

  # Retorna los valores de los sensores del objeto que recibe
  def getServosSensor(self, listServos):
    response = []
    for servo in listServos:

      IndexServo = self.findIndexServo(servo["NumServo"])
      ServoFound = self.Servos[IndexServo]

      readingSensor = robot.getSensor(ServoFound["NumServo"],ServoFound["MicroController"])
      ServoFound["Sensor"] = readingSensor

      responseServo = { "NumServo": ServoFound["NumServo"], "Sensor": ServoFound["Sensor"] }
      response.append(responseServo)
    return response

  # Guarda los valores de los sensores del objeto que recibe
  def setServosSensors(self, ServosSensors):
    for servo in ServosSensors:
      IndexServo = self.findIndexServo(servo.get("NumServo"))
      self.Servos[IndexServo]["Sensor"] = servo["Sensor"]


  # """--------------------------- Funciones para Actuadores -------------------------------"""

  # Retorna los valores de los actuadores del objeto que recibe
  def getServosActuator(self, ServosActuators):
    response = []
    for servo in ServosActuators:
      IndexServo = self.findIndexServo(servo["NumServo"])
      ServoFound = self.Servos[IndexServo]
      responseServo = { "NumServo": ServoFound["NumServo"], "Actuator": ServoFound["Actuator"] }
      response.append(responseServo)
    return response


  # Guarda los valores de los actuadores del objeto que recibe
  def setServosActuator(self, ServosActuators):
    for servo in ServosActuators:
      IndexServo = self.findIndexServo(servo["NumServo"])
      self.Servos[IndexServo]["Actuator"] = servo["Actuator"]
      ServoFound = self.Servos[IndexServo]
      robot.setActuator(ServoFound["NumServo"],ServoFound["Actuator"],ServoFound["MicroController"])
  

  # ---------------------------- Comunicacion con el servidor ---------------------------------

  def setServerServosSensors(self, ServosSensors):
    server.setServosSensors(ServosSensors)

  def getServerServosActuator(self, ListServos):
    ServosActuators = server.getServosActuators(ListServos)
    return ServosActuators

  def setServerServosActuator(self,ServosActuators):
    server.setServosActuators(ServosActuators)

  # ---------------------------- Comunicacion con el robot ---------------------------------

  def activateServomotor(self,Servos):
    for servo in Servos:
      IndexServo = self.findIndexServo(servo["NumServo"])
      self.Servos[IndexServo]["Actuator"] = servo["Actuator"]
      ServoFound = self.Servos[IndexServo]
      robot.activateActuator(ServoFound["NumServo"],ServoFound["Actuator"],ServoFound["MicroController"])

  def deactivateServomotor(self,Servos):
    for servo in Servos:
      IndexServo = self.findIndexServo(servo["NumServo"])
      ServoFound = self.Servos[IndexServo]
      robot.deactivateActuator(ServoFound["NumServo"],ServoFound["MicroController"])

  def readMPU(self, vectorMediana):
    vectorMediana = [ vectorMediana[1], vectorMediana[2], vectorMediana[3], robot.readMPU() ]
    angulo = np.median(vectorMediana)
    
    return ( angulo, vectorMediana )
