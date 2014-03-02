#!/usr/bin/python
# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

# My solution:

def remove_tags(b):
    for i in b:
        if i == '<':            # Loops through string searching for start of tag ('<').
            c = b.index(i)      # Locates position of start tag.
            d = b.index('>')    # Locates position of end tag.
            b = b[:c] + ' ' + b[d + 1:]    # Modifies b to include portion of string without tag. 
    return b.split()        # Splits b to separate all words. 

print remove_tags('''Title</h1>
    <p>This is a<a href="http://www.udacity.com">link</a>.<p>''')


#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']

# Professor's solution:

def remove_tags_prof(string):
    start = string.find('<')                # Finds first tag. 
    while start != -1:                         # Continues looping until no more '<' are found. 
        end = string.find('>', start)  # Locates nearest closing tag. 
        string = string[:start] + ' ' + string[end + 1:] # Modifies string variable to not include start and end of tag. 
        start = string.find('<')        # Modifies start to locate the next tag. 
    return string                  