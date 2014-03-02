#!/usr/bin/python
# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def triangle(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:                    # Three exceptions are listed, the function will create the proper triangle for n above 3.
        return [[1], [1, 1]]
    x = 3
    triangle_list = [[1], [1, 1]]   # Base for triangle in function
    completed_row = [1, 1]      # Variable for last row created
    new_row = []
    while x <= n:
        for i in range(0, (len(completed_row) - 1)): # Loops through first through next to last value in list.
            new_row.append((completed_row[i] + completed_row[i +1])) # Appends the sum of the current value and the next. 
        new_row.insert(0, 1)    # Inserts 1 at the beginning of the row.
        new_row.append(1)   # Inserts 1 at the end of the row. 
        x += 1              # Increments x
        triangle_list.append(new_row)   # Adds newly completed row to kayyam triangle.
        completed_row, new_row = new_row, [] # Updates created_row to new_row, resets new_row.
    return triangle_list

print triangle(10)

# While my code is not as elegant as the professor's, it does the same work using
# a few extra exceptions and directly inputting 1's into the start and the end of the row. 
# Line 43 adds the first and the next number together up until the next to last number (as there are 
# no more numbers to the right of the last number in the list).

# Essentially, the code works like this:
# [1, 1]
# Adds 1 and 1 -> 2
# Insert and append 1: [1, 2, 1]
# Next loop: 1 + 2 = 3 and 2 + 1 = 3
# [3, 3]
# Insert and append 1: [1, 3, 3, 1]
# Next loop: 1 + 3 = 4, 3 + 3 = 6, 3 + 1 = 4
# [4, 6, 4]
# Insert and append 1: [1, 4, 6, 4, 1]

# Professor's answer below: 

def make_next_row(row):
  result = []
  prev = 0
  for e in row:
    result.append(e + prev)
    prev = e
  result.append(prev)
  return result

def triangle_prof(n):
  result = []
  current = [1]
  for unused in range(0, n):
    result.append(current)
    current = make_next_row(current)
  return result


# Professor's answer uses a separate function to make every row, and uses the primary function to 
# create n amount of new rows to add to the kayyam triangle.
# The first function has two variables to keep track of the old and new row and continue to increase
# the value of the rows by adding the old value together and updating the values as the function
# continues to loop. 

print triangle(8)


#For example:

print triangle(0)
#>>> []

print triangle(1)
#>>> [[1]]

print triangle(2)
#>> [[1], [1, 1]]

print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

#print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
