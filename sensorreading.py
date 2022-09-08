#!/usr/bin/python3

from time import sleep

delay = 1

import serial

if name == 'main':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
        with open('temperatureData') as f:
         contents = f.read()
         print(f'temperatur: {contents}')
        # sleep(delay)
