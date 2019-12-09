
import os
import tweepy as tw
import pandas as pd
import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

CONSUMER_KEY = "xxxxxxxxxxxx"
CONSUMER_SECRET = "xxxxxxxxxxxx"
ACCESS_TOKEN = "xxxxxxxxxxxx-xxxxxxxxxxxx"
ACCESS_TOKEN_SECRET = "xxxxxxxxxxxx"


auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

userName = input("Please Enter User's username: ")

if len(userName) > 0:
    print("Getting data for " + userName)
    item = api.get_user(userName)
    print("name: " + item.name)
    print("screen_name: " + item.screen_name)
    print("description: " + item.description)
    print("statuses_count: " + str(item.statuses_count))
    print("friends_count: " + str(item.friends_count))
    print("followers_count: " + str(item.followers_count))
else:
    exit(1)


dataset = ""
for status in tw.Cursor(api.user_timeline, screen_name=userName, tweet_mode="extended").items():
    print(status.full_text + " From: " + status.user.location + "\n------------------------\n")
    dataset+=status.full_text

dataset = dataset.lower()

maskArray = npy.array(Image.open("cloud.png"))
cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
cloud.generate(dataset)
cloud.to_file("wordCloud.png")



    



