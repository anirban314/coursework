# Coursera, Google IT Automation with Python
# Course 6, Automating Real-World Tasks with Python
# Week 4, FINAL PROJECT, Part 5 of 5

import os
import psutil
import socket
import emails

def main():
	if check_cpu_usage(used_percent=80):
		warn_by_email('Error - CPU usage is over 80%')
	
	if check_dsk_usage(used_percent=80):
		warn_by_email('Error - Available disk space is less than 20%')
	
	if check_mem_usage(free_MB=500):
		warn_by_email('Error - Available memory is less than 500MB')
	
	if check_localhost(ip='127.0.0.1'):
		warn_by_email('Error - localhost cannot be resolved to 127.0.0.1')


def warn_by_email(subject):
	"""Creates and sends email to current user
	based on the subject line provided"""

	email_params = {
		'from'    : 'automation@example.com',
		'to'      : f"{os.environ['USER']}@example.com",
		'subject' : subject,
		'content' : 'Please check your system and resolve the issue as soon as possible.'
	}

	# Generate and send the email with no attachment
	message = emails.create_email(params=email_params)
	emails.send_email(message)


def check_cpu_usage(used_percent):
	return psutil.cpu_percent(1) > used_percent

def check_dsk_usage(used_percent):
	return psutil.disk_usage('/').percent > used_percent

def check_mem_usage(free_MB):
	return psutil.virtual_memory().available / 1024**2 < free_MB

def check_localhost(ip):
	return socket.gethostbyname('localhost') != ip


if __name__ == '__main__':
	main()