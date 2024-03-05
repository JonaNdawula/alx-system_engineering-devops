#!/usr/bin/python3
"""
Defines a recursive function
that queries the Reddit API and returns
a list containing titles of all hot
articles for a subreddit
"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """ Will return a list containing the titles"""

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers={"User-Agent": "PythonScript"},
                            params={"count": count, "after": after},
                            allow_redirects=False)
    if response.status_code >= 400:
        return None

    hotlist = hot_list + [child.get("data").get("title")
                          for child in response.json()
                          .get("data")
                          .get("children")]
    pg_info = response.json()
    if not pg_info.get("data").get("after"):
        return hotlist

    return recurse(subreddit, hotlist, pg_info.get("data").get("count"),
                   pg_info.get("data").get("after"))
