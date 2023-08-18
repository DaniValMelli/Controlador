#include "Arduino.h"
#include <Servo.h>

class Servomotor {
  private:
    Servo servo;
    int NumServo;
    int PinSensor;
    int PinActuator;
    float Sensor;
    float Actuator;

  public:
    Servomotor( int NUM_SERVO, int PIN_SENSOR, int PIN_ACTUATOR ){
      NumServo = NUM_SERVO;
      PinSensor = PIN_SENSOR;
      PinActuator = PIN_ACTUATOR;
      Sensor = 0;
      Actuator = 0;
    }

    void activateActuador(){
      servo.attach(PinActuator);
    }

    void deactivateActuador(){
      servo.detach();
    }

    float getSensor(){
      return Sensor;
    }

    void setActuator( float value ){
      int microSeconds = 544 + 11.2484848*value;
      if(microSeconds < 544){
        microSeconds = 544;
      }else if(microSeconds > 2400){
        microSeconds = 2400;
      }
      servo.writeMicroseconds(microSeconds);
    }

    void readSensor(){
      int AnalogRead = analogRead(PinSensor);
      Sensor = 190.09901 - 0.316831*AnalogRead;
      if(Sensor < 0.0){
        Sensor = 0.0;
      }else if(Sensor > 165.0){
        Sensor = 165.0;
      }
    }
};