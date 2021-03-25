# Coursera, Algorithms Specialization, Stanford University
# Course 1, Divide and Conquer, Sorting and Searching, and Randomized Algorithms
# Week 1: Integer Multiplication

# Attempts to implement the 3rd-grade multiplication algorithm
# Limitations: Can only accept non-negative integers

import sys

def main():
	num1, num2 = get_argvs()
	num1, num2 = split_digits(num1, num2)
	
	products = get_products(num1, num2)
	pad_with_zero(products)
	answer = add_products(products)

	unpad_zeros(products, answer)
	printify(num1, num2, products, answer)
	verify_answer(num1, num2, answer)


def split_digits(n1, n2):
	"""Takes two numbers and returns them as lists of integer digits"""

	num1 = [int(d) for d in str(n1)]
	num2 = [int(d) for d in str(n2)]
	return num1, num2


def get_products(num1, num2):
	"""Takes two numbers as lists of integers and multiplies them
	to yield a list of partial products as lists of integers"""

	products = [[] for i in range(len(num2))]
	for i, dig2 in enumerate(num2[::-1]):
		carry = 0
		for dig1 in num1[::-1]:
			pp = dig2 * dig1 + carry
			pp, carry = pp % 10, pp // 10
			products[i].insert(0,pp)
		products[i].insert(0,carry)
	return products

def pad_with_zero(products):
	"""Takes a list of lists of partial products and pads each of
	them with 0s on the right according to mathematical rules, and
	on the left to make all of them of equal sizes"""

	# pad right-side with 0s
	for c, pp in enumerate(products):
		for i in range(c):
			pp.append(0)
	# pad left-side with 0s
	for c, pp in enumerate(products[::-1]):
		for i in range(c):
			pp.insert(0, 0)

def add_products(products):
	"""Takes a list of lists of partial products and adds them up
	to yield the final product as a list of integers"""

	flipped_pps = [pp[::-1] for pp in products]
	answer = []
	carry = 0
	for digits in zip(*flipped_pps):
		sum = 0 + carry
		for d in digits:
			sum += d
		sum, carry = sum % 10, sum // 10
		answer.insert(0,sum)
	answer.insert(0,carry)
	return answer


def unpad_zeros(products, answer):
	"""Removes extra 0s on the left and replaces padded 0s on the
	right with periods from the list of lists of partial products.
	Only removes extra 0s on the left from the list of digits."""
	
	def unpad_left(digits):
		"""Removes extra 0s from left"""
		for i, d in enumerate(digits):
			if d!=0: break
		del digits[0:i]
	
	unpad_left(answer)
	for i, pp in enumerate(products):
		unpad_left(pp)
		# replace padded 0s on the right with periods
		for j in range(i):
			pp[-(j+1)] = '.'


def printify(num1, num2, products, answer):
	def merge_digits(val):
		return ' '.join(str(d) for d in val)

	def print_dashes(pad):
		dashes = ''.join('~' for i in range(pad+1))
		print("{:>{}}".format(dashes, pad+1))
	
	pad = len(max(products, key=len)) * 2 + 3
	print("{:>{}}".format(merge_digits(num1), pad))
	print("{:>{}}".format('x  '+ merge_digits(num2), pad))
	print_dashes(pad)

	for pp in products:
		print("{:>{}}".format(merge_digits(pp), pad))
	print_dashes(pad)

	print("{:>{}}".format('=  '+ merge_digits(answer), pad))
	print_dashes(pad)


def verify_answer(num1, num2, answer):
	n1 = int(''.join(str(d) for d in num1))
	n2 = int(''.join(str(d) for d in num2))
	ans = int(''.join(str(d) for d in answer))
	if n1*n2 != ans:
		print(f"{n1} x {n2} is not {ans}\nThe answer here is INCORRECT...")
		print(f"\nKindly send a bug report to the dev,\nincluding the nos. {n1} {n2} in the report.")
		sys.exit(2)


def get_argvs():
	"""Extract two positive integers from the commandline. Exits the
	script if the correct number and type of arguments are not found."""

	if len(sys.argv) < 3:
		print("Requires the 2 numbers to be multiplied as arguments!")
		print("Note: Both numbers must be non-negative.")
		print("Example,\nuser@pc:~$ python3 grade3x.py 1234 5678")
		sys.exit(1)
	return int(sys.argv[1]), int(sys.argv[2])


if __name__ == '__main__':
	main()