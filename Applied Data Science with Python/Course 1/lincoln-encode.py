# Coursera, Applied Data Science with Python, University of Michigan
# Course 1, Introduction to Data Science in Python
# Week 1: Fundamentals of Data Manipulation with Python

# Embeds the United States Constitution into the famous
# Abraham Lincoln "cracked glass plate" photograph.
# Cypher: put every character in the text in every prime
# numbered pixel of the image, starting from pixel 1787


import math
import numpy as np
from PIL import Image

def main():
	img_path = 'images/lincoln-clean.png'
	txt_path = 'files/usa-constitution.txt'

	img_array = get_img_array(img_path)
	txt_array = get_txt_string(txt_path)

	img_array = encode_txt(img_array, txt_array)
	save_image(img_array, 'images/lincoln-encoded.png')


def encode_txt(img_array, txt_array):
	org_shape = img_array.shape
	img_array = img_array.flatten()
	prime_pixels = get_prime_pixels(img_array.shape[0])

	print("Embedding text into prime-numbered pixels in image...", end=' ')  #verbose
	for pixel, char in zip(prime_pixels, txt_array):
		img_array[pixel] = ord(char)
	img_array = img_array.reshape(org_shape)
	img_array = img_array.astype(np.uint8)

	print("DONE!")  #verbose
	return img_array


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


def save_image(img_array, path):
	img = Image.fromarray(img_array)
	img.save(path, format='PNG', optimize=False)
	print(f"Encoded image saved as {path}")  #verbose


def get_img_array(path):
	with Image.open(path) as img:
		img = img.convert('L')
		img_array = np.array(img)
	
	print(f"{path} has {img_array.size} pixels in total")  #verbose
	return img_array


def get_txt_string(path):
	with open(path, 'r') as file:
		txt_array = file.read()
	
	print(f"{path} has {len(txt_array)} characters in total")  #verbose
	return txt_array


if __name__ == '__main__':
	main()