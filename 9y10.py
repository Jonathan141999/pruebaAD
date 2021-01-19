import json
import pymongo
import pandas as pd



DBS = 'prueba7'

try:
    client = pymongo.MongoClient('mongodb+srv://esfot1:esfot1@cluster0.3rdjg.mongodb.net/prueba7?retryWrites=true&w=majority')
    client.server_info()
    print ('MongoDB Atlas connection: Success')
except pymongo.errors.ServerSelectionTimeoutError as e:
    print ('MongoDB Atlas connection: failed: %s' % e)

db = client.prueba7
col = db.couchmongo
    
myprueba = col.find()

data=[]
for item in myprueba:
    data.append(item)
    
pd.DataFrame([data]).to_csv('prueba7.csv', index=False)

