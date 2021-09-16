#!/usr/bin/env python
# coding: utf-8

# In[26]:


import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId


# In[47]:


#conexion con mongodb
client = MongoClient('mongodb://localhost:27017')
try:
    client.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

DBS = client['Canciones']

client2 = MongoClient('mongodb+srv://esfot:esfot@cluster0.xf99e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
try:
    client2.admin.command('ismaster')
    print('MongoDB connection atlas: Success')
except ConnectionFailure as cf:
    print('MongoDB connection atlas: failed', cf)

mongoDB = client2.get_database('Canciones')
db2 = mongoDB.Pop

for db in DBS:
    if db in ('Canciones'):
        cols = client[db].list_collection_names()
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for datos in client[db][col].find():
                try:
                    documents = json.loads(json_util.dumps(datos))
                    db2.insert_many(documents)
                    print("SAVE")
                    print(documents)
                except Exception as error:
                    print ("Error saving data: %s" % str(error))


# In[ ]:




