import serial # importerar serial library där vi kan arbeta med  seriell kommunikation

# variabel ser skaffas för den seriella anslutningen för att lättare att referas till den
# Den första är ansltningen via USB bit hastighet sätts till 9600 sist en timeout för kommunukation  en sekund
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
# Spola bufferten 
ser.reset_input_buffer()

while True: # En kontitinerlig loop
# Readline läser in det som kommer från serilaanslutningen. UTF8 Decoder är en teckenavkodning som kan göra alla Unicode-tecken läsbara.
#Slutligen avslutas med rstrip() tar bort alla efterföjare slutet av strängen mellansalg som standard. 
 line = ser.readline().decode('utf-8').rstrip()

    #Write data to file in CSV format

 with open ('/var/www/html/arduino.csv','a') as datafile:
  datafile.write(str(line) + ("\n"))


