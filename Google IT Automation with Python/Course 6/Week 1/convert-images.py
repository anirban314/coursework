# Coursera, Google IT Automation with Python
# Course 6, Automating Real-World Tasks with Python
# Week 1, Manipulating Images

import os
import sys
from PIL import Image

def main():
	#Validate user-given arguments
	if not check_no_of_argvs(sys.argv):
		sys.exit(1)
	if not validate_source_dir(sys.argv[1]):
		sys.exit(2)
	if not validate_destination_dir(sys.argv[3]):
		sys.exit(3)
	
	#Unpack arguments
	source_dir, source_ext, destination_dir = sys.argv[1:]

	for source_file in os.listdir(source_dir):
		source_path = f"{source_dir}/{source_file}"
		destination_file = os.path.splitext(source_file)[0]
		destination_path = f"{destination_dir}/{destination_file}.jpeg"
		if os.path.isfile(source_path) and source_path.endswith(source_ext):
			convert_image(source_path, destination_path)

def convert_image(source_path, destination_path):
	with Image.open(source_path) as img:
		print(f"\nINFO: Processing : {source_path} {img.size} {img.format}")
		img = img.convert('RGB')			#Convert image to RGB
		img = img.rotate(-90, expand=True)	#Rotate 90 degrees clock-wise
		img = img.resize((128,128))			#Resize image to given size
		img.save(destination_path, 'JPEG')			#Save image to new path
		print(f"      Saved as\t : {destination_path} {img.size} {img.format}")

def check_no_of_argvs(argv):
	if not len(argv) == 4:
		print("ERROR: Invalid arguments... Exiting!")
		return False
	return True

def validate_source_dir(source_dir):
	if not os.path.isdir(source_dir):
		print("ERROR: Invalid source directory... Exiting!")
		return False
	return True

def validate_destination_dir(destination_dir):
	if not os.path.isdir(destination_dir):
		print("INFO: Destination directory missing... Creating!")
		try:
			os.mkdir(destination_dir)
		except:
			print("ERROR: Cannot create directory... Exiting!")
			return False
	return True

if __name__ == "__main__":
	main()
