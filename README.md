## Automation of a CDROM linear actuator using Arduino

![Alt Text](https://github.com/serhiykobyakov/CDROM_linear_actuator_automatization/blob/main/howitworks.webp)

### What is it

I needed some mecnanical laser beam interrupter (optical shutter) and decided to make it myself using garbage. Yes, I like the idea of zero waste way of doing business. Yes, it's damn time consuming way of doing things but let's put all the discussion aside and let me just show you the coding part of the project here.

Here I have only the Arduino sketch without all the other stuff - the circuitry and the case.

The software has been tested for errors, stability and speed (bugs free is not guaranteed, see the licence).

### How It Works

I have an old CDROM which has working linear actuator. It's not very fast for optical shutter but it's cheap. So I need some low power stepper motor driver, an Arduino board to control it and a case to hold it all together. The stepper motor is the [Easy Driver](https://learn.sparkfun.com/tutorials/easy-driver-hook-up-guide/all) - you can see the red board in the bottom left corner of the image. Any Arduino board is siutable for this task (not shown in the image).

In this particular case I needed just two extreme positions of the linear actuator corresponding to the optical shutter states "open" and "close".

The device finds the start position using endstop at the initialization. To open the optical shutter one have to send "o" to serial port, to close it - send "c". Arduino sends back zero ("0") to PC when the process is finished (it si useful to know when the shutter is fully closed or open).


### Install

1. Make directory "ShutterCD" in the sketchbook directory on your PC (it is "Arduino" by default, check the preferences in Arduino IDE).
2. Put the ShutterCD.ino into "ShutterCD" directory.
3. Open Arduino IDE and set your Arduino board
4. Check the sketch for errors and upload the sketch to the board.


### How To Setup The Device
When you have the device assembled - you need to check for two things:
1. What is the positive direction of motion - it must be the one when the carriage moves away from the endstop.
2. How many steps is the travel range of your linear actuator - at the maximum it must stop at the end of the range in order to not hit the wall (maybe the good idea is to put another endstop there). Check for the number and then correct the sketch accordingly.


### Contact
For reporting [bugs, suggestions, patches](https://github.com/serhiykobyakov/CDROM_linear_actuator_automatization/issues)


### License
The project is licensed under the [MIT license](https://github.com/serhiykobyakov/CDROM_linear_actuator_automatization/blob/main/LICENSE)
