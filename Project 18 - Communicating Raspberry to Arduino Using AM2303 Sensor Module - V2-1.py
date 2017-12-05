# Declara-se as bibliotecas que serão utilizadas no código
import RPi.GPIO as GPIO
import time
import serial
import Adafruit_DHT
 
#Define a GPIO que irá receber os dados do módulo sensor
DHT_IN = 15


#Configura o uso do terminal serial e da taxa de transmissão de dados
ser = serial.Serial("/dev/ttyS0", 9600)


#Define um objeto para a classe Adafruit_DHT, que habilita o módulo sensor
sensor = Adafruit_DHT.DHT22


#Configuração inicial dos terminais GPIO
GPIO.setwarnings(False)


GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT_IN, GPIO.IN)


while True:
    
    # Armazena e converte os dados do tipo “int” em tipo “string” 
    umid, temp = Adafruit_DHT.read_retry(sensor, DHT_IN)
    temp_st = str("%.1f" % temp)    
    umid_st = str("%.1f" % umid)
    #  Avalia se os dados enviado pelo módulo sensor são válidos
    if umid is not None and temp is not None:
        
        #Define um protocolo e transmite os dados via terminal serial
        ser.write(temp_st+umid_st)     
         
    else:
        #Informa que os dados gerados não serão válidos
        ser.write("Error")
        time.sleep(0.5)
        
    time.sleep(1)
