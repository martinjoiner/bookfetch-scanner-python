#!/usr/bin/env python

import db
import api
import time

csrftoken = ''

while True:

    if len(csrftoken) == 0:
        print "Obtaining CSRF token, please wait..."
        csrftoken = api.getCSRFToken()
    
        if len(csrftoken) == 0:
            print "CSRF token could not be obtained, waiting for 5 seconds"
            time.sleep(5)
            continue
        else:
            print "CSRF token obtained: " + csrftoken
    
    # Check if there are items in the queue
    scan = db.frontQueueItem()
    if scan is not None:
        print scan;
    
        # Attempt to POST to API
        print "Attempting POST to API"
        if api.record(csrftoken, scan["isbn"]):
            print "POST to API successful, deleting item from queue"

            # Delete the item from the queue
            db.deleteQueueItem( scan["id"] )
        else:
            print "POST to API failed, waiting for 5 seconds..."
            time.sleep(5)
    else:
        print "Nothing in queue, waiting for 5 seconds..."
        # If failed, wait 20 seconds
        time.sleep(5)
