# Coursera, Applied Data Science with Python, University of Michigan
# Course 1, Introduction to Data Science in Python
# Week 1: Fundamentals of Data Manipulation with Python

# Extracts the United States Constitution from the famous
# Abraham Lincoln "cracked glass plate" photograph.
# Cypher: put every character in the text in every prime
# numbered pixel of the image, starting from pixel 1787


import math
import numpy as np
from PIL import Image

def main():
	img_path = 'images/lincoln-encoded.png'
	org_txt_path = 'files/usa-constitution.txt'
	dec_txt_path = 'files/usa-constitution-decoded.txt'

	img_array = get_img_array(img_path)
	txt_array = decode_txt(img_array)
	save_text(txt_array, dec_txt_path)
	verify_decode(org_txt_path, dec_txt_path)


def decode_txt(img_array):
	org_shape = img_array.shape
	img_array = img_array.flatten()
	txt_array = ''
	prime_pixels = get_prime_pixels(img_array.shape[0])

	print("Extracting text from prime-numbered pixels in image...", end=' ')  #verbose
	for pixel in prime_pixels:
		txt_array += chr(img_array[pixel])
	img_array = img_array.reshape(org_shape)

	print("DONE!")  #verbose
	return txt_array


def get_prime_pixels(limit):
	def is_prime(num):
		for div in range(3, int(math.sqrt(num))+1, 2):
			if num % div == 0:
				return False
		return True
	
	print("Calculating no. of prime-numbered pixels in the image...")  #verbose
	prime_pixels = []
	for num in range(1787, limit, 2):
		if is_prime(num):
			prime_pixels.append(num)
	
	print(f"Image has {len(prime_pixels)} prime-numbered pixels...")  #verbose
	return prime_pixels


def get_img_array(path):
	with Image.open(path) as img:
		img_array = np.array(img)
	
	print(f"{path} has {img_array.size} pixels in total")  #verbose
	return img_array


def save_text(txt_array, path):
	with open(path, 'w') as file:
		file.write(txt_array)
	print(f"Decoded text saved as {path}")  #verbose


def verify_decode(org_txt_path, dec_txt_path):
	with open(org_txt_path, 'r') as org_file:
		org_txt = org_file.read()
	with open(dec_txt_path, 'r') as dec_file:
		dec_txt = dec_file.read()
	
	if org_txt == dec_txt:
		print("Decoded file MATCHES EXACTLY with the original file.")  #verbose
	elif org_txt in dec_txt:
		print("Decoded file contains the text in the original file, but DOES NOT MATCH exactly.")  #verbose
	else:
		print("ERROR: Decoding Unsuccessful! The decoded file DOES NOT MATCH with the original")  #verbose
		return False
	return True
	

if __name__ == '__main__':
	main()