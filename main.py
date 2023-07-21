# -*- coding: utf-8 -*-

import tweepy

ckey = "***"
csecret = "***"
atoken = "***"
asecret = "***"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

public_tweets=api.home_timeline(count=3)

for tweet in public_tweets:
    print(tweet.text)

my_retweets=api.retweets_of_me()
for tweets in my_retweets:
    print(tweets.text)


for status in tweepy.Cursor(api.user_timeline, id='lebigdata_fr').items():
    print(status.text)
    print(status.id)
    print(status.created_at)
    print(status.retweet_count)



for status in tweepy.Cursor(api.user_timeline, id='lebigdata_fr').items(20):
    hashtaglist=[]
    try:
        for hashtag in status.entities['hashtags']:
            hashtaglist.append(hashtag['text'])
        print(hashtaglist)
    except:
        pass

for status in tweepy.Cursor(api.user_timeline, id='lebigdata_fr').items(10):
    linklist=[]
    try:
        for link in status.entities['urls']:
            linklist.append(link['expanded_url'])
            print(linklist)
    except:
        pass

for status in tweepy.Cursor(api.user_timeline, id='lebigdata_fr').items(10):
    medialist=[]
    try:
        for media in status.entities['media']:
            medialist.append(media['epxanded_url'])
        print(medialist)
    except:
        pass

for status in tweepy.Cursor(api.user_timeline, id='CocaCola').items():
    print(status.text)
    print(status.id)
    print(status.created_at)

for status in tweepy.Cursor(api.user_timeline, id='CocaCola').items(10):
    hashtaglist=[]
    try:
        for hashtag in status.entities['hashtags']:
            hashtaglist.append(hashtag['text'])
        print(hashtaglist)
    except:
        pass
for status in tweepy.Cursor(api.user_timeline, id='CocaCola').items(10):
    linklist=[]
    try:
        for link in status.entities['urls']:
            linklist.append(link['expanded_url'])
        print(linklist)
    except:
        pass
for status in tweepy.Cursor(api.user_timeline, id='CocaCola').items(10):
    medialist=[]
    try:
        for media in status.entities['media']:
            medialist.append(media['expanded_url'])
        print(medialist)
    except:
        pass

