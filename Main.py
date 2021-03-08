import time
import os
from Sensores import *
from MongoDB import *
from SQL import *
from Archivos import *


class Main:
    def main():
        sens = Sensores()
        mngo = Mongo()
        sdb = sqldb()
        TEMPO = input("Ingrese cada cuantos segundos desea guardar los datos: ")
        while True:
            time.sleep(int(TEMPO))
            print("guardando datos..")
            sens.Proceso()
            mngo.insertar(sens.distancia,sens.temperature_c, sens.humidity)
            sdb.Registro(sens.distancia, sens.temperature_c, sens.humidity)
            Exportar()
            
            
        
    def clear():
       os.system("cls" if os.name == "nt" else "clear")
    if __name__ == "__main__":
        main()