import time
import serial
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

while True:
 line = ser.readline().decode('utf-8').rstrip()

 temperature = sensor.get_temperature()

    #Write data to file in CSV format
 with open ('/var/www/html/temp.csv','a') as datafile:
  datafile.write(str(sensor.get_temperature()) + ("\n"))
 time.sleep(1)

 with open ('/var/www/html/arduino.csv','a') as datafile:
  datafile.write(str(line) + ("\n"))
 time.sleep(1)
 


