#!/usr/bin/python

# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'		
    x = alphabet.find(letter)					# Find position of letter in alphabet. 
    y = x + n 									# Add position and desired letter shift amount. 
    if y >= 25 or y < 0:						
        return alphabet[(x + n) % 26]			# Modulo of 26 necessary for values of y larger 
    else:										# than the length of the alphabet or negative numbers. 
        return alphabet[(x + n) % 25]			# Modulo of 25 suitable for values of y within the  
        										# length of the alphabet.


print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i