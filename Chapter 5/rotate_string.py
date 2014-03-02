#!/usr/bin/python

# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


def rotate(x, n):		
    new_string = ''								# Creates a new string for the rotation procedure. 
    alphabet = 'abcdefghijklmnopqrstuvwxyz'		
    for i in x:									# Loops through input string.
        if i == ' ':							
            new_string += i 					# Adds empty space to new string if present. 
        else:									
            t = alphabet.find(i)				# Finds position of character in string. 
            y = t + n 							
            if y >= 25 or y < 0:						
                new_string += (alphabet[(y) % 26])		# Modulo of 26 if y is larger than alphabet length.
            else:									
                new_string += (alphabet[(y) % 25])		# Modulo of 25 if y is within alphabet length. 
    return new_string									# Returns newly constructed (rotated) string. 

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???