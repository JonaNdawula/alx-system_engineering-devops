#!/usr/bin/python3
""" Function Querire the Reddit API recursively"""


import requests


def count_words(subreddit, word_list, after='', wd_dict=None):
    """  Recursive function that queries the
    Reddit API, parses the title of all hot articles,
    and prints a sorted count of
    given keywords (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    """

    if wd_dict is None:
        wd_dict = {wd.lower(): 0 for wd in word_list}

    if after is None:
        wddict = sorted(wd_dict.items(), key=lambda i: (-i[1]. i[0]))
        for wd in wddict:
            if wd[1]:
                print(f'{wd[0]}: {wd[1]}')
        return None

    myUrl = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    hd = {'user-agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    response = requests.get(myUrl, headers=hd, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        ht = response.json()['data']['children']
        aft = response.json()['data']['after']
        for pst in ht:
            title = pst['data']['title']
            low_case = [wd.lower() for wd in title.split(' ')]

            for wd in wd_dict.keys():
                wd_dict[wd] += low_case.count(wd)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, wd_dict)
