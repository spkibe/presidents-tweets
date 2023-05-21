import pandas as pd
import tweepy
from datetime import datetime

# twitter api credentials
ACCESS_TOKEN = 'XXXXXX'
ACCESS_SECRET = 'XXXXX'
CONSUMER_KEY = 'XXXXX'
CONSUMER_SECRET = 'XXXXX'


# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit = True)
    return api

limit = 500
# Create API object
api = connect_to_twitter_OAuth()

print("try again")
tweets = []
# scraping 2000 tweets
for i in range(100):
    tweets.extend(api.user_timeline(
        screen_name = '@WilliamsRuto',
        include_rts = True,
        # keep full text
        tweet_mode = 'extended'

    ))

tweet_list = []
for tweet in tweets:
    text = tweet._json['full_text']

    refined_tweet = {
        'user': tweet.user.screen_name,
        'text' : text,
        'favorite_count': tweet.favorite_count,
        'retweet_count' : tweet.retweet_count,
        'create_at': tweet.created_at,
    }

    tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)

df.to_csv('william_ruto_tweets.csv')
print("done")



william = pd.read_csv("william_ruto_tweets.csv")
print(william.shape)
