from pymongo import MongoClient
from datetime import datetime
class Mongo:
    
    def __init__(self):
        self.client = MongoClient('mongodb://localhost')
    
    def insertar(self, sensor, dato1, dato2 = 0):
        
        self.db = self.client.datos
        self.collection2 = self.db.sensores_reg
        x=dict()
        x = self.collection2.find_one({"id": sensor},{"tipo_sensor": 1, "_id":0})
        self.collection3 = self.db.sensor
        y = dict()
        y = self.collection3.find_one({"id":int(x['tipo_sensor'])},{"_id":0, "name":1})
        self.collection = self.db.registros
        if y['name'] == "Ultrasonico":
            self.collection.insert_one({"sensor":sensor,"dato": dato1, "fecha": str(datetime.now())}) 
        elif y['name'] == "Temperatura y Humedad":
            self.collection.insert_one({"sensor":sensor,"dato1":dato1, "dato2": dato2, "fecha": str(datetime.now())})
        
    def getPines(self, sensor):
        self.db = self.client.datos
        self.collection2 = self.db.sensores_reg
        x=dict()
        x = self.collection2.find_one({"id": sensor},{"pines": 1, "_id":0})
        x = list(x['pines'])
        return x
            
        
        
        




