"""
Day 18: API Calls - GitHub Data Fetcher

Objective:
Build a script that can interact with the GitHub API to fetch user data and
repository information, handling authentication and rate limits.

Learning Objectives:
1. Making HTTP requests
2. Working with APIs
3. Handling responses
4. Managing authentication

Detailed Instructions:
1. Request Basics (15 mins):
   - Install requests
   - Make GET calls
   - Handle responses
   - Check status

2. Authentication (15 mins):
   - Set up tokens
   - Add headers
   - Handle auth
   - Test access

3. Data Processing (15 mins):
   - Parse JSON
   - Extract fields
   - Handle errors
   - Format output

4. Rate Limiting (15 mins):
   - Check limits
   - Handle waits
   - Retry requests
   - Log usage

Key Concepts:
1. Making Requests:
   ```python
   import requests
   
   # Basic GET request
   response = requests.get(
       'https://api.github.com/users/username',
       headers={'Authorization': f'token {token}'}
   )
   ```

2. Response Handling:
   ```python
   if response.status_code == 200:
       data = response.json()
       print(f"User: {data['login']}")
   else:
       print(f"Error: {response.status_code}")
   ```

Challenge Tasks:
1. Add pagination
2. Implement caching
3. Create rate tracker
4. Add async requests

Tips for Success:
- Check status codes
- Handle rate limits
- Add error handling
- Use proper headers

Common Mistakes to Avoid:
- Exposed tokens
- Missing error checks
- No rate limiting
- Blocking calls
"""

# Only necessary imports
import requests
import time
from typing import Dict, List, Optional

class GitHubDataFetcher:
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def get_user_data(self, username: str) -> Optional[Dict]:
        url = f"{self.base_url}/users/{username}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching user data: {response.status_code}")
            return None
    
    def get_repo_data(self, username: str) -> Optional[List[Dict]]:
        url = f"{self.base_url}/users/{username}/repos"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching repository data: {response.status_code}")
            return None

def main():
    # TODO: Implement main function to demonstrate GitHub data fetching
    pass

if __name__ == "__main__":
    main()
