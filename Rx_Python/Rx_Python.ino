const int Relay_Pin = 5;  // the number of the LED pin
int incomingByte = 0;
#include <Servo.h>
Servo myservo;   
int pos = 0;  
void setup(){
  Serial.begin(9600);
  pinMode(Relay_Pin, OUTPUT);
  myservo.attach(9);
}

void loop(){

  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    //Serial.println(incomingByte);
  }
  //Serial.println("3");
  if (incomingByte == 49)
  {
    digitalWrite(Relay_Pin, HIGH);
    
  }
  else
  {
    digitalWrite(Relay_Pin, LOW);    
  }

  delay(100);
}
