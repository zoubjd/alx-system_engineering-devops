#!/usr/bin/python3
"""fetches from api"""
import requests


def number_of_subscribers(subreddit):
    """ returns number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'custom-user-agent'
        }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get('data')
        return data.get('subscribers')
    else:
        return 0
