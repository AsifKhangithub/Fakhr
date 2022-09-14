import serial
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

while True:
 line = ser.readline().decode('utf-8').rstrip()

    #Write data to file in CSV format

 with open ('/var/www/html/arduino.csv','a') as datafile:
  datafile.write(str(line) + ("\n"))


