#!/usr/bin/python
# Deep Count 

# The built-in len operator outputs the number of top-level elements in a List,
# but not the total number of elements. For this question, your goal is to count
# the total number of elements in a list, including all of the inner lists.

# Define a procedure, deep_count, that takes as input a list, and outputs the
# total number of elements in the list, including all elements in lists that it
# contains.


# For this procedure, you will need a way to test if a value is a list. We have
# provided a procedure, is_list(p) that does this:

def is_list(p):
    return isinstance(p, list)

def deep_count(p):		
    total = 0		
    new_list = []		# Creates a new list to place all elements inside of. 
    while p != []:		# Condition for loop termination.
        for i in p:		# Loops through every element of p (even lists). 
            total += 1		# Increases total elements as it loops through the list. 
            if is_list(i) == True:	# Checks to see if element is a list. 
                new_list += i[0:]	# Adds elements of list to new_list.
        p, new_list = new_list, []	# Swaps values of p and new_list and allows the function to loop through any additional lists. 
    return total			




print deep_count([1, 2, 3])
#>>> 3

# The empty list still counts as an element of the outer list
print deep_count([1, [], 3]) 
#>>> 3 

print deep_count([1, [1, 2, [3, 4]]])
#>>> 7

print deep_count([[[[[[[[1, 2, 3]]]]]]]])
#>>> 10

#prof's solution: 
#def deep_count(p):
#   sum = 0
#   for e in p:
#       sum += 1
#       if is_list(e):
#           sum += deep_count(e)
#   return sum
