#include "Wire.h"

const byte I2C_SLAVE_ADDR = 12;

void setup()
{
  Serial.begin(9600);

  Wire.begin(I2C_SLAVE_ADDR);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

long data = 0;
long response = I2C_SLAVE_ADDR;

void receiveEvent(int bytes)
{
  data = 0;
  uint8_t index = 0;
  while (Wire.available())
  {
    byte* pointer = (byte*)&data;
    *(pointer + index) = (byte)Wire.read();
    index++;
  }
}

void requestEvent()
{
  Wire.write((byte*)&response, sizeof(response));
}

void loop() {

  if (data != 0)
  {
    Serial.println(data);
    data = 0;
  }
}