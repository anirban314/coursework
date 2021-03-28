# Coursera, Applied Data Science with Python, University of Michigan
# Course 1, Introduction to Data Science in Python
# Week 2: Basic Data Processing with Pandas

# Speed comparison between different methods of adding floating-point numbers


import time
import numpy as np
import pandas as pd

def main():
	limit = 10000000

	tick = time.time_ns()
	ran_floats = np.random.sample(limit)
	tock = time.time_ns()
	elapsed = round((tock-tick)/1E6, 3)
	print(f"Time taken to generate {limit} floating-point numbers: {elapsed} ms")

	numbers = pd.Series(ran_floats)
	result = 0.0
	
	print("\nSum using ITERATION...")
	tick = time.time_ns()
	for number in numbers:
		result = result + number
	tock = time.time_ns()
	elapsed = round((tock-tick)/1E6, 3)
	print(f"Result  = {result}\nElapsed = {elapsed} ms")

	print("\nSum using built-in sum()...")
	tick = time.time_ns()
	result = sum(numbers)
	tock = time.time_ns()
	elapsed = round((tock-tick)/1E6, 3)
	print(f"Result  = {result}\nElapsed = {elapsed} ms")

	print("\nSum using VECTORIZATION on Pandas Series...")
	tick = time.time_ns()
	result = np.sum(numbers)
	tock = time.time_ns()
	elapsed = round((tock-tick)/1E6, 3)
	print(f"Result  = {result}\nElapsed = {elapsed} ms")

	print("\nSum using VECTORIZATION on Numpy Array...")
	tick = time.time_ns()
	result = np.sum(ran_floats)
	tock = time.time_ns()
	elapsed = round((tock-tick)/1E6, 3)
	print(f"Result  = {result}\nElapsed = {elapsed} ms")


if __name__ == '__main__':
	main()