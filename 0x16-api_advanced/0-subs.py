#!/usr/bin/python3
'''fetches from recdit api and prints the number of subscribers'''

import requests


def number_of_subscribers(subreddit):
    """Request number of subscribers of subreddit
    from Reddit API
    """
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    headers = {'User-Agent': 'zoubjd'}
    r = requests.get(url, headers=headers,
                            allow_redirects=False)

    if r.status_code != 200:
        return 0

    data = r.json()
    return data['data'].get('subscribers')
