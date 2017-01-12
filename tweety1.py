import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import json
from textblob import TextBlob
import HTMLParser
from tweepy.streaming import StreamListener

# keys generated to use ethe twitter API
ckey="XQRiQMrYJhdsGwbD4bxFlx2fN"
csecret="sQVJbuSYeiGhud1LzeU7bJeXaNyc2jU6D0v9qzwyWTK3HXTC4d"
atoken="796755551904468992-xZbWsYMp5XzNnzPigrzF1KKwSDtKoms"
asecret="60d6Af3aXqbrjEBcTSwhWIk06Jldu4hLinkqu9KtdqJvW"



auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api =  tweepy.API(auth)

public_tweets = api.search('airtel')
i = 0
tweets_airtel = []
for tweet in public_tweets:
	text_tweet =  (tweet.text).encode('utf-8').strip()
	tweets_airtel.append(text_tweet)
	print tweets_airtel[i], "\n"
	i+=1
