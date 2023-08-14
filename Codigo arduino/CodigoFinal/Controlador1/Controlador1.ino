#include <Wire.h>
#include "Servomotor.h"

// Direccion MCU
const byte ADDR = 11;

// ------------- pines inicializacion servos

// Identificador de motor
const byte NUM_SERVOMOTOR_1 = 1;
const byte NUM_SERVOMOTOR_2 = 2;
const byte NUM_SERVOMOTOR_3 = 3;

// Pines para leer sensores
const int PIN_SENSOR_SERVOMOTOR_1 = A1;
const int PIN_SENSOR_SERVOMOTOR_2 = A2;
const int PIN_SENSOR_SERVOMOTOR_3 = A0;

// Pines mover motores
const int PIN_ACTUATOR_SERVOMOTOR_1 = 3;
const int PIN_ACTUATOR_SERVOMOTOR_2 = 9;
const int PIN_ACTUATOR_SERVOMOTOR_3 = 10;

//Inicializacion servomotores
Servomotor Servomotor1(NUM_SERVOMOTOR_1,PIN_SENSOR_SERVOMOTOR_1,PIN_ACTUATOR_SERVOMOTOR_1);
Servomotor Servomotor2(NUM_SERVOMOTOR_2,PIN_SENSOR_SERVOMOTOR_2,PIN_ACTUATOR_SERVOMOTOR_2);
Servomotor Servomotor3(NUM_SERVOMOTOR_3,PIN_SENSOR_SERVOMOTOR_3,PIN_ACTUATOR_SERVOMOTOR_3);

// ----------- Instrucciones comunicacion raspberry

// type of request
const byte GET_SERVOMOTOR = 1;
const byte SET_SERVOMOTOR = 2;
const byte ACTIVATE_SERVOMOTOR = 3;
const byte DEACTIVATE_SERVOMOTOR = 4;

// type of response
const byte OK = 1;
const byte ERROR = 2;

// ---------- Variables globales

// handling requests and responses
byte request = 0;
byte response = ERROR;
byte servomotor = 0;
float value = 0.0;

void setup() {
  Wire.begin(ADDR);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() { 
  LeerSensores();
}

void receiveEvent(int numBytes) {

  byte data[5];
  int i = 0;
  while (Wire.available()) {
    data[i] = Wire.read();
    i++;
  }
  if (data[0] == 0){
    handleRequest(data);
  }else{
    servomotor = data[0];
  }
  
}

void handleRequest(byte data[5]) {
  
  boolean bandera = true;

  if( data[1] != SET_SERVOMOTOR && data[1] != ACTIVATE_SERVOMOTOR && data[1] != DEACTIVATE_SERVOMOTOR) { bandera = false; }
  if( data[2] != NUM_SERVOMOTOR_1 && data[2] != NUM_SERVOMOTOR_2 && data[2] != NUM_SERVOMOTOR_3) { bandera = false; }

  if ( bandera == true ){

    request = data[1];
    servomotor = data[2];
    value = data[3] + float(data[4])/100;

    makeRequest();
  }

}

void makeRequest(){
  
  if ( request == SET_SERVOMOTOR ){

    if( servomotor == NUM_SERVOMOTOR_1 ){
      Servomotor1.setActuator(value);
    }else if (servomotor == NUM_SERVOMOTOR_2) {
      Servomotor2.setActuator(value);
    }else if (servomotor == NUM_SERVOMOTOR_3) {
      Servomotor3.setActuator(value);
    }
    
  }else if ( request == ACTIVATE_SERVOMOTOR ){

    if( servomotor == NUM_SERVOMOTOR_1 ){
      Servomotor1.activateActuador();
      Servomotor1.setActuator(value);
    }else if (servomotor == NUM_SERVOMOTOR_2) {
      Servomotor2.activateActuador();
      Servomotor2.setActuator(value);
    }else if (servomotor == NUM_SERVOMOTOR_3) {
      Servomotor3.activateActuador();
      Servomotor3.setActuator(value);
    }

  }else if ( request == DEACTIVATE_SERVOMOTOR ){

    if( servomotor == NUM_SERVOMOTOR_1 ){
      Servomotor1.deactivateActuador();
    }else if (servomotor == NUM_SERVOMOTOR_2) {
      Servomotor2.deactivateActuador();
    }else if (servomotor == NUM_SERVOMOTOR_3) {
      Servomotor3.deactivateActuador();
    }

  }

}

void requestEvent() {

  returnSensor();
  byte message[3];

  int response = OK;
  int integerValueMessage = int(value);
  int decimalValueMessage = round((value - integerValueMessage) * 100);

  message[0] = response;
  message[1] = integerValueMessage;
  message[2] = decimalValueMessage;
  Wire.write(message, 3);

  response = ERROR;
}

void returnSensor() {
  if( servomotor == NUM_SERVOMOTOR_1 ){
    value = Servomotor1.getSensor();
  }else if (servomotor == NUM_SERVOMOTOR_2) {
    value = Servomotor2.getSensor();
  }else if (servomotor == NUM_SERVOMOTOR_3) {
    value = Servomotor3.getSensor();
  }
}

void LeerSensores(){
  Servomotor1.readSensor();
  Servomotor2.readSensor();
  Servomotor3.readSensor();
}

