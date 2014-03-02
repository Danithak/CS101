#!/usr/bin/python

# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):   # Creates a hash as a function of the amount of letters inside 
    b = 0                           # of the keyword and the amount of buckets you want to use. 
    for i in keyword:               # This hash function makes lookup much faster. 
        b += ord(i)
    return b % buckets
        




print hash_string('a',12)
#>>> 1

print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

print hash_string('au',12)
#>>> 10

print hash_string('udacity',12)
#>>> 11



