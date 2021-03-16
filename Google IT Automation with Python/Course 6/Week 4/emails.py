# Coursera, Google IT Automation with Python
# Course 6, Automating Real-World Tasks with Python
# Week 4, FINAL PROJECT

import os
import mimetypes
import smtplib
from email.message import EmailMessage


def create_email(params, attachment=None):
	"""Generates the message to be emailed and returns it"""

	message = EmailMessage()
	message['from'] = params['from']
	message['to'] = params['to']
	message['subject'] = params['subject']
	message.set_content(params['content'])
	
	if attachment != None:
		mime_type = mimetypes.guess_type(attachment)[0]
		mime_type, mime_subtype = mime_type.split('/')
		with open(attachment, 'rb') as file:
			message.add_attachment(
				file.read(),
				maintype=mime_type,
				subtype=mime_subtype,
				filename=os.path.basename(attachment))
	return message


def send_email(message):
	"""Emails the message using the local mailserver"""

	mail_server = smtplib.SMTP('localhost')
	mail_server.send_message(message)
	mail_server.quit()
