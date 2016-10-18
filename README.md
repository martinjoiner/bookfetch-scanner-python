BookFetch Scanner
-----------------

### Python script to run the Raspberry Pi end of the BookFetch project. 

The script (`listen.py`) will listen for input from a USB barcode scanner, queueing scanned codes by storing them in a local SQLite database. A second script (`queue-worker.py`) will run simultaneously, checking for an internet connection and emptying the queue by POSTing the scans to the [BookFetch website](http://bookfetch.co.uk) via the REST API. 

This method means that the scanner can be operated offline and as soon as it finds an internet connection it will upload the scan data.


Installation
------------

Clone this repo to the Raspberry Pi.

Rename `user.example.json` to `user.json` and edit the contents so that the correct API URL, username and password are in the blank fields.

Set the OS to run both scripts on boot. (TODO: Lookup how to do this) 
