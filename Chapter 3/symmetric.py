#!/usr/bin/python
# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(p):
    i = j = 0       
    for e in p:         ## For each list in list of lists
        if len(e) != len(p):   ## Checks each row length against the column length
            return False
    while i < len(p):        ## Loops through each row until last row
        while j < len(p):    ## Loops through each column until last column
            if (p[i][j]) != p[j][i]: ## Symmetry test, e.g. p[0][1] must = p[1][0]
                return False
            j = j + 1       ## Increment element in first list until it has checked each element
        j = 0           ## Reset list[element] back to 0
        i = i + 1       ## Move to next list in list of lists
    return True     ## If p[i][j] always = p[j][i]

print symmetric([[0, 1, 2], 
                [1, 0, 3], 
                [2, 3, 0]])   
#>>> True

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
##>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False
