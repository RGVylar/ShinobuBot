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