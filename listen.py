#!/usr/bin/env python

import logging
import api


csrftoken = api.getCSRFToken()

print "Obtained CSRF Token: " + csrftoken

while True:
    barcode = raw_input("Enter something: ")
    if ( len(barcode) > 1 ):
        logging.info("Recording barcode: " + barcode)
        print "Recording barcode: " + barcode
        api.record(csrftoken, barcode)

