import time

SETPOINT = 7.0

KP = 0.2
KI = 0.2 #0.2
KD = 0.01 #0.01

def Proporcional( error ):
  accionProporcional = KP * error
  return accionProporcional


def Integral( error, errorAcumulado, errorAnterior, tiempo ):
  errorAcumulado += ((error + errorAnterior)/2)*tiempo
  accionIntegral = KI * errorAcumulado
  return [ accionIntegral, errorAcumulado]


def Derivativa( salida, salidaAnterior, tiempo ):
  accionDerivativa = KD * (( salida - salidaAnterior )/tiempo)
  return accionDerivativa


def controlador( salida, salidaAnterior, tiempoAnterior_ns, errorAcumulado, errorAnterior ):

  error = SETPOINT - salida
  tiempo_ns = time.time_ns()
  tiempo = (tiempo_ns - tiempoAnterior_ns)/1000000000

  accionProporcional = Proporcional(error)
  [ accionIntegral, errorAcumulado] = Integral( error, errorAcumulado, errorAnterior, tiempo)
  accionDerivativa = Derivativa( salida, salidaAnterior, tiempo)

  accionControl = accionProporcional + accionIntegral - accionDerivativa

  errorAnterior = error
  salidaAnterior = salida
  tiempoAnterior_ns = tiempo_ns

  return [accionControl, salidaAnterior, tiempoAnterior_ns, errorAcumulado, errorAnterior]


