#!/usr/bin/python3
"""function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
if subreddit is invalid return 0
"""

import requests


def number_of_subscribers(subreddit):
    """Will Returns total Number of subscribers on Reddit subreddit"""
    Reddit_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    resp = requests.get(Reddit_url, headers={"User-Agent": "app/1.0"},
                        allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0


if __name__ == "__main__":
    numbert_of_subscribers(argv[1])
