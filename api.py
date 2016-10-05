#!/usr/bin/env python
import requests
import json

URL_ROOT = 'http://loc.charitystock'
user_data = {}

# Open user.json file to get credentials
with open('user.json') as user_file:
    user_data = json.load(user_file)
    
def getCSRFToken():
    path = '/rest/session/token'
    url = URL_ROOT + path 
    r = requests.get(url)
    return r.text


# Query the API with this barcode
def record(CSRFToken, barcode):

    path = '/entity/node'
    url = URL_ROOT + path
    
    # Construct the headers dict
    headers = { 
        'Content-Type': 'application/hal+json',
        'X-CSRF-Token': CSRFToken
    }
    #print headers
    
    # Construct the data dict
    data = { '_links': {} }
    data['_links']['type'] = {}
    data['_links']['type']['href'] = URL_ROOT + '/rest/type/node/scan'
    data['title'] = [ {'value': barcode} ]
    #print data
    
    # Make the API call
    response = requests.post(url, auth=(user_data['user'], user_data['pass']), headers=headers, data=json.dumps(data) )
    print response
    #json = response.json()
    #print json

