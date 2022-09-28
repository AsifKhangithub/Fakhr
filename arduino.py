    # Vi importerar Seriel bibloteket för läsning av serial data från arduino
import serial
    # Datan från arduino hamna i /dev/ttyACM0 och det kommer med 9600 bithastighet. vi döper den till ser.
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

while True:
     # När vi kör koden då läser vi datan som kommer in.
 line = ser.readline().decode('utf-8').rstrip()
     # När vi läser data från arduino och vind sensor stor stilla
     # Då får vi - värden och för att få bort det använde vi replace
 tabort_minus = line.replace('-', '0.00')
    # Och här läser vi första 5 värden som kommer från sensorn.
 siffror = tabort_minus[0:4]

    #Skickar datan till arduino.csv som läses senare av webbsidan
    #Efter det lägger vi till ny rads tecken för att skriva det nya data i en ny rad.
 with open ('/var/www/html/arduino.csv','a') as datafile:
  datafile.write(str(line) + ("\n"))
