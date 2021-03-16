# Coursera, Google IT Automation with Python
# Course 6, Automating Real-World Tasks with Python
# Week 4, FINAL PROJECT, Part 1&2 of 5

import os
import requests
from PIL import Image

def main():
	source_dir = 'supplier-data/images'
	url = 'http://localhost/upload/'

	os.chdir(source_dir)	# making life easy
	for source in os.listdir():
		if source.endswith('.tiff'):
			target = os.path.splitext(source)[0] + '.jpeg'
			convert_image(source, target)
			upload_image(target, url)


def convert_image(source, target):
	"""Opens the source image, converts to the
	required format, and saves to the target path"""

	with Image.open(source) as img:
		img = img.convert('RGB')    	#Convert image to RGB
		img = img.resize((600,400)) 	#Resize image to given size
		img.save(target, 'JPEG')    	#Save image to new path
		print(source, 'converted successfully!', end='\t')


def upload_image(target, url):
	"""Opens the given file, and uploads to the
	provided url using the POST method"""

	with open(target, 'rb') as file:
		files = {'file': file}
		response = requests.post(url, files=files)
	print(target, "POST response:", response.status_code)


if __name__ == '__main__':
	main()
