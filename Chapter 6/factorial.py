#!/usr/bin/python

# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

def factorial(n):
    if n == 0 or n == 1: 			# Base case.
        return 1
    else:
        return n * factorial(n-1)	# Recursively multiply numbers together by calling the function
        							# over and over again until base case is achieved. 



#print factorial(0)
#>>> 1

#print factorial(5)
#>>> 120

#print factorial(10)
#>>> 3628800