# Coursera, Google IT Automation with Python
# Course 2, Using Python to Interact with the Operating System
# Week 4, Managing Data and Processes
# Read given log file and search for the error input by the user

# NOTE: Input the path to the log file as a commandline argument

import re
import sys

def error_search(log_file):
	error = input("What is the error? ")
	error_patterns = error.lower().split()
	returned_errors = []
	with open(log_file, mode='r', encoding='UTF-8') as file:
		for log in file.readlines():
			if all(re.search(pattern, log.lower()) for pattern in error_patterns):
				returned_errors.append(log)
	return returned_errors

def file_output(returned_errors):
	with open('files/errors_found.log', 'w') as file:
		for error in returned_errors:
			file.write(error)


if __name__ == "__main__":
	log_file = sys.argv[1]
	returned_errors = error_search(log_file)
	file_output(returned_errors)
	sys.exit(0)
