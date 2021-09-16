import time
from pymongo import MongoClient
from elasticsearch import Elasticsearch

mongodb_client = MongoClient('mongodb://localhost:27017')
es_client = Elasticsearch(['https://analisisdedatosproject.es.us-central1.gcp.cloud.es.io:9243'], http_auth=("elastic", "F5ktpvBwxH4jbUqkdTbWw0bU"))

mdb = mongodb_client['elastic']
data = mdb.elastic.find()

# Run a search for all existing words
res = es.search(index="mongo_log_data", doc_type="docs", body={})

# Pull the word object from each hit in the search results
hit_list = (res['hits']['hits'])

# List word objects, appending the contents from the search hit's _source field.
logs_list = []
for hit in hit_list:
    logs_list.append(hit['_source'])
    
doc_id = data.insert_one(json.dumps(logs_list)).inserted_id