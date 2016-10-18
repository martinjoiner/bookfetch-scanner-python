#!/usr/bin/env python

import os.path
import sqlite3

DB_FILE_NAME = "scan-queue.db"


# If the database file does not exist, create it
if not os.path.isfile( DB_FILE_NAME ):
    print "Creating database file " + DB_FILE_NAME
    file = open( DB_FILE_NAME, 'w+' )
    file.close()
else:
    print "Database file exists"


# Open connection to SQLite dababase
conn=sqlite3.connect(DB_FILE_NAME)
curs = conn.cursor()


# Check if scans table exists
scansExists = 0
for row in curs.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='scans'"):
    scansExists += 1


# Create scans table if required
if scansExists == 0:
    print "Creating scans table"
    curs.execute( """CREATE TABLE scans(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              isbn TEXT NOT NULL,
              shop_id INT NOT NULL
              )"""
    )
    conn.commit()
else:
    print "scans table exists"


# Print contents of scans table
print "Contents of scans table:"

for row in curs.execute("SELECT * FROM scans"):
    print row

def recordScan(isbn, shop_id):
    curs.execute("INSERT INTO scans ( isbn, shop_id ) VALUES ( '" + isbn + "', " + str(shop_id) + " )")
    conn.commit()

#conn.close()
