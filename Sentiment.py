# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 19:09:12 2017

@author: Shanmukh Agastyaraju
"""

import tweepy
from textblob import TextBlob
import pandas as pd


user_key= 'Enter your consumer key'
user_secret= 'Enter your consumer key secret'

access_token='Enter the access token'
access_token_secret='Enter the access token secret'

authentication = tweepy.OAuthHandler(user_key, user_secret)
authentication.set_access_token(access_token, access_token_secret)

api = tweepy.API(authentication)

tweet_api = input('Enter the keyword: ')
all_tweets = api.search(tweet_api)

def AnalyseSentiment(polarity):
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"
        
Tweets=[]
Polarities=[]

for tweet in all_tweets:
    Tweets.append(tweet.text)
    s_analysis = TextBlob(tweet.text)
    p = AnalyseSentiment(s_analysis.sentiment.polarity)
    Polarities.append(p)

k = list(zip(Polarities, Tweets))
df = pd.DataFrame(k, columns=['Polarity', 'Tweet'])
print(df)
df.to_csv('TwitterSentimentAnalysis.csv',index=False)
df.Polarity.value_counts().plot(kind='bar')