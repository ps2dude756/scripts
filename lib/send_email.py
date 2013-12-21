import smtplib

def send_email_with_gmail(username, password, to_address, subject, content):
    headers = 'From: ' + username + '\r\n' + \
        'To: ' + to_address + '\r\n' + \
        'Subject: ' + subject + '\r\n\r\n'
    msg = headers + content
    
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(username, password)
    mailserver.sendmail(username, to_address, msg)
    mailserver.close()
