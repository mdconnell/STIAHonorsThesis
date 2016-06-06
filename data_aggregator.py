import tweepy
import time
import json
from database_handler import add_tweet
import re


consumer_key = "8m1UdV9ESW7z3S7paHZS6l6Pm"
consumer_secret = "6JdZiQu7CTWnormk5hKvkyRsG9cCRzVeTHd8XYCwmc5z0Us11X"
access_token = "2408924693-cW4lQORJcLHhaR4z5Fdep0JA29Fg3hKPlmRyQlz"
access_token_secret = "9eaMBKeCTLi0ufSsUS5ZuVR6p6h100pSTxlJlDsZgTCJ6"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_terms = "transgenic","genetically modified", "genetically engineered", "gmo", "monsanto"
location = ["-99.271467", "40.853367", "1500mi"]


# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
        #check if streamed object is indeed a tweet, then add it to db if so
        try:
        #print tweet['user']['screen_name'], tweet['text'], tweet['coordinates']
            add_tweet(decoded)
            print "\n\n"+decoded["user"]["screen_name"]+":\n"+decoded["text"]+"\n"
            print decoded["user"]["location"], str(decoded["coordinates"])
            print json.dumps(decoded, sort_keys=True,indent=4, separators=(',', ': '))

            return True
        except: TypeError

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    print "Showing all new tweets for \""+str(", ".join(search_terms))+"\""
    stream = tweepy.Stream(auth, l)
    stream.filter(track=search_terms)