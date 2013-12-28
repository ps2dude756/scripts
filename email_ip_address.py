#!/usr/bin/python2

from auth.gmail import get_username, get_password
from lib.send_email import send_email_with_gmail
from scrapers.myexternalip import get_external_ip

FILENAME = './output/ip.txt'

def main():
    ip = get_external_ip()
    try:
        f = open(FILENAME, 'r+')
        old_ip = f.readline()
    except IOError:
        old_ip = ''
    
    if ip != old_ip:
        username = get_username()
        password = get_password()
        subject = 'Daily IP Report'
        content = 'The server\'s IP address is: {0}'.format(ip)
        send_email_with_gmail(username, password, username, subject, content)
        
        f = open(FILENAME, 'w')
        f.write(ip)

if __name__ == '__main__':
    main()
