#!/usr/bin/python

# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets): 		# Essentially, creates a list with as many lists
    table = []						# inside of it as you want. 
    for i in range(0, nbuckets):
        table.append([])
    return table
        
print make_hashtable(9)