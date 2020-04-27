import praw
import time
import os
import requests
import json
import bot_login
import psycopg2
import re

if __name__ == "__main__":
    print ("\nBot on...")
    r = bot_login.bot_login()
    print ("\nBot log")
    try:
        marvin_quotes = \
        [
        "It's not good to expect too much, but you can't do anything if you're being overly pessimistic. If you just wait thinking it's useless, nothing will come of it.",
        "No matter what bonds you forge with others, time will tear them apart. Well... Doesn't thinking about it make you sick?",
        "It's difficult to change the world on your own, but twisting it a little might not be all that hard.",
        "There's no reason a fake can't do what the real thing would. And it's possible for a fake to be more real than the real thing.",
        "The sun is my enemy, but the moon has been good to me.",
        "We can't let the past be mere water under the bridge. Even so, there's no reason that we can't come together."
        ]

        reddit = praw.Reddit('bot1')

        subreddit = reddit.subreddit("DuckGameClips")

        for comment in subreddit.stream.comments():
            print(comment.body)
            if re.search("Shinobu Help", comment.body, re.IGNORECASE):
                    marvin_reply = "Shinobu says: " + random.choice(marvin_quotes)
                    comment.reply(marvin_reply)
                    print(marvin_reply)
     except Exception as e:
        print (str(e.__class__.__name__) + ": " + str(e))