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
    titlesp = "Sensor, dato_string, dato_decimal, dato_bool fecha, dato_int\n"
    csvp.write(titlesp)
    sql.getRegistros()
    for (id, sensorID, dato_str, dato_decimal, dato_bool, fecha, dato_int) in sql.MYCURSOR:
        rowsp = "{},{},{},{},{},{},{}\n".format(id, sensorID, dato_str, dato_decimal, dato_bool, fecha, dato_int)
        csvp.write(rowsp)
    csvp.close()
    
Exportar()
