#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit
        
    Returns:
        int: Number of subscribers, or 0 if invalid subreddit
    """
    # Reddit API endpoint for subreddit info
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set custom User-Agent to avoid "Too Many Requests" errors
    headers = {
        'User-Agent': 'MyRedditApp/1.0 by YourUsername'
    }
    
    try:
        # Make the API request
        # allow_redirects=False prevents following redirects to search results
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract subscriber count from the response
            # The structure is: data -> data -> subscribers
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            # Invalid subreddit or other error
            return 0
            
    except Exception:
        # Handle any exceptions (network errors, JSON parsing errors, etc.)
        return 0


# Example usage and testing
if __name__ == "__main__":
    # Test with valid subreddit
    print(f"Programming subreddit: {number_of_subscribers('programming')}")
    
    # Test with invalid subreddit
    print(f"Fake subreddit: {number_of_subscribers('this_is_a_fake_subreddit')}")
    
    # Test with some popular subreddits
    print(f"Python subreddit: {number_of_subscribers('Python')}")
    print(f"AskReddit: {number_of_subscribers('AskReddit')}")
