BookFetch Scanner
-----------------

### Python script to run the Raspberry Pi end of the BookFetch project. 

The script (`listen.py`) will listen for input from a USB barcode scanner, queueing scanned codes by storing them in a local SQLite database. A second script (`queue-worker.py`) will run simultaneously, checking for an internet connection and emptying the queue by POSTing the scans to the [BookFetch website](http://bookfetch.co.uk) via the REST API. 

This method means that the scanner can be operated offline and as soon as it finds an internet connection it will upload the scan data.


Installation
------------

Clone this repo to the Raspberry Pi, placing it in a folder in your user's home directory (user is usually `pi`).

Rename `user.example.json` to `user.json` and edit the contents, populating the blank fields with the correct API URL, username and password.

Set the Raspberry Pi to boot up in text console with the `pi` user automatically logged in. To do this run `sudo raspi-config`, choose `3) Boot Options` and then `B2) Console Autologin`

Configure the `pi` users account to automatically execute both the background queue worker script and the foreground listener script. To do this create a file called `.bash_login` in the users home directory with the following contents:

```
cd ~/bookfetch
python queue-worker.py > /dev/null &
python listen.py
```

_Note: The path on that first line will have to match the location that you cloned the repo into_

You are now free to power on the Raspberry Pi with only the scanner attached and it should record scans.
