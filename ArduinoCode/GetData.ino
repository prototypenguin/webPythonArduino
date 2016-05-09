int incByte;
int val;

void setup() {
  Serial.begin(9600); 
}

void loop() {
if (Serial.available() > 0){ 
  incByte = Serial.read(); 
  
  if (incByte == 'A'){ 
    Serial.flush(); 
    Serial.println("Connected");
    Serial.flush();
    }
  if (incByte == 'B'){
    Serial.flush();
    val = 1;
    Serial.println(val);
    Serial.flush();
    }


}
}
