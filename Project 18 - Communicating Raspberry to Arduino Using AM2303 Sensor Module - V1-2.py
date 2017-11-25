# Program : Communicating Raspberry with Arduino
# Author  : Roniere Rezende
# Date    : 15/11/2017
# Version :
2.0
# Update  : Include a communication protocol to transmit the temperature and humid data
 
import RPi.GPIO as GPIO
import time
import serial
import Adafruit_DHT
 
DHT_IN = 15

#Configure the serial and the throughput
ser = serial.Serial("/dev/ttyS0", 9600)

sensor = Adafruit_DHT.DHT22

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT_IN, GPIO.IN)

while True:

    umid, temp = Adafruit_DHT.read_retry(sensor, DHT_IN)
    temp_st = str("%.1f" % temp)    
    umid_st = str("%.1f" % umid)
    
    if umid is not None and temp is not None:

        ser.write('T')
        print('T')
        ser.write(temp_st)
        print(temp_st)
        time.sleep(1)
        
        ser.write('H')
        print('H')
        ser.write(umid_st)
        print(umid_st)
        time.sleep(1)
         
    else:
        print("Error")
        ser.write("Error")
        time.sleep(0.5)
