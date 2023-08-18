export class SensorsForce {
  constructor () {
    this.SensorsForce = []
    for (let i = 1; i <= 8; i++) {
      const SensorForce = {
        NumSensorForce: i,
        Force: 0
      }
      this.SensorsForce.push(SensorForce)
    }
  }

  // Retornar el indice del servo
  findIndexSensorForce (NumSensorForce) {
    const IndexSensorForce = this.SensorsForce.findIndex((SensorForce) => SensorForce.NumSensorForce === NumSensorForce)
    return IndexSensorForce
  }

  /* ----------------- Funciones para Sensores ------------------ */

  // Retorna los valores de los sensores del objeto que recibe
  getSensorsForce (sensorsForce) {
    const response = sensorsForce.map((SensorForce) => {
      const IndexSensorForce = this.findIndexSensorForce(SensorForce.NumSensorForce)
      const SensorForceFound = this.SensorsForce[IndexSensorForce]
      const responseSensorForce = { NumSensorForce: SensorForceFound.NumSensorForce, Force: SensorForceFound.Force }
      return responseSensorForce
    })
    return response
  }

  // Guarda los valores de los sensores del objeto que recibe
  setSensorsForce (sensorsForce) {
    sensorsForce.forEach(sensorForce => {
      const IndexSensorForce = this.findIndexSensorForce(sensorForce.NumSensorForce)
      this.SensorsForce[IndexSensorForce].Force = sensorForce.Force
    })
  }
}
