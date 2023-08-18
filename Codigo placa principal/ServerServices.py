import requests

HEADERS = {"Content-Type": "application/json"}

URL = "http://192.168.36.150:3000/"

URL_GET_SERVOS_SENSORS = URL + "getServosSensors"
URL_SET_SERVOS_SENSORS = URL + "setServosSensors"

URL_GET_SERVOS_ACTUATORS = URL + "getServosActuators"
URL_SET_SERVOS_ACTUATORS = URL + "setServosActuators"

def sendRequestServer(url,body):
  try:
    response = requests.post(url, json=body, headers=HEADERS)
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"Error en la petición: {e}")


def getServosSensors(body):
  return sendRequestServer(URL_GET_SERVOS_SENSORS,body)

def setServosSensors(body):
  return sendRequestServer(URL_SET_SERVOS_SENSORS,body)

def getServosActuators(body):
  return sendRequestServer(URL_GET_SERVOS_ACTUATORS,body)

def setServosActuators(body):
  return sendRequestServer(URL_SET_SERVOS_ACTUATORS,body)

  
