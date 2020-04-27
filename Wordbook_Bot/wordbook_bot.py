import praw
import time
import os
import requests
import json
import bot_login
import psycopg2
import re
import random

def run_bot(r):
    try:
        subreddit = r.subreddit("Shinobunfriends")
        for comment in subreddit.stream.comments():
            print(comment.body)
            if re.search("Shinobu Order", comment.body, re.IGNORECASE):
                    marvin_reply = "[Suggested watch order](https://media.discordapp.net/attachments/652432414135681060/662034140505571378/6gqy1AQaz0AXwlkBaVPMP-ST8fwleVWMLFXAcWkBHOM.png?width=617&height=904)"
                    comment.reply(marvin_reply)
                    print(marvin_reply)
    
    # Low karma
    except Exception as e:
        time_remaining = 15
        if (str(e).split()[0] == "RATELIMIT:"):
            for i in str(e).split():
                if (i.isdigit()):
                    time_remaining = int(i)
                    break
            if (not "seconds" or not "second" in str(e).split()):
                time_remaining *= 60

        print (str(e.__class__.__name__) + ": " + str(e))
        for i in range(time_remaining, 0, -5):
            print ("Retrying in", i, "seconds..")
            time.sleep(5)

if __name__ == "__main__":
    while True:
        try:
            print ("\nBot on...")
            r = bot_login.bot_login()
            print ("\nBot log")
            run_bot(r)
            time.sleep(10)
        except Exception as e:
                print (str(e.__class__.__name__) + ": " + str(e))
                time.sleep(15)