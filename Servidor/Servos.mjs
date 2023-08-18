export class Servos {
  constructor() {
    this.Servos = []
    for (let i = 1; i <= 12; i++) {
      const Servo = {
        NumServo: i,
        Sensor: 0,
        Actuator: 0
      }
      this.Servos.push(Servo)
    }
  }

  // Retornar el indice del servo
  findIndexServo(NumServo) {
    const IndexServo = this.Servos.findIndex((Servo) => Servo.NumServo === NumServo)
    return IndexServo
  }

  /* ----------------- Funciones para Sensores ------------------ */

  // Retorna los valores de los sensores del objeto que recibe
  getServosSensor(ServosSensors) {
    const response = ServosSensors.map((Servo) => {
      const IndexServo = this.findIndexServo(Servo.NumServo)
      const ServoFound = this.Servos[IndexServo]
      const responseServo = { NumServo: ServoFound.NumServo, Sensor: ServoFound.Sensor }
      return responseServo
    })
    return response
  }

  // Guarda los valores de los sensores del objeto que recibe
  setServosSensors(ServosSensors) {
    ServosSensors.forEach(Servo => {
      const IndexServo = this.findIndexServo(Servo.NumServo)
      this.Servos[IndexServo].Sensor = Servo.Sensor
    })
  }

  /* ----------------- Funciones para Actuadores ------------------ */

  // Retorna los valores de los actuadores del objeto que recibe
  getServosActuator(ServosActuators) {
    const response = ServosActuators.map((Servo) => {
      const IndexServo = this.findIndexServo(Servo.NumServo)
      const ServoFound = this.Servos[IndexServo]
      const responseServo = { NumServo: ServoFound.NumServo, Actuator: ServoFound.Actuator }
      return responseServo
    })
    return response
  }

  // Guarda los valores de los actuadores del objeto que recibe
  setServosActuator(ServosActuators) {
    ServosActuators.forEach(Servo => {
      const IndexServo = this.findIndexServo(Servo.NumServo)
      this.Servos[IndexServo].Actuator = Servo.Actuator
    })
  }
}
