import pandas as pd
from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import dns
import json

clientatlas = pymongo.MongoClient("mongodb+srv://esfot1:esfot1@cluster0.3rdjg.mongodb.net/prueba7?retryWrites=true&w=majority")
Database_m = clientatlas.get_database('prueba7')
Database_ma =Database_m.couchmongo

try:
    clientatlas.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as e:
    print('MongoDB Atlas connection: failed', e)

df=pd.read_csv("Database_ma")
ruta="/Users/user/prueba"
df.to_csv(ruta)