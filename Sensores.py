from SQL import *
from Archivos import *
import RPi.GPIO as GPIO
import Adafruit_DHT
import adafruit_dht
import time
import board
from MongoDB import *
class Sensor:
    
    
    def __init__(self,_id):
        self.id = _id
        self.mongo = Mongo()
    
    def ReadUlt(self):
        x = self.mongo.getPines(self.id) #Trae los pines del sensor
        self.TRIG = int(x[0]) #Triger - 17 para pruebas
        self.ECHO = int(x[1]) #Eco - 27 para pruebas
        self.TEMPO = 0 #Timer
        #SENSO = 16 #Presencia

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TRIG, GPIO.OUT) 
        GPIO.setup(self.ECHO, GPIO.IN)  
        #GPIO.setup(SENSO, GPIO.IN)

        try:

            while self.TEMPO < 1:
          

                GPIO.output(self.TRIG, GPIO.LOW)
                time.sleep(0.5)


                GPIO.output(self.TRIG, GPIO.HIGH)
                time.sleep(0.00001)
                GPIO.output(self.TRIG, GPIO.LOW)

            
                while True:
                    pulso_inicio = time.time()
                    if GPIO.input(self.ECHO) == GPIO.HIGH:
                        break
            
                while True:
                    pulso_fin = time.time()
                    if GPIO.input(self.ECHO) == GPIO.LOW:
                        break


                duracion = pulso_fin - pulso_inicio

                self.distancia = (34300 * duracion) / 2
                dito = round(self.distancia,2)

                self.TEMPO += 1
                print(self.distancia)
                #i=GPIO.input(SENSO)
        
        
            #Registro(distancia, humedad, temperatura, i)
            #Exportar(distancia, humedad, temperatura, i)
            #print (str(humedad))
        except:
            GPIO.cleanup()
        finally:
            
            GPIO.cleanup()
    
    def ReadTemp(self):
        x = self.mongo.getPines(self.id) #Trae el pin del sensor
        x = int(x[0])
        y = "D"+ str(x)
        z = "board."+y
        try:
            dhtDevice = adafruit_dht.DHT11(z)    
            self.temperature_c = dhtDevice.temperature
            self.humidity = dhtDevice.humidity
            dhtDevice.exit()
        except:
            dhtDevice.exit()
        
            
        
            
        
    
    def ReadPIR(self):
        x = self.mongo.getPines(self.id)
        pin = int(x[0])
        GPIO.setup(pin, GPIO.IN)
        try:
            dato = GPIO.input(pin)
        except:
            GPIO.cleanup()
        finally:
            GPIO.cleanup()
        

        
        

