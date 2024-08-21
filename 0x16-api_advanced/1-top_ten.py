#!/usr/bin/python3
"""
module that implements a function that returns
top 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': '0-subs:v1.0.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print(None)
            else:
                for post in posts:
                    print(post.get('data', {}).get('title'))
        else:
            print(None)
    except requests.RequestException:
        print(None)
