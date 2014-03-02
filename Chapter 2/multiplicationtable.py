#!/usr/bin/python
# 2 GOLD STARS

# Define a procedure, print_multiplication_table,
# that takes as input a positive whole number, and prints out a multiplication,
# table showing all the whole number multiplications up to and including the
# input number. The order in which the equations are printed matters.

# Hint: You can not add an integer and a string, but in homework 1.9
# you came across a method, str, for turning an integer into a string.

def print_multiplication_table(n):
    x = 1							## starts multiplication table with first # as 1
    while x <= n:					## loops until x reaches n
        y = 1						## resets y to 1 after y has been increased to n
        while y <= n:				## loops until y reaches n
            print str(x) + ' * ' + str(y) + ' = ' + str(x*y)		## prints a separate line for each multiplication and allows it to be concatenated
            y += 1					## increments y by 1 to create a line for each number up to n
        x += 1						## increments x to start the process over for the next number up to n
        
            


print_multiplication_table(2)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4

print_multiplication_table(3)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 1 * 3 = 3
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4
#>>> 2 * 3 = 6
#>>> 3 * 1 = 3
#>>> 3 * 2 = 6
#>>> 3 * 3 = 9


