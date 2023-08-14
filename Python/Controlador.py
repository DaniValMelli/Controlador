
SETPOINT = 0
OFFSET = 90

KP = 0
KI = 0
KD = 0

errorAnterior = 0

def accionProporcional( error ):
  accionProporcional = KP * error
  return accionProporcional

def accionIntegral( error ):
  accionProporcional = KP * error
  return accionProporcional

def accionDerivativa( error ):
  accionProporcional = KP * error
  return accionProporcional

def controlador( salida ):
  
  error = SETPOINT - salida
  AccionControl = OFFSET + accionProporcional(error) + accionIntegral(error) + accionDerivativa(error)
  errorAnterior = error


