void setup()
{
  Serial.begin(9600);
}
void loop()
{
  float sensorValue = analogRead(A0);
  float voltage = (sensorValue / 1023) * 5;
  float wind_speed = mapfloat(voltage, 0.4, 2, 0, 32.4);
  Serial.print("Vind Hastighet =");
 // Serial.print(wind_speed);
 // Serial.println("m/s");
 // Serial.print("Vind Hastighet =");
  Serial.print(wind_speed * 3.6);
  Serial.println("Km/h");
  delay(100);
}
 float mapfloat(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
