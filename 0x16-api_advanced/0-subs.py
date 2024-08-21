#!/usr/bin/python3
"""
module that implements a function that returns
number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0.
    """
    user = {'User-Agent': '0-subs:v1.0.0'}
    url = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                       headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0
