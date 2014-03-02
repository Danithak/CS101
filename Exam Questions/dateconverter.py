#!/usr/bin/python
# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is 
# a dictionary and the second a string. The string is a valid date in 
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".
# Hint: int('12') converts the string '12' to the integer 12.

# My solution:
# Removes '/' from the date and then takes the month and concatenates the day of the month and year on 
# the end after converting the month from the particular language. 

def date_converter(language, string):
	string = string.replace('/', ' ')  
	string = string.split()
	return str(string[1] + ' ' + language[int(string[0])] + ' ' + string[2])

# Needs to be a string in order to concatenate, but uses int to make sure value can be retrieved from key. 
		

# Professor's solutions:

def date_converter_prof(language, date):
	first = date.find('/')
	month = date[:first]
	second = date.find('/', first + 1)
	year = date[second + 1:]
	return day + ' ' + language[int(month)] + ' ' + year

# Three line solution:

def date_converter_prof_2(language, date):
	month, day, year = date.split('/')
	return day + ' ' + language[int(month)] + ' ' + year



print date_converter_prof(english, '5/11/2012')
#>>> 11 May 2012

print date_converter_prof(english, '5/11/12')
#>>> 11 May 12

print date_converter_prof(swedish, '5/11/2012')
#>>> 11 maj 2012

print date_converter_prof(swedish, '12/5/1791')
#>>> 5 december 1791
