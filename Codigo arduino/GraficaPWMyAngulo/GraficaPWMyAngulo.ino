#include <Servo.h>

Servo servo;


void setup() {
  Serial.begin(9600);
  servo.attach(11,400,2700);
}

void loop() {
  if(Serial.available()){
    String data = Serial.readString();
    int value = data.toInt();
    delay(500);
    servo.writeMicroseconds(value);
  }

  Serial.print(analogRead(A0));
  Serial.print(",");
  Serial.print(650);
  Serial.print(",");
  Serial.println(300);
}
