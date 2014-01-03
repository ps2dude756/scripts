get\_marvel\_publications.py
----------
Obtains a list of all Marvel comics printed between a given start and stop year
according to http://marvel.wikia.com, and prints them to a given output file,
with any errors being printed to a given log file.

email\_ip\_address.py
----------
Obtains ip address from http://myexternalip.com, and if it has changed since
last run, sends an email containing the ip address to a gmail account.

In order to use, first create the file auth/gmail.py. It should contain two 
functions, get\_username and get\_password, each of which return your gmail 
username and password as Python strings.
