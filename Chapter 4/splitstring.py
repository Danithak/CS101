#!/usr/bin/python

# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

def split_string(source,splitlist):
    word = ""
    result = []
    for e in source:
        if e not in splitlist:
            word += e
        else:
            if word:
                result.append(word)
                word = ""
    if word:
        result.append(word)
    return result

# This function essentially loops through each character individually and adds it to the
# word variable up until the point that a character in the splitlist is found.
# After finding one of those character, it adds the word to the result list, resets
# the word variable, and loops through the remaining characters concatenating them
# if they aren't in the list, or finishing off the word, adding it, and then starting
# a new word every time a character from the splitlist is found. 

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
#print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']