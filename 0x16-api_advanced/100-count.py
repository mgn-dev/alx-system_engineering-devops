#!/usr/bin/python3
"""
module that implements a function that parses the title of
all hot articles, and prints a sorted count of given keywords.
"""
from collections import Counter
import re
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    if counts is None:
        counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': '0-subs:v1.0.0'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])

        # Process each post title
        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            for word in word_list:
                word_lower = word.lower()
                matches = re.findall(r'\b{}\b'.format(re.escape(word_lower)),
                                     title)
                counts[word_lower] += len(matches)

        after = data.get('after')
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            # Sorting and printing
            for word, count in sorted(counts.items(),
                                      key=lambda item: (-item[1], item[0])):
                if count > 0:
                    print(f"{word}: {count}")
    except requests.RequestException:
        return
