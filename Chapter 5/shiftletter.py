#!/usr/bin/python
# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):									
    alphabet = 'abcdefghijklmnopqrstuvwxyz'			
    x = alphabet.find(letter)				# Returns position of letter.
    if x == 25: 							# Since there are 26 letters in the alphabet, 
        return 'a'							# created a rule that would return a if letter == z (position 25.
    else:									# Otherwise, returned letter in next position of string. 
        return alphabet[x + 1]



print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a