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
def connect():
    return sqlite3.connect(DB_FILE_NAME)
    #curs = conn.cursor()


# Check if scans table exists
scansExists = 0
conn = connect();
for row in conn.cursor().execute("SELECT name FROM sqlite_master WHERE type='table' AND name='scans'"):
    scansExists += 1


# Create scans table if required
if scansExists == 0:
    print "Creating scans table"
    conn.cursor().execute( """CREATE TABLE scans(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              isbn TEXT NOT NULL,
              shop_id INT NOT NULL
              )"""
    )
    conn.commit()
else:
    print "scans table exists"

conn.close()


# Returns a dict representing a 
def frontQueueItem():
    conn = connect()
    for row in conn.cursor().execute("SELECT id, isbn, shop_id FROM scans ORDER BY id LIMIT 1"):
        scan = {}
        scan["id"] = row[0]
        scan["isbn"] = row[1]
        scan["shop_id"] = row[2]
        conn.close()
        return scan
    conn.close()


# Deletes a row from the scan table
def deleteQueueItem(id):
    conn = connect()
    conn.cursor().execute("DELETE FROM scans WHERE id = " + str(id) )
    conn.commit()
    conn.close()


# Adds an item to queue
def recordScan(isbn, shop_id):
    insert = "INSERT INTO scans ( isbn, shop_id ) VALUES ( ?, ? )"
    conn = connect()
    conn.cursor().execute(insert, [isbn, shop_id])
    conn.commit()
    conn.close()
