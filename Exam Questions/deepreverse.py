#!/usr/bin/python

# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

import copy

def is_list(p):
    return isinstance(p, list)

# My solution: uses deepcopy from the Python copy library. 

def deep_reverse(x):
	new_list = copy.deepcopy(x) # creates a new, separate list of the original list (thus not modifying the original list). 
	new_list.reverse() 	# Reverses each element in the list. 
	for i in new_list:
		if is_list(i):
			i.reverse()
			for e in i:
				if is_list(e):
					e.reverse()
					for t in e:
						if is_list(t):
							t.reverse()  # Each of these lines do the same thing, it goes
	return new_list 					 # 3 levels to see if they are still lists. 


# Professor's solution: more elegant - simply checks if each element is a list and appends it to 
# result in reverse using the range function in reverse. 

def deep_reverse_prof(p):
	if is_list(p):
		result = []
		for i in range(len(p) - 1, -1, -1):
			result.append(deep_reverse_prof(p[i]))
		return result
	else:
		return p


#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse_prof(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse_prof(q)
#>>> [ [6,5], 4, [3, 2], 1]
#print q
#>>> [1, [2,3], 4, [5,6]]

