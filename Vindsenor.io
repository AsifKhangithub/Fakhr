void setup()
{
  Serial.begin(9600);
}
void loop()
{
  # Vi läser data från A0
  float sensorValue = analogRead(A0);
  # Vi gör om datan som kommer i value som är ej relevnta till relevnta data.
  float voltage = (sensorValue / 1023) * 5;
  float wind_speed = mapfloat(voltage, 0.4, 2, 0, 32.4);
  # Skriver serielt datan som kommer från sensor till serialmoniter som i sin del kommer läsas av pi.
  Serial.print(wind_speed);
  Serial.println("");
  # en liten delay.
  delay(100);
}
 float mapfloat(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
