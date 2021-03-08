import mysql.connector
from datetime import datetime
class sqldb:
    def __init__(self):
        self.MYDB = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="",
                                       database="datos")
        self.MYCURSOR = self.MYDB.cursor()

    def Registro(self,distancia, temperatura, humedad):
        dis = 1
        ult = "INSERT INTO registros(sensor, dato, fecha) VALUES (%s, %s, %s)" #ULTRASONICO
        ult_data = (1, str(distancia)+'cm', datetime.now())
        temp = "INSERT INTO registros(sensor, dato, fecha) VALUES (%s, %s, %s)"#TEMPERATURA
        temp_data = (3, str(temperatura)+"°C"+"//"+str(humedad)+"%", datetime.now())
        '''pre = "INSERT INTO registros(sensor, dato, fecha) VALUES (%s, %s, %s)"
        pre_data = (1, str(temperatura)+"°C"+"//"+str(humedad)+"%", datetime.now())''' #PRESENCIA
        self.MYCURSOR.execute(ult, ult_data)
        self.MYDB.commit()
        
        self.MYCURSOR.execute(temp, temp_data)
        self.MYDB.commit()
        print("Registros Completados")
    
    def getRegistros(self):
        sql = "SELECT * FROM registros"
        self.MYCURSOR.execute(sql)
        


        
    
