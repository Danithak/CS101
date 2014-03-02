#!/usr/bin/python
# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
	converter = match, replacement
	return converter

# Creates a converter variable with converter[0] as the string to be replaced and converter[1]
# as the replacement. 

def apply_converter(converter, string):
    if converter[0] in string:
        string = string.replace(converter[0], converter[1]) 	
        string = apply_converter(converter, string)
    return string

# Replaces converter[0] with converter[1] until no more instances of converter[0] remain.



# For example,

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever).


# Professor's solution:

def make_converter_prof(match, replacement):
	converter = [match, replacement]

def apply_converter_prof(converter, string):
	previous = None
	while previous != string:
		previous = string
		position = string.find(converter[0])
		if position != -1:
			string = string[:position] + converter[1] + string[position + len(converter[0]):]
		return string

c2 = make_converter_prof('aa', 'a')
print apply_converter_prof(c2, 'aaaa')
#>>> a

c3 = make_converter_prof('aba', 'b')
print apply_converter_prof(c3, 'aaaaaabaaaaa')
#>>> ab