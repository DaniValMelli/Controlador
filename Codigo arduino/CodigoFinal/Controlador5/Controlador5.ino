#include <Wire.h>
#include "Servomotor.h"

// Direccion MCU
const byte ADDR = 15;

// ------------- pines inicializacion servos

// Identificador de motor
const byte NUM_SERVOMOTOR_1 = 10;

// Pines para leer sensores
const int PIN_SENSOR_SERVOMOTOR_1 = A2;

// Pines mover motores
const int PIN_ACTUATOR_SERVOMOTOR_1 = 9;

//Inicializacion servomotores
Servomotor Servomotor1(NUM_SERVOMOTOR_1,PIN_SENSOR_SERVOMOTOR_1,PIN_ACTUATOR_SERVOMOTOR_1);

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
  handleRequest(data);
}

void handleRequest(byte data[5]) {
  
  boolean bandera = true;

  if( data[1] != GET_SERVOMOTOR && data[1] != SET_SERVOMOTOR && data[1] != ACTIVATE_SERVOMOTOR && data[1] != DEACTIVATE_SERVOMOTOR) { bandera = false; }
  if( data[2] != NUM_SERVOMOTOR_1) { bandera = false; }

  if ( bandera == true ){
    response = OK;

    request = data[1];
    servomotor = data[2];
    value = data[3] + float(data[4])/100;
  }

}

void requestEvent() {

  makeRequest();

  byte message[3];

  int integerValueMessage = int(value);
  int decimalValueMessage = round((value - integerValueMessage) * 100);

  message[0] = response;
  message[1] = integerValueMessage;
  message[2] = decimalValueMessage;
  Wire.write(message, 3);

  response = ERROR;
}

void makeRequest(){
  
  // requests the reading of the angular position sensor of the servomotor
  if ( request == GET_SERVOMOTOR ){

    if( servomotor == NUM_SERVOMOTOR_1 ){
      value = Servomotor1.getSensor();
    }

  //  requests to move the servo motor to an angular position
  } else if ( request == SET_SERVOMOTOR ){

    if( servomotor == NUM_SERVOMOTOR_1 ){
      Servomotor1.setActuator(value);
      value = 0.0;
    }
    
  }else if ( request == ACTIVATE_SERVOMOTOR ){

    if( servomotor == NUM_SERVOMOTOR_1 ){
      Servomotor1.activateActuador();
      Servomotor1.setActuator(value);
    }

  }else if ( request == DEACTIVATE_SERVOMOTOR ){

    if( servomotor == NUM_SERVOMOTOR_1 ){
      Servomotor1.deactivateActuador();
    }

  }


}

void LeerSensores(){
  Servomotor1.readSensor();
}

