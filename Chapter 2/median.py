#!/usr/bin/python
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))        ## resolves which of b and c is bigger then checks 
                                        ## against a.
def median(a, b, c):                       
    i = biggest(a,b,c)
    if a == i:                          ## stores largest variable, then returns larger of
        return bigger(b,c)              ## two leftovers to determine median number of 
    if b == i:                          ## a set of 3.
        return bigger(a,c)
    if c == i:
        return bigger(a,b)

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7







