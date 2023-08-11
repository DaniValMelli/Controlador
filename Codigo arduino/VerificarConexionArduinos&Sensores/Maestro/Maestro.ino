#include <ArduinoJson.h>
#include <Wire.h>
#include <Adafruit_ADS1X15.h>

// Direccion MCU
const byte ADDR1 = 11;
const byte ADDR2 = 12;
const byte ADDR3 = 13;
const byte ADDR4 = 14;
const byte ADDR5 = 15;
const byte ADDR6 = 16;

// Direccion ADS1115
const byte ADDR_ADS1 = 0x49;
const byte ADDR_ADS2 = 0x48;

Adafruit_ADS1115 ADS1;
Adafruit_ADS1115 ADS2;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  inicializacionSensoresFuerza();
}

void loop() {
  requestToSlave(ADDR2);
  requestToSlave(ADDR3);
  requestToSlave(ADDR4);
  requestToSlave(ADDR5);
  requestToSlave(ADDR6);
  delay(2000);
}

void requestToSlave(byte ADDR){
  long data = 100;
  long response = 0;

  response = 0;
  Wire.requestFrom(ADDR, sizeof(response));

  uint8_t index = 0;
  byte* pointer = (byte*)&response;
  while (Wire.available())
  {
    *(pointer + index) = (byte)Wire.read();
    index++;
  }
  Serial.print("Arduino ");
  Serial.print(ADDR);
  Serial.print(": ");
  Serial.println(response);
}


void inicializacionSensoresFuerza(){
  Serial.println("Comienza inicializacion ADS");

  if(!ADS1.begin(ADDR_ADS1)){
    Serial.println("Failed to initialize ADS1.");
  }else{
    Serial.println("Initialize ADS1.");
  }

  if(!ADS2.begin(ADDR_ADS2)){
    Serial.println("Failed to initialize ADS2.");
  }else{
    Serial.println("Initialize ADS2.");
  }

  Serial.println("Finalizo inicializacion ADS");
}

void sensorAnalogico(Adafruit_ADS1115 ADS){
  int16_t adc0, adc1, adc2, adc3;

  adc0 = ADS.readADC_SingleEnded(0);
  adc1 = ADS.readADC_SingleEnded(1);
  adc2 = ADS.readADC_SingleEnded(2);
  adc3 = ADS.readADC_SingleEnded(3);
  Serial.print("AIN0: "); Serial.println(adc0);
  Serial.print("AIN1: "); Serial.println(adc1);
  Serial.print("AIN2: "); Serial.println(adc2);
  Serial.print("AIN3: "); Serial.println(adc3);
  Serial.println(" ");
}