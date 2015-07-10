#!/usr/bin/env python

import smtplib, datetime, os

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders

senderEmail = ""
sendPass = ""
smtpServ = ""
sendPort = 587

currentDate = str(datetime.date.today())

# forming message

msg = MIMEMultipart()

msg['Subject'] = "RTW Report for " + currentDate
msg['From'] = senderEmail
msg['To'] = ''
body = """Please see the attached .zip file.

- Your Friendly Neighbourhood Server
"""
msg.attach(MIMEText(body, 'plain'))


# grabbing attachment

files_to_attach = os.listdir('_PATH_')

for file in files_to_attach:
	file = os.path.abspath(os.path.join('_PATH_, file))
	part = MIMEBase('application', "octet-stream")
	part.set_payload( open(file, "rb").read() )
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
	msg.attach(part)
	




# connecting to smtp server and sending

server = smtplib.SMTP(smtpServ, sendPort)

server.starttls()
server.login(senderEmail.partition('@')[0], sendPass)
server.sendmail(senderEmail, '_EMAIL_', msg.as_string())


