## Automation of a CDROM linear actuator using Arduino

### What it does

The software has been tested for errors, stability and speed (bugs free is not guaranteed, see the licence).

### Install

1. Make directory "ShutterCD" in the sketchbook directory on your PC (it is "Arduino" by default, check the preferences in Arduino IDE).
2. Put the ShutterCD.ino into "ShutterCD" directory.
3. Open Arduino IDE and set your Arduino board
4. Check the sketch for errors and upload the sketch to the board.


### How It Works
The stepper motor in CDROM actuator can be driven by some low power driver, for example [this one](https://learn.sparkfun.com/tutorials/easy-driver-hook-up-guide/all).
 Arduino board can drive the stepper driver.

In this particular case I needed just two extreme positions of the linear actuator corresponding to the stated of the optical shutter: "open" and "close".

Here I have only the Arduino sketch without all the other stuff - the circuitry and the case.

The device starts from finding the initial position using endstop.

### How To Setup The Device
When you have the device assembled - you need to check for two things:
1. What is the positive direction of motion - it must be the one when the carriage moves away from the endstop.
2. How many steps is the travel range of your linear actuator - at the maximum it must stop at the end of the range in order to not hit the wall (maybe the good idea is to put another endstop there). Check for the number and then correct the sketch accordingly.


### How To Use
To open the optical shutter one have to send "o" to serial port, to close it - send "c".
Arduino sends back zero when the process is finished.


### Contact
For reporting [bugs, suggestions, patches](https://github.com/serhiykobyakov/CDROM_linear_actuator_automatization/issues)


### License
The project is licensed under the [MIT license](https://github.com/serhiykobyakov/CDROM_linear_actuator_automatization/blob/main/LICENSE)
