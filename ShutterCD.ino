// ShutterCD
//
// Copyright (C) 2022 Serhiy Kobyakov
//


#include <AccelStepper.h>

// Dynamics of the stepper motor
#define TheSpeed 30000.0
#define TheAcceleration 19000.0

// The stepper driver pins
#define STEPPER1_DIR_PIN 3
#define STEPPER1_STEP_PIN 2
#define MotorDisable 4

// Endstop pin
#define theEndStop A0

long long int steps; // motor step position
int count;           // just counter variable

int theMax=1950;     // maximum number of steps 
                     // for this particular linear actuator
                     // need to be checked for each new device!

// Define stepper and the pins it will use
AccelStepper stepper1(AccelStepper::DRIVER, STEPPER1_STEP_PIN, STEPPER1_DIR_PIN);


void setup()
// main setup routine
{
  pinMode(MotorDisable, OUTPUT);
  digitalWrite(MotorDisable, HIGH);
  stepper1.setMaxSpeed(TheSpeed);
  stepper1.setAcceleration(TheAcceleration);
  Serial.begin(115200);
  while (!Serial);
  shutterInit();
}


void closeShutter()
{
  digitalWrite(MotorDisable, LOW);
  delay(20);
  stepper1.moveTo(theMax);
  while (stepper1.distanceToGo() != 0) stepper1.run();
  digitalWrite(MotorDisable, HIGH);
}


void openShutter()
{
  digitalWrite(MotorDisable, LOW);
  delay(20);
  stepper1.moveTo(0);
  while (stepper1.distanceToGo() != 0) stepper1.run();
  digitalWrite(MotorDisable, HIGH);
}


void shutterInit()
// we have to begin the work with the device
// from the carriage positioning
{
  digitalWrite(MotorDisable, LOW);
  
  if (hitEndStop()) {  
    stepper1.moveTo(stepper1.currentPosition() + 130);
    while (stepper1.distanceToGo() != 0) stepper1.run();  
  }

  count=0;
  do {
    stepper1.moveTo(stepper1.currentPosition() - 1);
    while (stepper1.distanceToGo() != 0) stepper1.run();
    count++;
  } while ( not hitEndStop());
  
  delay(100);
  stepper1.moveTo(stepper1.currentPosition() + 60);
  while (stepper1.distanceToGo() != 0) stepper1.run();
  stepper1.setCurrentPosition(0);
  digitalWrite(MotorDisable, HIGH);
}


boolean hitEndStop()
// check if the carriage hit the endstop
{
  delay(8);
  if (analogRead(theEndStop) < 100) {
    return false;
  }
  else {
    return true;
  }
}


void loop()
{
  if (Serial.available() > 0 ) {

    char data_in = (char) Serial.read();

    switch (data_in) {
    case '?':  // print identification string
      delay(4);
      Serial.println("Shutter CD");
      break;
    case 'o':  // open shutter
      openShutter();
      Serial.println("0");
      break;
    case 'c':  // close shutter
      closeShutter();
      Serial.println("0");
      break;
    default:  // do nothing if other input happens
        break;

    }// end of switch    

  }// end of Serial.available
}
