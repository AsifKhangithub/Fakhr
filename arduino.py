
import serial # importerar serial library där vi kan arbeta med  seriell kommunikation

# variabel ser skaffas för den seriella anslutningen för att lättare att referas till den
# Den första är ansltningen via USB, data från arduino hamnar, bit hastighet sätts till 9600 sist en timeout en sekund

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
# Spola bufferten, rensar platsen där allt info kommer in innan det sätts igång 
ser.reset_input_buffer()


while True: # En kontitinerlig loop
# Readline läser in det som kommer från serilaanslutningen. UTF8 Decoder är en teckenavkodning som kan göra alla Unicode-tecken läsbara.
#Slutligen avslutas med rstrip() tar bort alla efterföjare slutet av strängen mellansalg som standard. 

 line = ser.readline().decode('utf-8').rstrip()
     # När vi läser data från arduino och vind sensor står stilla
     # Då får vi - värden och för att få bort det använde vi replace
 tabort_minus = line.replace('-', '0.00')
    # Och här läser vi första 4 värden som kommer från sensorn.
 siffror = tabort_minus[0:4]

    #Skickar datan till arduino.csv som läses senare av webbsidan
    #Efter det lägger vi till ny rads tecken för att skriva det nya data i en ny rad.
 with open ('/var/www/html/arduino.csv','a') as datafile:
  datafile.write(str(line) + ("\n"))
