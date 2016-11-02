#!/usr/bin/env python

import os.path
import db

SHOPCODE_FILENAME = "shop_code.temp"

current_shop_code = ""


# Write a .temp to disk to store the current shop code
def storeCurrentShopCode(new_code):
    file = open( SHOPCODE_FILENAME, 'w+')
    file.write(new_code)
    file.close()


def printCurrentShopCode():
    print "Shop code set to to " + current_shop_code


# On load, check if a shop_code file exists
if os.path.isfile( SHOPCODE_FILENAME ):
    file = open( SHOPCODE_FILENAME, 'r' )
    current_shop_code = file.read()
    file.close()
    print SHOPCODE_FILENAME + " file found"
    printCurrentShopCode()
else:
    print "No shop code set!"
    

while True:
    barcode = raw_input("Scan something: ")
    if ( barcode[:3] == 'BF-' ):
        current_shop_code = barcode[3:]
        storeCurrentShopCode(current_shop_code)
        printCurrentShopCode()
    else:
        print "ISBN " + barcode + " scanned in " + current_shop_code
        db.recordScan(barcode, current_shop_code)
        

