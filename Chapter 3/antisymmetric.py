#!/usr/bin/python
# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(p):
    i = j = 0       
    for e in p:         ## for each list in list of lists
        if len(e) != len(p):   ##checks each row length against the column length
            return False
    while i < len(p):        ##loops through each row until last row
        while j < len(p):    ##loops through each column until last column
            if -(p[i][j]) != p[j][i]: ## antisymmetry test, e.g. -p[0][1] must = p[1][0]
                return False
            ##print -(p[i][j])
            ##print p[j][i]
            ##print '\n'
            j = j + 1       ##increment element in first list until it has checked each element
        j = 0           ##reset list[element] back to 0
        i = i + 1       ##move to next list in list of lists
    return True     ##if p[i][j] always = p[j][i]

print antisymmetric([[0, 1, 2], 
                [-1, 0, 3], 
                [-2, -3, 0]])   
# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
