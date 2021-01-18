from facebook_scraper import get_posts
import couchdb
import json
import time
import pymongo
import pprint
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

db_client = pymongo.MongoClient("mongodb://localhost:27017")    #('http://115.146.93.184:5984/')
prueba = db_client.prueba
my_posts = prueba.posts
    
i=1
for post in get_posts('Fifa',pages=1000,extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
    
    doc['id']=id
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}
        
        doc['post_url']=post['post_url']
        my_posts.save(doc)
        
        print('guardado con exito')
    except Exception as e:
        print('no se pudo guardar:'+str(e))