import time
import os
from Sensores import *
from MongoDB import *
from SQL import *
from Archivos import *


class Main:
    def main():
        sensorUltrasonico = Sensor(1)
        sensorTemp = Sensor(2)
        mngo = Mongo()
        sdb = sqldb()
        TEMPO = input("Ingrese cada cuantos segundos desea guardar los datos: ")
        while True:
            time.sleep(int(TEMPO))
            print("guardando datos..")
            sensorUltrasonico.ReadUlt()
            sensorTemp.ReadTemp()
            mngo.insertar(sensorUltrasonico.id,sensorUltrasonico.distancia)
            mngo.insertar(sensorTemp.id, sensorTemp.temperature_c, dato2 = sensorTemp.humidity)
            sdb.Registro(sensorUltrasonico.id,sensorUltrasonico.distancia)
            sdb.Registro(sensorTemp.id, sensorTemp.temperature_c, dato2 = sensorTemp.humidity)
            Exportar()
            
            
        
    def clear():
       os.system("cls" if os.name == "nt" else "clear")
    if __name__ == "__main__":
        main()