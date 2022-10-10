#!/usr/bin/python3

__version__ = '10.10.2022'
__author__ = 'Serhiy Kobyakov'

import sys
import time
import serial.tools.list_ports
from arduino_device import ArduinoDevice as ad
from shuttercd import ShutterCD


def do_open(the_shutter):
    tstmp1 = time.time()
    the_shutter.open()
    tstmp2 = time.time()
    print(f"Open time: {(tstmp2 - tstmp1):.3f} s")
    time.sleep(0.9)


def do_close(the_shutter):
    tstmp1 = time.time()
    the_shutter.close()
    tstmp2 = time.time()
    print(f"Close time: {(tstmp2 - tstmp1):.3f} s")
    time.sleep(0.9)

def show_info(the_shutter):
    tstmp1 = time.time()
    print(the_shutter.serial_info)
    tstmp2 = time.time()
    print(f"Print time: {(tstmp2 - tstmp1):.3f} s")


if __name__ == "__main__":
    # Let's check the active serial devices and list them all:
    # print("\nLooking for serial devices...", end="\r")
    # ports = serial.tools.list_ports.comports()
    # if len(ports) == 0:
    #     print("No serial devices found!", " "*50, "\n")
    # else:
    #     for port in ports:
    #         print(f"{port.device}:", ad.get_device_id_str(port.device), " "*50, "\n")

    theport = ''
    shutter = None
    old_id = id(shutter)

    # get the serial port address to which the device is connected:
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if ad.get_device_id_str(port.device) == 'ShutterCD':
            theport = port.device
            print(f"Found {'ShutterCD'} at {theport}")

    # initialize the device:
    if len(theport) > 0:
        shutter = ShutterCD(theport)

    # check if the device has been initialized:
    if id(shutter) == old_id:
        print("\ntest_shutter.py: Error initializing the device!\n")
        sys.exit(1)

    print()
    # ask the device to do something:

    # do_close(shutter)
    # do_open(shutter)
    # do_close(shutter)
    do_open(shutter)
    do_close(shutter)

    show_info(shutter)

