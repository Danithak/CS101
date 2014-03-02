#!/usr/bin/python
# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.

## Bottom line, check to see if the second input string can be created from letters and 
## symbols present in the second input string. 

def fix_machine(debris, product):
    i = 0						## Sets i to first location in string
    while i < len(product):		## Loops through the entire second string
    	t = product[i]			## Sets t to corresponding letter in second string
    	if debris.find(t) < 0: 	## Checks to see if corresponding letter is present in first string
    		return "Give me something that's not useless next time."   ## Statement when product cannot be created from debris
    	i +=1 					## Sets i to next value of second string
    return product 				## Returns second string if it can be constructed from letters
								## present in first string after looping through every letter/symbol.

### TEST CASES ###		
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'