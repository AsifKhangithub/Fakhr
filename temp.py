import time
import serial
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
ser.reset_input_buffer()

while True:
 temperature = str(sensor.get_temperature())
 siffror = temperature[0:3]

    #Write data to file in CSV format
 with open ('/var/www/html/temp.csv','a') as datafile:
  datafile.write(str(siffror) + ("\n"))
 time.sleep(1)

