#!/usr/bin/python3
"""
Module that queries Reddit API for number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If invalid subreddit, returns 0.
    """
    if not isinstance(subreddit, str) or not subreddit:
        return 0
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:reddit.api.script:v1.0 (by /u/test_user)'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if we got redirected (invalid subreddit)
        if response.status_code == 302:
            return 0
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            # Check if the response contains valid subreddit data
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
        
        return 0
    
    except (requests.RequestException, ValueError, KeyError):
        return 0
