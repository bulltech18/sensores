import mysql.connector
from datetime import datetime
class sqldb:
    def __init__(self):
        self.MYDB = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="",
                                       database="datos")
        self.MYCURSOR = self.MYDB.cursor()

    def Registro(self, sensor, dato, dato2 = 0):
        dis = 1
        sql = "SELECT nombre FROM sensores, sensores_reg WHERE sensores.id = sensores_reg.sensor_id and sensores_reg.id = %s"
        sqldata = (sensor,)
        self.MYCURSOR.execute(sql, sqldata)
        myresult = self.MYCURSOR.fetchone()
        
        if myresult[0] == "Ultrasonico":
            ult = "INSERT INTO registros(sensorID, dato_decimal, fecha) VALUES (%s, %s, %s)" #ULTRASONICO
            ult_data = (sensor, dato, datetime.now())
            self.MYCURSOR.execute(ult, ult_data)
            self.MYDB.commit()
        elif myresult[0] == "Temp y Humedad":
            temp = "INSERT INTO registros(sensorID, dato_decimal,dato_int, fecha) VALUES (%s, %s, %s, %s)"#TEMPERATURA
            temp_data = (sensor, dato, dato2,  datetime.now())
            self.MYCURSOR.execute(temp, temp_data)
            self.MYDB.commit()
        elif myresult[0] == "Presencia":
            pre = "INSERT INTO registros(sensor, dato, fecha) VALUES (%s, %s, %s)"
            pre_data = (1, str(temperatura)+"°C"+"//"+str(humedad)+"%", datetime.now()) #PRESENCIA
        else:
            print("sensor no valido")
        
    
    def getRegistros(self):
        sql = "SELECT * FROM registros"
        self.MYCURSOR.execute(sql)
    
    
        

        
    
