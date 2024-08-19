#!/usr/bin/python3
"""model doc"""
import requests


def top_ten(subreddit):
    """ Function that queries the Reddit API and prints
        the titles of the first 10 hot posts """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'custom-user-agent'
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get('data')
        for post in data.get('children'):
            print(post.get('data').get('title'))
    else:
        print("None")
        return
