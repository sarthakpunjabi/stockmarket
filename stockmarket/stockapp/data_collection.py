import tweepy
from decouple import config
import pandas as pd
from stockapp.mlmodels import mymodel

consumer_key = config("API_KEY")
consumer_secret = config("API_KEY_SECRET")
access_token = config("ACCESS_TOKEN")
access_token_secret = config("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(
  consumer_key, 
  consumer_secret, 
  access_token, 
  access_token_secret
)


def get_tweets(news):
    print(news)
    query = news.split(" ")[2]
    api = tweepy.API(auth,wait_on_rate_limit=True)
    verify = api.verify_credentials()
    tweets = api.search_tweets("BAJAJ PULSAR SALES BREAKUP JUNE 2022 – 125, 150, 160, 200, 250CC - RUSHLANE", tweet_mode="extended")
    twee = tweepy.Cursor(api.search_tweets, q=query,lang='en',tweet_mode='extended').items(2000)
    list_tweets = [tweet for tweet in twee]

    data = []

    for tweet in list_tweets:
        try:
            print(tweet.retweeted_status.full_text)
            data.append((tweet.id_str,tweet.retweeted_status.full_text))
            print("=====")
        except AttributeError:
            print(tweet.full_text)
            data.append((tweet.id_str,tweet.full_text))
            print("=====")

    df = pd.DataFrame(data,columns = ['id','text'])

    result = mymodel(df)

    return result[0]
