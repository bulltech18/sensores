import time
from Sensores import *

TEMPO = input("Ingrese cada cuantos segundos desea guardar los detos de los sensores: "); print()

while TEMPO != 0:
    time.sleep(int(TEMPO))
    Proceso()
    
