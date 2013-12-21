#!/usr/bin/python2

from auth.gmail import get_username, get_password
from lib.send_email import send_email_with_gmail
from scrapers.myexternalip import get_external_ip

def main():
    ip = get_external_ip()
    username = get_username()
    password = get_password()
    subject = 'Daily IP Report'
    content = 'The server\'s IP address is: ' + ip
    send_email_with_gmail(username, password, username, subject, content)

if __name__ == '__main__':
    main()
