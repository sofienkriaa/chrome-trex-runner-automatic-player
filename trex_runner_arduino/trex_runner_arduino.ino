void setup() {
  Serial.begin(9600);
}

void loop() {
  int analog = analogRead(A0);
  //Serial.println(analog);
  if (analog < 700) {  
    Serial.write("c");    
  }
}
