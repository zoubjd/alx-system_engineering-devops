#!/usr/bin/python3
'''fetches from recdit api and prints the number of subscribers'''

def number_of_subscribers(subreddit):
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url)
    subs = r.json().get('data').get('subscribers')
    return subs
