import praw
import time
import os
import requests
import json
import bot_login
import psycopg2
import re

if __name__ == "__main__":
    while True:
        try:
            r = bot_login.bot_login()
        except Exception as e:
            print (str(e.__class__.__name__) + ": " + str(e))
            time.sleep(15)
