#!/usr/bin/python

def is_identity_matrix(matrix):
    i = 0
    while i < len(matrix):
        if len(matrix) != len(matrix[i]):  # Checks each row to ensure proper length
            return False
        j = 0							# Sets j back to 0 after loop below
        while j < len(matrix[i]):		
            if i == j:					# Checks to see if matrix[0][0], matrix[1][1] == 1 and so on
                if matrix[i][j] != 1:   
                    return False
            else:						# Makes sure that every other value is 0, otherwise returns False
                if matrix[i][j] != 0:
                    return False
            j = j + 1
        i = i + 1						# Increments i by 1 and loops through next list until all lists have been checked
    return True

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)


matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False           


# Professor's answer: 


def is_identity_matrix_prof(matrix):
    i = 0
    for e in matrix:
        if len(e) != len(matrix):
            return False
    while i < len(matrix):
        if matrix[i][i] != matrix[0][0]:
            return False
        i += 1
    return True
        



# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix_prof(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix_prof(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix_prof(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix_prof(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix_prof(matrix5)
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

print is_identity_matrix_prof(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix_prof(matrix7)
#>>>False           
