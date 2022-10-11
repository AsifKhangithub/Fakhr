    #Det importerar bibloteket för tid och tempsensor data från sensor Biblotek för temp sensor behvöer installeras med <sudo apt-get install python3-w1thermsensor>
     # Eller installera via < sudo pip3 install w1thermsensor > innan installering måste man aktivera 1-wire Interface genom att skriva i kommando raden <sudo raspi-config>
import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()


while True:
 #Här läses data när koden körs från sensorn.
 temperature = str(sensor.get_temperature())
 # Här kontrollerar vi att vi får in data men inte alla siffror som kommer in eftersom vi får många decimaler
 # Då gör vi index 0 till 4 för att läsa första 5 siffror inklusive '.' så det blir ex "23.00" .
 siffror = temperature[0:4]

    #Skickar datan till temp.csv som läses senare av webbsidan
    #Efter det lägger vi till ny rads tecken för att skriva det nya data i en ny rad.
 with open ('/var/www/html/temp.csv','a') as datafile:
  datafile.write(str(siffror) + ("\n"))


