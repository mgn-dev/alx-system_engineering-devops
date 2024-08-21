#!/usr/bin/python3
"""
module that implements a function that returns
a list containing the titles of all hot articles.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. If no results are
    found for the given subreddit, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': '0-subs:v1.0.0'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            if not posts and not hot_list:
                return None
            hot_list.extend(post.get('data', {}).
                            get('title') for post in posts)
            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None
