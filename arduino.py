
import serial # Importerar serial library för att kunna arbeta med seriell kommunikation

# Variabeln 'ser' skaffas för den seriella anslutningen. Detta för att lättare att referas till den.
# Den första är ansltningen via USB, data från arduino hamnar, bit hastighet sätts till 9600 sist en timeout en sekund.

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
# Spola bufferten, rensar platsen där all info kommer in innan det sätts igång.
ser.reset_input_buffer()


while True: # En kontinuerlig loop
# Readline läser in det som kommer från serilaanslutningen. UTF8 Decoder är en teckenavkodning som kan göra alla Unicode-tecken läsbara.
#Slutligen avslutas med rstrip() tar bort alla efterföjare slutet av strängen mellanslag som standard.

 line = ser.readline().decode('utf-8').rstrip()
     # När data läses från arduino och vind sensor står stilla
     # Då får man minustecken (-) med i värden. För att få bort det användes replace.
 tabort_minus = line.replace('-', '0.00')
    # Och här läses de första 4 värden som kommer från sensorn.
 siffror = tabort_minus[0:4]

    #Skickar datan till arduino.csv som läses senare av webbsidan
    #Efter det lägges till en ny rads tecken för att skriva det nya data i en ny rad.
 with open ('/var/www/html/arduino.csv','a') as datafile:
  datafile.write(str(line) + ("\n"))
