import os
from SQL import *

def Exportar():
    '''file = open("/home/pi/Desktop/Datos.txt", "w")
    file.write("Distancia: "+str(round(distancia,2))+" cm."  + os.linesep)
    file.write("Humedad: "+str(humedad) + os.linesep)
    file.write("Temperatura: "+str(temperatura)+" ºC" + os.linesep)
    #file.write("Presencia: "+str(presencia))
    file.close()'''
    sql = sqldb()
    filePres = "datos.csv"
    csvp = open(filePres,"w")
    titlesp = "Sensor, Dato, fecha\n"
    csvp.write(titlesp)
    sql.getRegistros()
    for (id, sensor, dato, fecha) in sql.MYCURSOR:
        rowsp = "{},{},{},{}\n".format(id, sensor, dato, fecha)
        csvp.write(rowsp)
    csvp.close()
