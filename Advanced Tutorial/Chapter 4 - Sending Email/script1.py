import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todoamin.com']

message = """From: From Person <from@fromdomain.com>
To: Person <to@todoamin.com>
Subject: STMP Email Test

This is a test email message"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully Sent Email")
except SMTPException:
    print("Error! Unable To Send Email")