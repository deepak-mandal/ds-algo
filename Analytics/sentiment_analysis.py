
#Import Libraries
import tweepy
from textblob import TextBlob

#Twitter Authentication



#Twitter Authentication 
consumer_key = '08OOW0qCZhjYrWGieb6PhxzUn' 
consumer_secret = 'l2d3EcXrQhrVqfNyAI8mHakN4AocOmzvDQvn9pR46PBXADSrr4' 
access_token = '1212320988563558406-EwwCCuQp2zxEZJO4t61sZkiscbP7UV' 
access_token_secret = 'iE0q6Ml4x8rVzWEVL0OsYvDm8HZP91NNIEFt6Ev2TOMZC'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Reading data from twitter
api = tweepy.API(auth)
public_tweets = api.search('mandal')

#Printing the data read from twitter
for tweet in public_tweets:
    print(tweet.text)
    
#Performing Sentiment Analysis
    analysis = TextBlob(tweet.text)
    type(analysis)
    print(analysis.sentiment)
