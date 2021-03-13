# Coursera, Google IT Automation with Python
# Course 6, Automating Real-World Tasks with Python
# Week 2, Interacting with Web Services

import os
import requests

def main():
	source_dir = 'files'
	os.chdir(source_dir)
	for path in os.listdir():
		if path.endswith('.txt'):
			payload = text_to_dict(path)
			response = requests.post('http://localhost/feedback/', json=payload)
			if response.ok:
				print(f"{path} processed! Response: {response.status_code}")
			else:
				print(f"{path} FAILED! Response: {response.status_code}")
	print("DONE")

def text_to_dict(path):
	with open(path) as file:
		lines = [line.strip() for line in file]
	return {
		'title': lines[0],
		'name': lines[1],
		'date': lines[2],
		'feedback': lines[3]
	}

if __name__ == "__main__":
	main()