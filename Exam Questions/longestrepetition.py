#!/usr/bin/python
# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

# My solution (Warning: not very elegant!):

def highest(blah):
    highnumber = 0
    highest = 0
    for i in blah:
        if i[1] > highest:
            highnumber = i[0]
            highest = i[1]
    return highnumber

# I started by creating a helper function to determine the highest amount of repetitions of a single 
# element by looping through the list created below. 

def longest_repetition(blah):
	cons = []
	tally = 1 
	counter = 0
	if blah == []:
		return None 		# None for empty list. 
	for i in blah: 			# Loops through each element. 
		if counter == (len(blah) - 1):  # Check for end of list. 
			for e in cons:				# Loops through entire cons list when final element is reached.
				if i == e[0]: 			# Checks if last element is in list and updates tally if it is, 
					if tally > e[1][0]:
						e[1][0] = tally
						return highest(cons)
			else:
				cons.append([i, [tally]]) # appends if not. 
				return highest(cons)
		if blah[counter + 1] != i: # Checks if next element is the same, and if not, 
			for e in cons: 		 
				if i == e[0]: 	# Finds value if present, 
					if tally > e[1][0]:
						e[1][0] = tally # Updates tally if it is larger, 
						tally = 1 	# Resets tally. 
		if blah[counter + 1] == i: # If next element is the same: 
			tally += 1 			# Increments tally, 
			counter += 1		# Increments counter.
		else:
			cons.append([i, [tally]])	# If value is not present (no above conditions are true), 
			tally = 1 					# appends valu, increases tally and counter. 
			counter +=1
	return highest(cons)	# Uses highest function to determine longest repetition. 

# Essentially, the above code keeps track of the tally (how long a single element is repeated in a row), 
# the counter (which is checked against the next element and ultimately the length of the list), and
# and cons (which keeps a list of all of the elements and their longest repetition inside of the 
# list). It is a monster block of code, that starts by looping through each element in the list, 
# checking if the element is already inside cons, then checking if the next element is the same, 
# and then appending the element as a list with a tally if it is not present in cons, or updating the
# tally if it is larger than the current tally (as the same element can be present in the list in 
# different places.) All of the conditional checking and updating of the three variables
# is what makes the block of code so lengthy (resolving even the first example takes 114 steps).

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
# [2, 2]

# Professor's solution (much more elegant, but actually takes more steps to resolve than my 
# messy block of code):

def longest_repetition_prof(input_list):
	best_element = None
	length = 0
	current = None
	current_length = 0
	for element in input_list: 	# Loops through each element. 
		if current != element: 	# Current starts at None, 
			current = element 	# updates if it is different. 
			current_length = 1 	# Resets length (repetition amount) if different. 
		else:
			current_length += 1 # Increments length if it is the same. 
		if current_length > length: # Checks if repetition length is larger than the element with 
			best_element = current # the highest length and updates the best element if so, 
			length = current_length # and updates length (longest) as well. 
	return best_element 




#For example,

print longest_repetition_prof([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition_prof(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition_prof([1,2,3,4,5])
# 1

print longest_repetition_prof([])
# None

print longest_repetition_prof([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
# [2, 2]

