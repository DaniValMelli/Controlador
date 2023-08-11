#include <Servo.h>

// Objeto manejo servo
Servo SERVO_1;
Servo SERVO_2;
Servo SERVO_3;

// Pines pwm control servos
const int PIN_SET_SERVO_1 = 9;
const int PIN_SET_SERVO_2 = 10;
const int PIN_SET_SERVO_3 = 11;

// Pines lectura angulo servos
const int PIN_GET_SERVO_1 = A0;
const int PIN_GET_SERVO_2 = A1;
const int PIN_GET_SERVO_3 = A2;

//Variables globales
int Servo, Angulo, Grafica;

void setup() {
  Serial.begin(9600);

  SERVO_1.attach(PIN_SET_SERVO_1);
  SERVO_2.attach(PIN_SET_SERVO_2);
  SERVO_3.attach(PIN_SET_SERVO_3);
}

void loop() {
  if(Serial.available()){
    Lectura();
  }
  Graficar();
}

void Lectura() {
  Serial.readString();
  delay(500);
  Servo = LeerDato("Selecciona el servo (1, 2 o 3): ");
  Angulo = LeerDato("Digita el angulo al que quieres mover: ");
  Grafica = LeerDato("Que grafica va a mostrar: ");
  MoverServo();
}

int LeerDato(String msg){
  boolean bandera = false;
  String Data;
  
  Serial.println(msg);
  while(!bandera){
    if(Serial.available()){
      Data = Serial.readString();
      bandera = true;
    }
  }
  return Data.toInt();
}

void MoverServo(){
  if(Servo == 1){
    SERVO_1.write(Angulo);
  }

  if(Servo == 2){
    SERVO_2.write(Angulo);
  }

  if(Servo == 3){
    SERVO_3.write(Angulo);
  }
}

void Graficar() {
  int pos;
  const int limitSuperior = 650;
  const int limitInferior = 300;

  int pos1 = analogRead(PIN_GET_SERVO_1);
  int pos2 = analogRead(PIN_GET_SERVO_2);
  int pos3 = analogRead(PIN_GET_SERVO_3);

  if (Grafica == 1){
    pos = pos1;
  }
  if (Grafica == 2){
    pos = pos2;
  }
  if (Grafica == 3){
    pos = pos3;
  }

  Serial.print(pos);
  Serial.print(",");
  Serial.print(limitSuperior);
  Serial.print(",");
  Serial.println(limitInferior);
  delay(10);
}
