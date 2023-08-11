import express from 'express'
import { Servos } from './Servos.mjs'
import { SensorsForce } from './SensorsForce.mjs'

const PORT = 3000

const app = express()
app.use((req, res, next) => {
  if (req.method !== 'POST') return next()
  if (req.headers['content-type'] !== 'application/json; charset=UTF-8' && req.headers['content-type'] !== 'application/json') return next()

  let body = ''
  req.on('data', chunk => {
    body += chunk.toString()
  })
  req.on('end', () => {
    req.body = JSON.parse(body)
    next()
  })
})

app.post('/getServosSensors', (req, res) => {
  const response = servos.getServosSensor(req.body)
  res.status(200).json(response)
})

app.post('/setServosSensors', (req, res) => {
  servos.setServosSensors(req.body)
  console.log(servos)
  res.status(200).json({ ok: 'ok' })
})

app.post('/getServosActuators', (req, res) => {
  const response = servos.getServosActuator(req.body)
  res.status(200).json(response)
})

app.post('/setServosActuators', (req, res) => {
  servos.setServosActuator(req.body)
  console.log(servos)
  res.status(200).json({ ok: 'ok' })
})

app.post('/getSensorsForces', (req, res) => {
  const response = sensorsForce.getSensorsForce(req.body)
  res.status(200).json(response)
})

app.post('/setSensorsForces', (req, res) => {
  sensorsForce.setSensorsForce(req.body)
  console.log(sensorsForce)
  res.status(200).json({ ok: 'ok' })
})

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`)
})

const servos = new Servos()
const sensorsForce = new SensorsForce()
