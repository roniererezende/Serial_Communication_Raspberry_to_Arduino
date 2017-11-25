# Program : Communicating Raspberry with Arduino
# Author  : Roniere Rezende
# Date    : 15/11/2017
# Version : 1.0
# Update  : This is the  first version, there isn't atualization  
 
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
    
    if umid is not None and temp is not None:
        print(temp_st)
        ser.write(temp_st)
        time.sleep(0.5)
    else:
        print("Error")
        ser.write("Error")
        time.sleep(0.5)