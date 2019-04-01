import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todoamin.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Sending An HTML Email

This Is An Email In HTML Format

<h1>This Is A Heading</h1>
<p>This Is A Paragraph</p>"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully Sent Email")
except SMTPException:
    print("Error! Unable To Send Email")