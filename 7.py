from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import dns
import json

client = couchdb.Server('http://Jonathan14:Familia141999@localhost:5984/')

try:
    print('Couch connection: Success')
except ConnectionFailure as e:
    print('Couch connection: Failed', e)
    
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

clientatlas = pymongo.MongoClient("mongodb+srv://esfot1:esfot1@cluster0.3rdjg.mongodb.net/prueba7?retryWrites=true&w=majority")
Database_m = clientatlas.get_database('prueba7')
Database_ma =Database_m.couchmongo

try:
    clientatlas.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as e:
    print('MongoDB Atlas connection: failed', e)
    
DBc=client['prueba0']

for db in DBc:
    try:
        Database_ma.insert_one(DBc[db])
        print('Data saved mongoDB Atlas')
    except TypeError as et:
        print('current document raised error: {}'.format(et))
        SKIPPED.append(db)  # creating list of skipped documents for later analysis
        continue    # continue to next document
    except Exception as e:
        raise e