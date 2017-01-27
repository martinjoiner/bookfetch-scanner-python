#!/usr/bin/env python
import requests
import json

user_data = {}

# Open user.json file to get credentials
with open('user.json') as user_file:
    user_data = json.load(user_file)

url_root = user_data['api_url']

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'BookFetch Roaming Scanner v1.0'
}

# Returns a string, blank if request failed
def getAccessToken():
    
    url = url_root + '/oauth/token'

    # Construct the data dict
    data = {
        'grant_type': 'password',
        'client_id': user_data['client_id'],
        'client_secret': user_data['client_secret'],
        'username': user_data['username'],
        'password': user_data['password'],
        'scope': ''
    }
    
    try:
        r = requests.post(  url,
                            headers=headers,
                            data=data,
                            timeout=10)

        rVals = json.loads(r.text)
        return rVals['access_token']
    except:
        return ''
    

# POST a new 'scan' to the API 
def record(access_token, shop_code, isbn):

    url = url_root + '/api/scan'
    
    # Construct the headers dict
    authheaders = headers
    authheaders['Authorization'] = 'Bearer ' + access_token
    
    # Construct the data dict
    data = {
        'isbn': isbn,
        'shop_code': shop_code
    }
    
    # Make the API call
    try:
        response = requests.post(url,
                                 headers=authheaders,
                                 data=data,
                                 timeout=10
                            )
    except:
        return 404
    
    return response.status_code 




