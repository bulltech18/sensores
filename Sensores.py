#from SQL import *
from Archivos import *
import RPi.GPIO as GPIO
import Adafruit_DHT
import adafruit_dht
import time
import board
class Sensores:
    def __init__(self):
        self.distancia = 0
        self.temperature_c = 0
        self.humidity = 0
        #self.presencia
    def Proceso(self):
        TRIG = 17 #Triger
        ECHO = 27 #Eco
        TEMPO = 0 #Timer
        SENSO = 16 #Presencia

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT) 
        GPIO.setup(ECHO, GPIO.IN)  
        #GPIO.setup(SENSO, GPIO.IN)

        try:

            while TEMPO < 1:
          

                GPIO.output(TRIG, GPIO.LOW)
                time.sleep(0.5)


                GPIO.output(TRIG, GPIO.HIGH)
                time.sleep(0.00001)
                GPIO.output(TRIG, GPIO.LOW)

            
                while True:
                    pulso_inicio = time.time()
                    if GPIO.input(ECHO) == GPIO.HIGH:
                        break
            
                while True:
                    pulso_fin = time.time()
                    if GPIO.input(ECHO) == GPIO.LOW:
                        break


                duracion = pulso_fin - pulso_inicio

                self.distancia = (34300 * duracion) / 2
                dito = round(self.distancia,2)

                TEMPO += 1
        #==================================================================================================
                
                dhtDevice = adafruit_dht.DHT11(board.D5)
                self.temperature_c = dhtDevice.temperature
            
                self.humidity = dhtDevice.humidity
                
             
            
                
        #==================================================================================================
            #i=GPIO.input(SENSO)
        
        
            #Registro(distancia, humedad, temperatura, i)
            #Exportar(distancia, humedad, temperatura, i)
            #print (str(humedad))
            dhtDevice.exit()
        except:
        
            dhtDevice.exit()
        finally:
            
            GPIO.cleanup()
        
   
        
        

