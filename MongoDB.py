from pymongo import MongoClient
from datetime import datetime
class Mongo:
    
    def __init__(self):
        self.client = MongoClient('mongodb://localhost')
    
    def insertar(self, distancia, temperatura, humedad):
        self.db = self.client.datos
        self.collection = self.db.registros
        self.collection.insert_one({"sensor":1,"dato": str(distancia)+"cm", "fecha": str(datetime.now())})
        self.collection.insert_one({"sensor":2,"dato": str(temperatura)+"°C"+"//"+str(humedad)+"%", "fecha": str(datetime.now())})
        
#client = MongoClient('hostname', 27017)
'''mydict = { "nombre": "Juan", "direccion": "C/ Mayor 1" }
db = client.datos
collection = db.sensor
collection.insert_one(mydict)'''
m = Mongo()
m.insertar(100, 20, 19)



