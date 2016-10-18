#!/usr/bin/env python

import logging
import db

while True:
    barcode = raw_input("Scan ISBN: ")
    if ( len(barcode) > 1 ):
        logging.info("Recording scanned ISBN: " + barcode)
        print "Recording scanned ISBN: " + barcode
        db.recordScan(barcode, 1)
        

