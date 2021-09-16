#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd
import numpy as np


# In[2]:


con = sqlite3.connect('CovidBD.db')


def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM covid_variantsNuevo')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(con)


# In[4]:


df = pd.read_sql_query("SELECT location FROM covid_variantsNuevo", con)
df2 = pd.read_sql_query("SELECT date FROM covid_variantsNuevo", con)
df3 = pd.read_sql_query("SELECT variant FROM covid_variantsNuevo", con)
df4 = pd.read_sql_query("SELECT num_sequences FROM covid_variantsNuevo", con)
df5 = pd.read_sql_query("SELECT perc_sequences FROM covid_variantsNuevo", con)
df6 = pd.read_sql_query("SELECT num_sequences_total FROM covid_variantsNuevo", con)


# In[6]:


df3


# In[7]:


arr = np.array(df)
arr2 = np.array(df2)
arr3 = np.array(df3)
arr4 = np.array(df4)
arr5 = np.array(df5)
arr6 = np.array(df6)


# In[8]:


arr3


# In[9]:


import json

from elasticsearch import Elasticsearch


# In[10]:


# create instance of elasticsearch
#host = 'localhost:9200'
#es = Elasticsearch([host])
id = 0

es = Elasticsearch(
   cloud_id="DataLake:ZWFzdHVzMi5henVyZS5lbGFzdGljLWNsb3VkLmNvbTo5MjQzJDRkZDUyZWQxYjkyMjQyOTNiYzcwMzBmNDNhMWRmMTdjJDdjNDhiOTc2M2U2ZTRlNmY5YmU0NDc2NjFkZWYzODVl",
    http_auth=("elastic", "HII3x5U0SfalSInLz0lBFOMP"),
)

for indexBD in range(len(arr)):
    id = id + 1
    es.index(index="sql", 
        body = {
        "Ubicacion": arr[indexBD],
        "Fecha": arr2[indexBD],
        "Variante": arr3[indexBD],
        "Numero de muestras": arr4[indexBD],
        "Porcentaje de las muestras": arr5[indexBD],
        "Numero total de muestras secuenciadas": arr6[indexBD]})
    
    print("Dato:" + str(id) + " Subido a elasticsearch")


# In[ ]:




