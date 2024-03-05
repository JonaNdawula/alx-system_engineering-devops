#!/usr/bin/python3
"""
Function top_ten
"""
import requests


def top_ten(subreddit):
    """
    Return top ten posts of subreddit
    """
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "PythonScript"},
                            allow_redirects=False)
    if response.status_code >= 300:
        print("None")
    else:
        [print(child.get("data").get("title"))
         for child in response.json().get('data').get('children')]


if __name__ == "__main__":
    import sys
    top_ten(sys.argv[1])
