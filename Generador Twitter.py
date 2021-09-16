#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install TextBlob


# In[6]:


import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch



###API ########################
ckey = "yn81IefREmbw9sKzeGGVzmMi1"
csecret = "ymyiZ4eAE86ynb2WolymoXHrB6RwrRLycn5or6twTp6k5u9ktJ"
atoken = "1415799839380676620-JFDtk7RewMt8xzBWlenAeA2ezkwfkZ"
asecret = "G3kJUNMPdyhjNxb2mz3pUbh2k1TePLYXgO0TAvgXYmpKM"
#####################################

# create instance of elasticsearch
#host = 'localhost:9200'
#es = Elasticsearch([host])

es = Elasticsearch(
   cloud_id="DataLake:ZWFzdHVzMi5henVyZS5lbGFzdGljLWNsb3VkLmNvbTo5MjQzJDRkZDUyZWQxYjkyMjQyOTNiYzcwMzBmNDNhMWRmMTdjJDdjNDhiOTc2M2U2ZTRlNmY5YmU0NDc2NjFkZWYzODVl",
    http_auth=("elastic", "HII3x5U0SfalSInLz0lBFOMP"),
)


class TweetStreamListener(StreamListener):

    # on success
    def on_data(self, data):

        # decode json
        dict_data = json.loads(data)

        # pass tweet into TextBlob
        tweet = TextBlob(dict_data["text"])

        # output sentiment polarity
        print (tweet.sentiment.polarity)

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # output sentiment
        print (sentiment)

        # add text and sentiment info to elasticsearch
        es.index(index="index3",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"],
                       "geo":dict_data["user"]["location"],
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "sentiment": sentiment})
        return True

    # on failure
    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    # create instance of the tweepy stream
    stream = Stream(auth, listener)

    # search twitter for "Ecuador" keyword
    stream.filter(track=['Ecuador', 'Presidentes'])
    #stream.filter(locations=[-74.25909,40.477399,-73.700181,40.916178])


    


# In[ ]:




