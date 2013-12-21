#!/usr/bin/python2

from bs4 import BeautifulSoup
import urllib2

def get_external_ip():
    url = "http://myexternalip.com/raw"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    
    return soup.text[:-1]
