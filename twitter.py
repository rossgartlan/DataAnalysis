from __future__ import division
from collections import Counter
import math, random, csv, json

from bs4 import BeautifulSoup
import requests
#import tweepy




from twython import Twython
# fill these in if you want to use the code
CONSUMER_KEY = "4mOpad3VZsMkmPnlpdy8snWll"
CONSUMER_SECRET = "JOqOcKM413FyCOOyHhrrFcbjcsCK6uHvZhd6o2m11l4Ux8B03t"
ACCESS_TOKEN = "2278012761-BgVa8ZJpScIKp7zICW2zGud66Q7YvSkWKZ3sWmD"
ACCESS_TOKEN_SECRET = "TCiEuB7PkRQaR0yLbOQAqNYmTqq6cS0ujQPuRMeY68sxS"


 
 
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.secure = True
#auth.set_access_token(access_token, access_secret)
 
#api = tweepy.API(auth)
#places = api.geo_search(query="ireland", granularity="country")
#place_id = places[0].id

def call_twitter_search_api():

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

    # search for tweets containing the phrase "data science"
    for status in twitter.search(q='"ozil"')["statuses"]:
        user = status["user"]["screen_name"].encode('utf-8')
        text = status["text"].encode('utf-8')
        print(user, ":", text)
        print()

from twython import TwythonStreamer

# appending data to a global variable is pretty poor form
# but it makes the example much simpler
tweets = [] 

class MyStreamer(TwythonStreamer):
    """our own subclass of TwythonStreamer that specifies
    how to interact with the stream"""

    def on_success(self, data):
        """what do we do when twitter sends us data?
        here data will be a Python object representing a tweet"""

        # only want to collect English-language tweets
        if data['lang'] == 'en':
            tweets.append(data)
            print("received tweet #", len(tweets))
			
        with open('C:/Users/Rossco/desktop/twitter.txt','a', encoding='utf-8') as saveFile:
            saveFile.write(str(data))
            saveFile.write('\n')
            saveFile.close()
        
		
			
			
        # stop when we've collected enough
        if len(tweets) >= 100:
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

ftweets = []
tweets_file = []
def read_ftweets():
	with open('C:/Users/Rossco/desktop/twitter.txt', 'r' , encoding= 'ISO-8859-1') as f:	
		for line in f:
			ftweets.append((line))	


count=len(tweets)
print(count)


def convert_ftweets_to_dict(count):
	for i in range(0, count):  
		tweets_file.append(ast.literal_eval(ftweets[i]))
	
		
		
		
def call_twitter_streaming_api():
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, 
                        ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # starts consuming public statuses that contain the keyword 'data'
    stream.statuses.filter(track='ozil')
    

call_twitter_search_api()
call_twitter_streaming_api()

top_hashtags = Counter(hashtag['text'].lower()
      for tweet in tweets
      for hashtag in tweet["entities"]["hashtags"])
print(top_hashtags.most_common(10))

count=len(tweets)
print(count)


