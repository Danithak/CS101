#!/usr/bin/python
# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.

# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(x, y):
    i = 0
    while True:
        if x.find(y, i) == -1:
            break						## breaks if string is not found.
        else:
            i+=1 						## keeps looping until the string is no longer found. 
    return x.find(y, i-1)				## returns last known string location 
    									## (increment of i before last).

print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0




