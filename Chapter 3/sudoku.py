#!/usr/bin/python

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.
def create_list(x): 		# Creates a list from x to 1 in descending order
	new_list = [] 			# This list will be used as a checker against the lists
	while x >= 1:
		new_list.append(x)
		x -= 1
	return new_list

def no_duplicates(row):
	checker = create_list(len(row)) 		# Creates a list with all numbers from 1 to len(row)
	checked = [i for i in checker if i in row]  # Creates a separate list, only adding i to the new list if it is present in the initial list
	if len(checked) == len(checker): # Since this will only be true if there are no duplicate numbers 
		return True 		# (as it will only add each number once if present), this is an effective tool to see if any duplicates are present
	else:
		return False

def no_row_duplicates(board):
	total = len(board) 				# len(board) should determine both the amount of rows and columns as a valid sudoku is square
	i = 0 							
	while i <= total: 				
		for row in board: 			# Since each list in this sudoku represents a row, this will check each row by looping through each list
			if no_duplicates(row) == True:
				i += 1 				# Increments i to check next row (next list in the list of lists)
				if i == total: 		# Evaluates to true after all lists have been checked (total = len(board))
					return True
			else: 
				return False



def no_column_duplicates(board):
	i = 0 	 						
	checker = create_list(len(board))
	checked = []
	while i <= len(board): 			# Loops through increments of i to check each column
		for t in board: 			# 
			checked.append(t[i]) 	# Appends each number (t) of a column to checked
		if no_duplicates(checked): 	# Checks numbers in checked against the checker
			i += 1 					# Increments i to move onto next column
			if i == len(board): 	# When i == len(board), all columns have been checked
				return True 		# Returns true if found no duplicates after looping through columns
			checked = []
		else:
			return False
			break

def check_sudoku(board): 	# If there are no row or column duplicates, it is a valid sudoku puzzle
	if no_column_duplicates(board) == True and no_row_duplicates(board) == True:
		return True
	else:
		return False
	





correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

print check_sudoku(correct)
#>>>True

print check_sudoku(correct)
#>>> False

print check_sudoku(incorrect)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False
