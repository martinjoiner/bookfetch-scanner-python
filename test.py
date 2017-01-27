#!/usr/bin/env python
import requests
import json

user_data = {}

# Open user.json file to get credentials
with open('user.json') as user_file:
    user_data = json.load(user_file)

url_root = user_data['api_url']

headers = {
    'User-Agent': 'BookFetch Roaming Scanner v1.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

url = url_root + '/api/test'

print url
    
r = requests.post(url, headers=headers, timeout=10)
print r

    


