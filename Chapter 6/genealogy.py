#!/usr/bin/python
# Single Gold Star

# Family Trees

# In the lecture, we showed a recursive definition for your ancestors. For this
# question, your goal is to define a procedure that finds someone's ancestors,
# given a Dictionary that provides the parent relationships.

# Here's an example of an input Dictionary:

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }

# Define a procedure, ancestors(genealogy, person), that takes as its first input
# a Dictionary in the form given above, and as its second input the name of a
# person. It should return a list giving all the known ancestors of the input
# person (this should be the empty list if there are none). The order of the list
# does not matter and duplicates will be ignored.

def ancestors(genealogy, person):
    known_ancestors = []          # Creates a new list. 
    if person in genealogy:       # Checks to see if name of person in input is in list. 
        for parent in genealogy[person]:  # Checks parents of person. 
            known_ancestors.append(parent)  # Appends parents to known_ancestors. 
            if parent in genealogy:         # Checks if parent is in the extended geneaology list.
                for grandparent in genealogy[parent]: 
                    if grandparent in genealogy:  # Checks to see if parent's parents are in the geneaology list. 
                        for great_grandparent in genealogy[grandparent]:
                            known_ancestors.append(great_grandparent)   # Appends grandparents to known_ancestors. 
                    known_ancestors.append(grandparent)
    return known_ancestors

# My answer looped through the dictionary several layers deep, and is not likely the most efficient 
# possible answer. Additionally, it will not look for anything beyond a grandparent, which is a 
# limitation. 

# Professor's answer using recursion: 
def ancestors_prof(genealogy, person):
    if person in genealogy:
        parents = genealogy[person]
        result = parents
        for parent in parents:
            result += ancestors(genealogy, parent)
        return result
    return []





# Here are some examples:

print ancestors(ada_family, 'Augusta Ada King')
#>>> ['Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon','Captain John Byron']

print ancestors(ada_family, 'Judith Blunt-Lytton')
#>>> ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King',
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon', 'Captain John Byron']

print ancestors(ada_family, 'Dave')
#>>> []

