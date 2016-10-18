BookFetch-Scanner
-----------------

### Python script to run the Raspberry Pi end of the BookFetch project. 

A script will listen for input from a USB barcode scanner, queueing scanned codes by storing them in a local SQLite database. A second script will run simultaneously, checking for an internet connection and emptying the queue by POSTing the scans to the [BookFetch website](http://bookfetch.co.uk) via the REST API. 


Installation
------------

Clone this repo to the Raspberry Pi.

Rename `user.example.json` to `user.json` and edit the contents so that the correct API URL, username and password are in the blank fields.

Set the OS to run both scripts on boot. (TODO: Lookup how to do this) 
