#!/usr/bin/env python

import logging
import api
import db

print "Obtaining CSRF token, please wait..."

csrftoken = api.getCSRFToken()

print "CSRF token obtained: " + csrftoken

while True:
    barcode = raw_input("Enter something: ")
    if ( len(barcode) > 1 ):
        logging.info("Recording barcode: " + barcode)
        print "Recording barcode: " + barcode
        db.recordScan(barcode, 1)
        #api.record(csrftoken, barcode)

