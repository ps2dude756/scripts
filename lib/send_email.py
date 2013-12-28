#!/usr/bin/python2

import smtplib

def send_email_with_gmail(username, password, to_address, subject, content):
    headers = 'From: {0}\r\n' \
        'To: {1}\r\n' \
        'Subject: {2}\r\n\r\n'.format(
            username, 
            to_address, 
            subject
        )
    msg = headers + content
    
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(username, password)
    mailserver.sendmail(username, to_address, msg)
    mailserver.close()
