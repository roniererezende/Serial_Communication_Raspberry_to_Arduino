// Program: Communicating Arduino With Raspberry Pi 
//          Using Sensor Module AM2302
// Author: Roniere Rezende
// Date: 15/11/2017
// Version: 2.1
// Upgrade: - Include a communication protocol to transmit the temperature and humid data
//          - Create a protocol which join the kind of data and the information
#include <LiquidCrystal.h>

char temp          = '0';
char humid         = '0';
char buff[8]       = {};

LiquidCrystal lcd(8,9,4,5,6,7);

byte degree[8] = {
B00000,
B01110,
B01010,
B01110,
B00000,
B00000,
B00000,
B00000
};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  lcd.begin(16,2);

  lcd.setCursor(0,0);
  lcd.print("Temp:");
  lcd.setCursor(11,0);
  lcd.print("C");
  lcd.setCursor(0,1);
  lcd.print("Humid:");
  lcd.setCursor(11,1);
  lcd.print("%");
  
  lcd.createChar(0, degree);
  lcd.setCursor(10,0);
  lcd.write((byte)0);  
}

void loop() {
  // put your main code here, to run repeatedly:
  int i              = 0;
  int column_T       = 6;
  int column_H       = 6;
  
  if (Serial.available()){
    for(i = 0; i < 8; i++ ){
      buff[i] = Serial.read();
    }

    for(i = 0; i < 8; i++ ){
      if(i < 4){
        lcd.setCursor(column_T,0);
        lcd.print(buff[i]);
        column_T++;
      }

      if(i>=4 && i<8){
        lcd.setCursor(column_H,1);
        lcd.print(buff[i]);
        column_H++; 
      }
    }
  }
  delay(100);
}
