# Coursera, Google IT Automation with Python
# Course 6, Automating Real-World Tasks with Python
# Week 4, FINAL PROJECT, Part 3 of 5

import os
import requests

def main():
	source_dir = 'supplier-data/descriptions'
	url = 'http://localhost/fruits/'

	os.chdir(source_dir)	# making life easy
	for filename in os.listdir():
		if filename.endswith('.txt'):
			update_catalog(filename, url)


def update_catalog(filename, url):
	"""Calls text_to_dict() to convert text file to dict
	and uploads the returned dict to the given url"""

	payload = text_to_dict(filename)
	response = requests.post(url, json=payload)
	print(filename, "POST response:", response.status_code)


def text_to_dict(filename):
	"""Reads each line from given text file and
	puts them into a dictionary and returns it"""

	with open(filename, 'r') as file:
		text = [line.strip() for line in file]
	return {
		'name': text[0],
		'weight': int(text[1].strip(' lbs')),
		'description': text[2],
		'image_name': os.path.splitext(filename)[0] + '.jpeg'
	}


if __name__ == '__main__':
	main()
