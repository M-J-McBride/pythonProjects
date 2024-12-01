import sys
sys.path.insert(1,'/Users/michmcbr')
import script
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any

def send_email(to_email: str, body: str, subject: str | None):
    host: str = 'smtp-mail.outlook.com'
    port: int = 587

    context = ssl.create_default_context()
    with smtplib.SMTP(host, port) as server:
        print('Logging in....')
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(script.EMAIL, script.PASSWORD)

        # Prepare the email
        print('Attempting to send the email')
        message = MIMEMultipart()
        message['From'] = script.email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body,'plain'))

        server.sendmail(from_addr=script.EMAIL, to_addrs=to_email,msg=message.as_string())


if __name__ == '__main__':
    send_email(to_email='mmcbride164@gmail.com',
               body='TEST',
               subject='TEST EMAIL')