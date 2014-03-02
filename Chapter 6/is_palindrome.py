#!/usr/bin/python

# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if s == '': 					# Base case (empty string).
        return True					#
    first = s[0]					# 
    last = s[-1]					#
    if first == last:				# Compares first and last letter in the string, increments string 
        s = s[1:-1]					# position both ways, and continues calling the function
        return is_palindrome(s)		# recursively if the letters match.
    else:							# Returns True if base case is met, False if the letters fail to match
        return False				# at any point. 
 
 
 
 
print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True