#!/usr/bin/python

#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def rabbits(n):
    if n == 1:
        return 1
    if n == 0:
        return 0			# Two base cases. 
    count = 2				# Count starting at 2. 
    count2 = 0				# Count 2 starting at 0. 
    rabbits = [1, 1] 		# List used to keep track of and continualy add each number in the fibonacci sequence. 
    while count <= n:		# Continues looping from count -> n.
        rabbits.append((rabbits[-2] + rabbits[-1])) 	# Appends sum of last two numbers in current sequence.
        count += 1 			# Increases count. 
    return rabbits[-2] # Return number before last for current generation (as this procedure moves one generation ahead of the target value).

#>>> 14930352