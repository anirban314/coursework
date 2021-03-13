# Coursera, Google IT Automation with Python
# Course 2, Using Python to Interact with the Operating System
# FINAL ASSIGNMENT
# Log Analysis Using Regular Expressions

import re
import csv
import operator

users_dict = {}
error_dict = {}

file = open("files/syslog.log", 'r')
for line in file:
	log = re.findall(r"ticky: ([A-Z]*?) (.*?) \((.*?)\)$", line)[0]

	if log[2] not in users_dict:
		users_dict[log[2]] = {'info':0, 'error':0}

	if log[0] == 'INFO':
		users_dict[log[2]]['info'] += 1

	if log[0] == 'ERROR':
		users_dict[log[2]]['error'] += 1
		error_dict[log[1]] = error_dict.get(log[1], 0) + 1
file.close()

users_dict = {key:value for key,value in sorted(users_dict.items(), key=operator.itemgetter(0))}
error_dict = {key:value for key,value in sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)}

with open("files/user_statistics.csv", 'w+') as file:
	writer = csv.writer(file, delimiter=',')
	writer.writerow(["Username", "INFO", "ERROR"])
	writer.writerows([user[0], user[1]['info'], user[1]['error']] for user in users_dict.items())

with open("files/error_message.csv", 'w+') as file:
	writer = csv.writer(file, delimiter=',')
	writer.writerow(["Error", "Count"])
	writer.writerows([error[0], error[1]] for error in error_dict.items())