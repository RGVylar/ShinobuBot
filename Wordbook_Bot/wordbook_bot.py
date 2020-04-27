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

            

            

            print ("\nFetching comments..")
            while True:
                # Fetching all new comments that were created after created_utc time
                
                time.sleep(10)

        except Exception as e:
            print (str(e.__class__.__name__) + ": " + str(e))
            time.sleep(15)
