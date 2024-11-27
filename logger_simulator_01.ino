long randNumber;

void setup() {
// initialize serial comms
  Serial.begin(19200);
  pinMode(13, OUTPUT);
}

long i=0,k1=0,k2=0;
float pi=3.14159,s1,s2;
void loop() {
  long j1=0,j2=0;
  unsigned long mtime;
  i=i+1;
  i=i%100;
  if(i==0){k1=random(-2,2);j1=i+k1;}
  else{j1=i+k1;}
  if(i==0){k2=random(-2,2);j2=i+k2;}
  else{j2=i+k2;}
  mtime=millis();
  Serial.print(mtime);
  Serial.print(",");
  s1=sin(2.0*pi*float(j1)/100.);
  if (s1<0.0){s1=0.0;}
  Serial.print(String(s1));
  Serial.print(",");
  s2=cos(2.0*pi*float(j2)/100.);
  if (s2<0.0){s2=0.0;}
  Serial.print(String(s2));
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.print(",");
  Serial.print("0.0");
  Serial.println();
  digitalWrite(13,1);
  delay(25);
  digitalWrite(13,0);
  delay(25);
}
