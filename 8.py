import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId

client = MongoClient('mongodb://localhost:27017')
try:
    client.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)
DBS = ['prueba']

client2 = MongoClient('mongodb+srv://esfot1:esfot1@cluster0.3rdjg.mongodb.net/prueba7?retryWrites=true&w=majority')
try:
    client2.admin.command('ismaster')
    print('MongoDB connection atlas: Success')
except ConnectionFailure as cf:
    print('MongoDB connection atlas: failed', cf)

DBc = client2.get_database('prueba7')
db2 = DBc.couchmongo

for db in DBS:
    if db in ('prueba7'):  
        cols = client[db].list_collection_names() 
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in client[db][col].find():  
                try:
                    documents = json.loads(json_util.dumps(x))
                    db2.insert_one(documents)
                    print("SAVE")
                    print(documents)
                except Exception as error:
                    print ("Error saving data: %s" % str(error))
